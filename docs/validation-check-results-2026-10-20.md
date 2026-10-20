# Walmart Project 1 — Reproducible validation check results

**Check date:** 2026-10-20. **Repository:** [Original Walmart repository](https://github.com/jmcdonald207/Walmart-repository).  
**Scope:** Independent arithmetic and SEC-source comparisons performed in this review, plus clearly identified *previously logged* program checks. This document is an AI-assisted check report. It is **not** a student-authored AI-off Locked Changed-Input Record, nor proof of a new end-to-end source-code execution.

## 1. Known-answer arithmetic check — PASS for independently recomputed bridge

Training DCF output in the saved runner: enterprise value **$1,624.8685 million**, cash **$50 million**, debt **$300 million**, 50 million diluted shares.

- Recomputed equity = 1,624.8685 + 50 - 300 = **$1,374.8685 million**.
- Recomputed share value = 1,374.8685 / 50 = **$27.49737**, rounds to **$27.4974**.
- **Result: PASS** for the final training-case EV-to-equity and per-share arithmetic. This checks consistency with the printed training case, **not independent derivation of all five FCFF forecasts**.
- Earlier runner also prints Asbury Automotive training P/E minimum **$215.81**, midpoint **$231.00**, maximum **$246.18**. These are previously logged outcomes; the corresponding weekly starter answer key has **not** been independently retrieved in this review.

## 2. Independent primary-source definition/input checks — PASS for listed balance-sheet entries

**Primary source:** [SEC XBRL balance sheet, Walmart Jan. 31, 2026 column](https://www.sec.gov/Archives/edgar/data/104169/000010416926000102/R4.htm), amounts in USD millions. This SEC filing presents the Jan. 31, 2026 comparative column; the current-year column is Apr. 30, 2026. The comparisons below deliberately use the **Jan. 31, 2026** column. The FY2026 annual report is the corresponding historical source.

| Jan. 31, 2026 source definition | SEC-reported | Model / derived | Numerical result |
|---|---:|---:|---|
| Cash and cash equivalents | 10,727 | 10,727 | PASS |
| Inventories | 58,851 | 58,851 | PASS |
| PP&E, net | 136,083 | 136,083 | PASS |
| Total assets | 284,668 | 284,668 | PASS |
| Accounts payable | 63,061 | 63,061 (model key: `floor_plan`) | PASS value; label misleading |
| Short-term borrowings | 6,596 | 6,596 (model key: `revolver`) | PASS value; financing definition requires care |
| Current long-term debt + long-term debt | 3,542 + 34,624 | 38,166 | PASS |
| Total funded borrowings | 6,596 + 3,542 + 34,624 | 44,762 | PASS |
| Total equity incl. nonredeemable NCI | 105,887 | 105,887 | PASS arithmetic; not entirely common equity |
| Nonredeemable NCI | 6,270 | not separated in model equity | UNRESOLVED common-equity valuation |
| Redeemable NCI | 293 | included in aggregate `other_liab` | UNRESOLVED common-equity valuation |
| Finance lease obligations | 856 + 5,905 | 6,761 | PASS arithmetic; EV treatment unresolved |
| Operating lease obligations | 1,631 + 13,941 | 15,572 | PASS arithmetic; EV/FCFF policy unresolved |

**Aggregate recomputation (independent arithmetic):**
- Other assets = receivables 11,172 + prepaid/other 4,124 + operating lease ROU 14,750 + finance lease ROU 6,123 + goodwill 28,735 + other long-term 14,103 = **79,007**; matches model opening aggregate.
- Other liabilities/temporary equity grouped by the model = 31,187 + 596 + 1,631 + 856 + 13,941 + 5,905 + 16,549 + 293 = **70,958**; matches its model aggregate **but mixes redeemable NCI with ordinary liabilities**.
- Opening model accounting identity: assets = 10,727 + 58,851 + 136,083 + 79,007 = **284,668**; liabilities, temporary-equity aggregate, and total equity = 63,061 + 38,166 + 6,596 + 70,958 + 105,887 = **284,668**. **Gap = 0**.

**Meaning:** These numerical source checks support the stated historical opening amounts but **do not** independently validate unusual-item normalization, later-period filing refresh, diluted share denominator, lease treatment in future FCFF, or all forecast drivers.

## 3. DCF output bridge — PASS arithmetic; common-equity definition NOT CLEARED

Saved integrated DCF *base-case* output: PV explicit FCFF **$55,988.88 million** + PV terminal **$243,792.02 million** = enterprise value **$299,780.90 million**. Applying the code's simplified bridge:

- Provisional equity proxy = 299,780.90 + 10,727 - 44,762 = **$265,745.90 million**.
- Dividing by entered 7,972.4 million shares yields **$33.333237…**, rounded **$33.33/share**.
- **PASS** for numerical equality between recorded outputs and the simplified formula.
- **QUALIFY** as a common-equity valuation: nonredeemable/redeemable noncontrolling interests, finance and operating leases, cash availability, share-basis consistency and other claims remain unresolved. Do not arbitrarily subtract all leases without checking EV/FCFF and peer convention; do not call the model's low/base/high endpoints a defensible fair-value interval.

## 4. Previously executed pro-forma and robustness checks — REPORTED, not freshly executed here

Prior successful program execution is preserved at [GitHub Actions run 39178101348 in the submission repository](https://github.com/jmcdonald207/Walmart-Project-1-Submission/actions/runs/39178101348) and [its visible output](https://github.com/jmcdonald207/Walmart-Project-1-Submission/blob/main/outputs/visible-output.md).

Existing scripts include:
- `models/walmart_proforma.py`: annual balance-sheet and cash reconciliation checks; data definitions and the historical opening model are separate from economic forecast validation.
- `models/walmart_project1.py` `verify()`: discount-rate monotonicity, terminal-growth monotonicity, invalid terminal-growth boundary (equal WACC/g fails), deliberately broken $10 million balance-sheet gap failure test, and five annual cash/balance ties.
- `models/walmart_sensitivity.py`: gross margin and SG&A changed-input cases and restored-base checks.

**Reproduction commands** (run in the repository root with Python 3):
```powershell
python models/fcff_dcf.py
python models/walmart_proforma.py
python models/walmart_project1.py
python models/walmart_sensitivity.py
```

**Evidence distinction:** The logged successful run exists, but I have not independently executed the exact current remote source in a fresh interpreter in this review. A final cold-run record should identify the target **repository commit SHA**, runtime, command, timestamp, actual output, and exit status.

## 5. Peer policy / multiple-definition check — INCOMPLETE

`models/walmart_peer_pe.py` calculates P/E using peer price and diluted EPS and prints dates. `project1/peer-enterprise-multiples.md` defines a policy for peer comparability, lease/noncontrolling interest treatment and matching EV/EBITDA bases. A documented, independently confirmed same-date EV/EBITDA comparison and final adjustments are **not** established by this report. Historical P/E observations must be checked against dated prices and relevant EPS periods; peer comparability is an analyst decision.

## 6. AI-generated-output disposition — QUALIFIED by independently checked source definitions

**AI-assisted model output under review:** Simplified claim that `EV + cash - borrowings` yields value attributable to common Walmart shareholders.

**Independent evidence checked in this review:** SEC Jan. 31, 2026 reported **$6,270 million nonredeemable NCI**, **$293 million redeemable NCI**, **$6,761 million finance lease obligations**, and **$15,572 million operating lease obligations**, as detailed above.

**Disposition: QUALIFIED.** The arithmetic itself matches, but the simplified bridge does not establish a final value attributable to common shareholders. The model flags missing adjustments; final EV/FCFF/NCI and lease consistency must be decided before using its price as investable intrinsic value. This is an AI-assisted independent evidence comparison, **not** a claim that the student personally performed the source check.

## 7. Locked Changed-Input Record — NOT PERFORMED

A genuine AI-off, **human-authored prediction must be written and committed BEFORE a new changed-input test**, including old/new input and units, expected numerical direction and decision effect, commit timestamp/SHA. Afterwards the student preserves before/after output, actual direction/decision consequence and any failure or unchanged-decision explanation. Prior automated sensitivities and this AI-assisted writeup **cannot** be substituted for the required precommit or retroactively claimed to be one.

## Validation conclusion

**Confirmed during this AI-assisted review:** Selected SEC historical source figures and aggregates, source-reported debt/leases/NCI definitions, the training DCF equity bridge, and the logged integrated DCF simplified bridge arithmetic.

**Supported by earlier logged program evidence, not rerun here:** Programmed statement articulation, monotonicity, invalid-boundary and deliberately broken-balance tests.

**Outstanding for a fully defensible investment conclusion:** authentic AI-off precommit/change test, normalized source base and share conventions, economically consistent NCI/lease/common-equity bridge, independently sourced peer enterprise multiples, WACC justification and final matching cold-run log. No unsupported “PASS” or fabricated student work is asserted.
