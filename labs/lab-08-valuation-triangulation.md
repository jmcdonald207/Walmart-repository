# Lab 08 — Walmart comparable-company valuation and triangulation

**Status: working draft; input verification and actual challenge record outstanding.**  
Target: Walmart (WMT). Comparison date: September 9, 2026. USD per share. Annual GAAP diluted EPS.

## Decision and peer policy (before selecting the final set)
Candidate companies must have meaningful overlapping U.S. mass retail or club retail economics, identifiable annual GAAP earnings, consistent dated prices, and sufficiently similar profitability and growth prospects to explain differences. A shared retail label alone is insufficient. Earnings must have been publicly released by the valuation date. Reported and adjusted EPS cannot be combined.

| Candidate | Provisional decision | Reason | Verification to complete |
|---|---|---|---|
| Target (TGT) | Use | Broad-store retail and substantial merchandise overlap; different discretionary mix and scale | Read business and EPS sections in contemporaneous 10-K |
| Costco (COST) | Qualify | High-volume retail but membership warehouse model and different margin economics | Read business and EPS sections in contemporaneous 10-K |
| Dollar General (DG) | Investigate | Discount consumables; smaller box, different basket and customer mix | Source-check before adding |
| Dollar Tree (DLTR) | Investigate | Discount retail; discontinued-operations comparability concern | Check earnings definition |
| BJ's (BJ) | Investigate | Membership club model; lower scale | Source-check before adding |

This policy and these classifications are a proposed analytical starting point, **not a claim they were recorded before the original Lab 8 work**.

## Recorded calculator inputs — subject to independent verification
Source code: [models/walmart_peer_pe.py](../models/walmart_peer_pe.py). Current input entries: WMT EPS 2.73; COST price 902.60, EPS 18.21; TGT price 157.52, EPS 8.13. Do not mistake numbers currently in code for independently verified primary-source evidence.

For the two provisional peers:
- COST P/E = 902.60 / 18.21 ≈ 49.5662×.
- TGT P/E = 157.52 / 8.13 ≈ 19.3752×.
- Applied to WMT EPS 2.73: approximately $52.89–$135.32 per share, median of the two approximately $94.11.

Removing COST leaves only TGT's approximately $52.89 *reference estimate*; removing TGT leaves COST's approximately $135.32 *reference estimate*. One peer gives no range. These are arithmetic illustrations, **not a validated fair-value range**.

## Evidence needed before finalizing
For WMT and each admitted peer, record (1) 10-K filing URL + exact annual EPS page/note, (2) fiscal year-end, (3) publication date before comparison date, (4) dated share-price source and whether adjusted/unadjusted, (5) share/currency basis, and (6) arithmetic verification. Reject candidates with incompatible or unverified inputs.

## DCF comparison — do not equate reverse DCF with forward fair value
[Reverse DCF](../analysis/reverse_dcf.md) records a $105.83 market-price baseline, WACC 7.0%, terminal growth 2.5%, and approximately 22.3% implied five-year FCFF growth. That is a **market-implied expectation**, not a forward DCF intrinsic value. [FCFF engine](../models/fcff_dcf.py) still contains training assumptions, and [Walmart pro forma](../models/walmart_proforma.py) currently models FCFE. A dated, Walmart-specific pro-forma-driven FCFF valuation is needed for an apples-to-apples comparison.

Possible reasons for disagreement: peers' different growth, membership economics and margins; historical GAAP EPS versus forecast cash flow; market-implied assumptions versus intrinsic forecasts; and dating/enterprise-equity convention differences. Do **not** average estimates mechanically.

## Skeptical challenge — actual lab record required
**Pending:** Paste the actual skeptical-colleague question, source checked, and your *accept / reject / unresolved* judgment. The concern that Costco is not directly comparable is a possible question to investigate, not a substitute for an actual recorded AI review.

## Provisional conditional action
**WATCH—DEFER** until the peer inputs and a sourced forward FCFF DCF support a consistent valuation range. Reconsider an initiation only if supported intrinsic downside/upside and market price offer a stated margin of safety. Monitor operating margins, recurring higher-margin revenue and cash conversion. This provisional view should not be represented as the final committee valuation.

## Submission links
- [Peer calculator](../models/walmart_peer_pe.py)
- [Company research](../walmart-investment-analysis.md)
- [Reverse DCF](../analysis/reverse_dcf.md)
