"""Integrated Walmart Project 1 analytical model (standard library only).
Training/illustrative forecast assumptions; NOT independently verified fair value.
Run: python models/walmart_project1.py
"""
from __future__ import annotations
import copy
import importlib.util
from pathlib import Path

def load_proforma():
    p = Path(__file__).with_name("walmart_proforma.py")
    spec = importlib.util.spec_from_file_location("wmt_forecast", p)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

M = load_proforma()
BASE = copy.deepcopy(M.A)
SCENARIOS = {
    "low": {"growth": -0.015, "gross_margin": -0.006, "sga_ratio": 0.012, "capex": 2000.0},
    "base": {"growth": 0.0, "gross_margin": 0.0, "sga_ratio": 0.0, "capex": 0.0},
    "high": {"growth": 0.010, "gross_margin": 0.003, "sga_ratio": -0.005, "capex": -1000.0},
}
WACC = 0.075  # ASSUMPTION; needs independent capital-cost evidence.
TERMINAL_GROWTH = 0.025
MARKET_PRICE = 105.83  # Historic 2026-09-09 price from earlier project notes; independently verify.
# Total equity includes noncontrolling interests, so do not silently treat all EV as common equity.
NONCONTROLLING_INTEREST = None  # Must source and reconcile before a committee-ready EV bridge.
OTHER_NONOPERATING_ADJUSTMENTS = None  # Pension, investments, lease definition, etc.

def scenario_inputs(name):
    shifts = SCENARIOS[name]
    inputs = copy.deepcopy(BASE)
    for key in ("growth", "gross_margin", "sga_ratio"):
        inputs[key] = [v + shifts[key] for v in BASE[key]]
    inputs["capex"] = [v + shifts["capex"] for v in BASE["capex"]]
    return inputs

def project(name):
    M.A = scenario_inputs(name)
    try:
        rows = M.project()
        M.assert_balanced(rows)
        beginning = M.OPEN["cash"]
        for r in rows:
            expected = beginning + r["fcfe"] - r["buyback"] + r["rev_draw"] - r["rev_repay"]
            assert abs(expected - r["cash"]) < 1e-6, f"Cash tie failed {r['year']}"
            beginning = r["cash"]
        return rows
    finally:
        M.A = copy.deepcopy(BASE)

def fcff_by_year(rows):
    """Unlever FCFE: remove net borrowing and add after-tax financing charges.
    Model's only interest-bearing finance is debt and revolver; 'floor_plan' represents
    non-interest-bearing accounts payable. Tax shield uses positive operating EBIT.
    """
    values = []
    for r in rows:
        interest_after_tax = r["interest"] * (1.0 - M.A["tax_rate"][M.YEARS.index(r["year"])])
        # FCFE already subtracts scheduled debt repayment, but ignores revolver
        # draws/repayment, which are financing items outside FCFE.
        fcff = r["fcfe"] + r["repay"] + interest_after_tax
        values.append(fcff)
    return values

def dcf(fcff, wacc=WACC, terminal_g=TERMINAL_GROWTH):
    if wacc <= 0 or terminal_g >= wacc:
        raise ValueError("Require positive WACC and terminal growth below WACC")
    pv_explicit = sum(cf / (1+wacc)**(t+1) for t,cf in enumerate(fcff))
    tv = fcff[-1]*(1+terminal_g)/(wacc-terminal_g)
    pv_tv = tv/(1+wacc)**len(fcff)
    enterprise = pv_explicit+pv_tv
    debt = M.OPEN["debt"] + M.OPEN["revolver"]
    cash = M.OPEN["cash"]
    # Provisional common equity proxy, with known omitted claims expressly unresolved.
    equity_proxy = enterprise + cash - debt
    price_proxy = equity_proxy/M.SHARES
    return dict(enterprise=enterprise, pv_explicit=pv_explicit, pv_terminal=pv_tv,
                terminal_share=pv_tv/enterprise, debt=debt, cash=cash,
                equity_proxy=equity_proxy, price_proxy=price_proxy)

