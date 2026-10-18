# Project 1 — Decision memo (working submission source)

**Status: incomplete; not an approved committee valuation.**

**Decision: WATCH / DEFER**, provisionally. Target: Walmart Inc. (WMT) common equity. The fund holds no position. Forecast horizon: five years, FY2027–FY2031. Currency: USD; accounting figures in USD millions. Historic price date used in the prior reverse DCF: September 9, 2026, **not independently reconfirmed here**.

## Investment thesis and evidence
Walmart benefits from grocery demand, scale and growing higher-margin offerings, but the attractiveness of the *stock* depends on future FCFF relative to its market price. See the [original filing-based business analysis](../walmart-investment-analysis.md) (FY2025 research as of March 14, 2025) and the [separate historical evidence ledger](../project1/historical-evidence-and-normalization.md) for the current model's FY2026 opening amounts. **Do not treat the original report's older information set as contemporaneous 2026 evidence.**

## Valuation and disagreement
The [integrated model](../models/walmart_project1.py) produces provisional low/base/high operating FCFF DCF cases derived from the Walmart three-statement pro forma. The current cash/debt-to-common-equity bridge omits verification of noncontrolling interests, lease treatment and other claims. Accordingly, its per-share figures are **sensitivity proxies, not a defensible investment range**.

The [peer calculator](../models/walmart_peer_pe.py) contains candidate equity P/E observations, but no independently verified same-date peer enterprise values/EBITDA. The [relative-valuation policy and missing EV data](../project1/peer-enterprise-multiples.md) must be completed. Differences between cash-flow and market-multiple approaches should be explained through assumptions and business models; do not average inconsistent estimates.

## Downside and conditions
The model's low case combines weaker growth and gross margin with SG&A pressure and additional capex. Initiate only when a source-reconciled FCFF valuation and a qualified EV and equity multiple comparison establish an adequately justified margin of safety against a dated market quote. Monitor comparative sales, margins, cash conversion, capex, debt/leases, advertising and membership revenue, and diluted share count. Reconsider if low-case fundamentals become the likely trajectory.

## Finalization required
Supply a **defensible numerical valuation interval**, reconciled balance-sheet/FCFF share basis, independently confirmed trading-date peer multiples and WACC evidence, and decision thresholds. Freeze the substantive memo and export to `docs/decision-memo.pdf` for repository delivery and `Decision-Memo.pdf` for Brightspace. This Markdown is a working source and **not the required final PDF**.

For a longer original draft see [Edition B committee memo](../project1/edition-b-committee-memo.md).
