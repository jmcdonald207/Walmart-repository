"""Lab 11: reproducible one-driver-at-a-time Walmart sensitivity.
Uses the actual pro-forma engine; no invented output numbers.
Run from repository root: python models/walmart_sensitivity.py
"""
import copy
import importlib.util
from pathlib import Path

source = Path(__file__).with_name("walmart_proforma.py")
spec = importlib.util.spec_from_file_location("walmart_proforma", source)
model = importlib.util.module_from_spec(spec)
spec.loader.exec_module(model)

BASE = copy.deepcopy(model.A)
# Judgement ranges are illustrative until supported by historical evidence.
SHIFTS = {"gross_margin": 0.005, "sga_ratio": 0.01}
TOLERANCE = 1e-6

def assert_close(actual, expected, label):
    if abs(actual - expected) > TOLERANCE:
        raise AssertionError(f"{label}: actual {actual}, expected {expected}")


def evaluate(assumptions):
    model.A = copy.deepcopy(assumptions)
    rows = model.project()
    model.assert_balanced(rows)
    # Independently reconcile cash movement to the balance-sheet cash each year.
    previous_cash = model.OPEN["cash"]
    for row in rows:
        cash_from_flows = (previous_cash + row["fcfe"] - row["buyback"]
                           + row["rev_draw"] - row["rev_repay"])
        assert_close(row["cash"], cash_from_flows,
                     f"Fiscal-start year {row['year']} ending cash tie")
        previous_cash = row["cash"]
    equity, terminal_share, price = model.value(rows)
    return {
        "operating_income": rows[-1]["op_income"],
        "fcfe": rows[-1]["fcfe"],
        "price": price,
        "balance_gap": max(abs(r["gap"]) for r in rows),
        "terminal_share": terminal_share,
    }

def main():
    try:
        baseline = evaluate(BASE)
        print("BASE", baseline)
        print("NOTE: This reruns the CURRENT walmart_proforma.py assumptions; "
              "older saved Lab 11 figures are not its validation target.")
        for key, shift in SHIFTS.items():
            if key not in BASE or len(BASE[key]) != len(model.YEARS):
                raise ValueError(f"Invalid driver path or year count: {key}")
            if shift <= 0:
                raise ValueError(f"Shift must be positive: {key}")
            print("\nDRIVER:", key, "shift", shift, "absolute ratio points")
            cases = {}
            for name, direction in (("lower", -1), ("base", 0), ("higher", 1)):
                inputs = copy.deepcopy(BASE)
                inputs[key] = [v + direction * shift for v in BASE[key]]
                result = evaluate(inputs)
                if name == "base":
                    for metric in ("operating_income", "fcfe", "price", "terminal_share"):
                        assert_close(result[metric], baseline[metric],
                                     f"{key} base {metric}")
                cases[name] = result
                print(name, "values:", inputs[key])
                print(" outputs:", result)
                print(" changes from base:", {
                    k: result[k] - baseline[k]
                    for k in ("operating_income", "fcfe", "price")
                })
            print("OUTPUT SPANS:", {
                k: max(v[k] for v in cases.values()) - min(v[k] for v in cases.values())
                for k in ("operating_income", "fcfe", "price")
            })
        restored = evaluate(BASE)
        for key in ("operating_income", "fcfe", "price"):
            assert_close(restored[key], baseline[key], "Base restoration: " + key)
        print("\nRESTORED BASE PASS", restored)
    finally:
        model.A = BASE

if __name__ == "__main__":
    main()
