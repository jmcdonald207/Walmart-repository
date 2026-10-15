"""Five-year discounted cash flow (DCF) valuation. USD amounts in millions."""

# ==================== EDITABLE INPUTS ====================
starting_fcff = 100.0             # USD millions, at Year 0
yearly_growth_rates = [0.08, 0.06, 0.05, 0.04, 0.03]  # Years 1-5
wacc = 0.10
terminal_growth = 0.03
non_operating_cash = 50.0         # USD millions
debt = 300.0                       # USD millions
diluted_shares = 50.0             # millions of shares
# =======================================================


def main():
    if len(yearly_growth_rates) != 5:
        raise SystemExit("Error: Provide exactly five yearly growth rates.")
    if terminal_growth >= wacc:
        raise SystemExit("Error: Terminal growth must be less than WACC.")
    if wacc <= -1:
        raise SystemExit("Error: WACC must be greater than -100%.")
    if diluted_shares <= 0:
        raise SystemExit("Error: Diluted shares must be greater than zero.")

    fcff = starting_fcff
    cash_flows = []
    for growth in yearly_growth_rates:
        fcff *= 1 + growth
        cash_flows.append(fcff)

    pv_explicit_fcff = sum(
        flow / (1 + wacc) ** year
        for year, flow in enumerate(cash_flows, start=1)
    )
    terminal_value_year_5 = cash_flows[-1] * (1 + terminal_growth) / (wacc - terminal_growth)
    pv_terminal_value = terminal_value_year_5 / (1 + wacc) ** 5
    enterprise_value = pv_explicit_fcff + pv_terminal_value
    equity_value = enterprise_value + non_operating_cash - debt
    value_per_share = equity_value / diluted_shares
    terminal_share_of_ev = pv_terminal_value / enterprise_value if enterprise_value != 0 else float("nan")

    for year, flow in enumerate(cash_flows, start=1):
        print(f"FCFF Year {year} (USD millions): {flow:.4f}")
    print(f"PV of Years 1-5 FCFF (USD millions): {pv_explicit_fcff:.4f}")
    print(f"Terminal value at Year 5 (USD millions): {terminal_value_year_5:.4f}")
    print(f"PV of terminal value (USD millions): {pv_terminal_value:.4f}")
    print(f"Enterprise value (USD millions): {enterprise_value:.4f}")
    print(f"Equity value (USD millions): {equity_value:.4f}")
    print(f"Value per diluted share (USD): {value_per_share:.4f}")
    print(f"PV of terminal value / enterprise value: {terminal_share_of_ev:.4f}")


if __name__ == "__main__":
    main()
