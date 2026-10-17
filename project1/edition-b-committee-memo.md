# Project 1 — Edition B / Committee memo (working draft)

**Status: NOT READY FOR COMMITTEE.** This document avoids asserting an unsupported valuation range.

## Decision frame
- User: buy-side portfolio manager with **no existing Walmart position**
- Security: Walmart Inc. common equity (NYSE WMT)
- Horizon: provisional five-year forecast FY2027–FY2031, long-run terminal
- Comparison date: September 9, 2026 for historic market-price baseline; refresh and cite before final submission
- Currency: USD; model financial statements in USD **millions**; per-share result USD
- Share convention: 7,972.4 million shares currently entered in `walmart_proforma.py`; **verify diluted vs actual outstanding share count and fiscal basis**
- Exclusions: no trading costs, portfolio taxes or transaction-control premium; minority interest, leases and other EV claims remain unresolved, not assumed zero

## Original baseline
Preserve the original, unchanged **Project 1 Edition A** and the original Brightspace receipt. Do not regenerate or backdate it. **Pending identification of the actual submitted copy.**

## Business thesis and falsification
Walmart's scale, procurement advantages, grocery exposure and developing high-margin businesses may support resilient cash generation. Contrary evidence could be persistent SG&A deleverage, weakening price competitiveness, lower free cash flow after automation capex or share dilution. See [company research](../walmart-investment-analysis.md). All market claims require dated primary support.

## Historical source map and contamination register
See [historical input ledger](historical-evidence-and-normalization.md). The opening balance sheet contains aggregate plug categories. Cash and debt conventions, minority interest, fiscal-year matching and diluted shares must be independently reconciled before using the output.

## Valuation architecture
1. [Five-year Walmart income statement, balance sheet and cash flow](../models/walmart_proforma.py): assumption-driven **FCFE** forecast.
2. [Integrated FCFF model](../models/walmart_project1.py): derives FCFF from the five-year pro forma, discounts at scenario-independent illustrative WACC, adds terminal value, and bridges enterprise to a **provisional** common equity proxy.
3. [Equity multiple](../models/walmart_peer_pe.py): P/E peers; price and annual EPS require historical corroboration.
4. [EV multiple](../project1/peer-enterprise-multiples.md): EV/EBITDA definition and input register; **EV multiple not calculated until primary inputs are verified**.
5. [Assumption register](../analysis/assumption-challenge-register.md) and [Lab 11 sensitivity](../models/walmart_sensitivity.py).

**Do not average** an unverified enterprise bridge and unverified peer multiples. FCFF is forward-looking and affected by financing normalization; P/E reflects current market beliefs about disparate retail models.

## Scenarios and downside
`models/walmart_project1.py` implements a named illustrative **low/downside** case (lower sales growth and margins, higher SG&A burden, higher capex), base case, and high case, with five-year accounting checks. The downside's recommendation effect cannot be asserted until committee valuation bounds and reference market-price evidence are verified. Current parameter ranges are judgments, **not sourced management guidance**.

## Provisional action: WATCH / DEFER
The fund holds zero Walmart shares. **Do not initiate on an unverified value proxy.** Initiate only if a reconciled FCFF enterprise-equity bridge and at least one corroborating, policy-consistent relative valuation support a margin of safety to a dated market price. Do not initiate if sustained cash conversion falls below downside assumptions or competition materially impairs margin durability.

Monitor: quarterly comparable sales, operating margin, advertising/membership mix, capital expenditure, inventory days, interest-bearing debt, and equity-share changes. The committee should revisit the decision when evidence resolves the NCI/lease/debt bridge and changes the accepted intrinsic-value range.

## Deliverable status
- Research and model draft: present
- Synthetic training check: Lab 5 DCF and Lab 7 Asbury P/E present; Lab 9 Asbury three-statement validation pending
- Source and base-year normalization: pending
- Locked AI-off changed-input record: **pending authentic student-generated record**
- Actual partner challenges (credit to challengers): **pending**
- Cold-run: see [GitHub Actions](https://github.com/jmcdonald207/Walmart-repository/actions), verify current SHA and logs
- Final defensible value range: **withheld pending corroborated financial inputs and method reconciliation**
- Three videos/transcripts: excluded from this automation at student request

No part of this memo claims a class interaction or supervised baseline that did not occur.