def verify():
    assert len(M.YEARS)==5
    opening_a = sum(M.OPEN[k] for k in ("cash","inventory","ppe","other_assets"))
    opening_le = sum(M.OPEN[k] for k in ("floor_plan","debt","revolver","other_liab","equity"))
    assert abs(opening_a-opening_le)<1e-6, "Opening accounting identity fails"
    # An opening accounting identity is NOT a filing normalization/source reconciliation.
    base = fcff_by_year(project("base"))
    lower_wacc = dcf(base,wacc=WACC-0.01)["price_proxy"]
    higher_wacc = dcf(base,wacc=WACC+0.01)["price_proxy"]
    assert lower_wacc > higher_wacc, "DCF WACC monotonicity failed"
    assert dcf(base,terminal_g=0.03)["price_proxy"] > dcf(base,terminal_g=0.02)["price_proxy"], "terminal growth monotonicity failed"
    try:
        dcf(base,wacc=0.05,terminal_g=0.05)
        raise AssertionError("DCF invalid terminal growth should fail")
    except ValueError:
        pass
    try:
        broken = project("base")
        broken[0]["gap"] += 10
        M.assert_balanced(broken)
        raise AssertionError("Broken balance sheet should fail")
    except AssertionError as e:
        if "should fail" in str(e):
            raise
    return base

def reverse_growth_shift(base_rows, market_price=MARKET_PRICE):
    """Uniform growth shift in all five revenues, holding all other forecast assumptions fixed.
    A solution is conditional on the provisional bridge, not a sourced market-implied conclusion.
    """
    def compute(shift):
        original=SCENARIOS["base"]["growth"]
        SCENARIOS["base"]["growth"]=shift
        try:
            return dcf(fcff_by_year(project("base")))["price_proxy"]
        finally:
            SCENARIOS["base"]["growth"]=original
    lo,hi=-0.025,0.2
    a,b=compute(lo),compute(hi)
    if not (a<=market_price<=b):
        return None,(a,b)
    for _ in range(55):
        mid=(lo+hi)/2
        if compute(mid)<market_price: lo=mid
        else: hi=mid
    return (lo+hi)/2,(a,b)

def main():
    verify()
    print("WALMART PROJECT 1 | FY2027-FY2031 | USD millions except per share")
    print("IMPORTANT: scenario values, WACC and bridge are PROVISIONAL; not a committee-ready fair value.")
    print("SOURCE BASIS: model labels FY2026 Walmart 10-K; filing date and values require independent verification.")
    results={}
    for name in ("low","base","high"):
        rows=project(name)
        fcff=fcff_by_year(rows)
        result=dcf(fcff)
        results[name]=result
        print(f"\\n{name.upper()} | Year 1-5 FCFF: "+", ".join(f"{n:,.2f}" for n in fcff))
        print(" FY2031 operating income:",round(rows[-1]["op_income"],2))
        print(" PV explicit:",round(result["pv_explicit"],2),
              "PV terminal:",round(result["pv_terminal"],2))
        print(" EV:",round(result["enterprise"],2),
              "Cash:",result["cash"],"Interest debt:",result["debt"])
        print(" COMMON EQUITY PROXY:",round(result["equity_proxy"],2),
              "VALUE/SHARE PROXY:",round(result["price_proxy"],2),
              "Terminal share:",f'{result["terminal_share"]:.2%}')
    for wacc in (0.065,0.075,0.085):
        print("WACC",f"{wacc:.1%}",":", " ".join(
            f"g={g:.1%} -> {dcf(fcff_by_year(project('base')),wacc,g)['price_proxy']:.2f}"
            for g in (0.015,0.025,0.035)))
    rev,bounds=reverse_growth_shift(project("base"))
    print("REVERSE DCF uniform REVENUE growth adjustment:",
          "NOT BRACKETED: "+str(bounds) if rev is None else f"{rev:+.4%}")
    print("CHECKS PASS: 5-year BS and cash ties; WACC/g monotonicity; invalid g boundary; fail-loud balance stress.")
    print("NOT YET VERIFIED: normalized base; opening filing lines; WACC weights; NCI & other EV bridge adjustments; market prices; peer EV/EBITDA.")
    print("Do not treat scenario endpoints as a committee valuation range until these are verified.")

if __name__=="__main__":
    main()
