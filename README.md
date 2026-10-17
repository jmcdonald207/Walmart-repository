# Walmart valuation coursework — FIN 43900

This is a collection of student research, training calculators, and work-in-progress Walmart valuation components. **It is not yet one validated investment application.** Files use differing dates and valuation bases; read limitations before comparing results.

## Run (Python standard library)
- **Entire collection plus integrated Walmart analysis:** `python walmart_all_models.py`
- **Standalone integrated Project 1 five-year FCFF/scenario/validation:** `python models/walmart_project1.py`
- Lab 5 training FCFF calculator: `python models/fcff_dcf.py`
- Lab 7 Asbury training case: `python references/abg_lab07_calculator.py`
- Walmart five-year FCFE pro forma: `python models/walmart_proforma.py`
- Lab 11 sensitivity reruns on Walmart pro forma: `python models/walmart_sensitivity.py`
- Walmart peer P/E candidate calculator: `python models/walmart_peer_pe.py`

## Project 1 finance decision and evidence
- [Edition B committee memo — working draft](project1/edition-b-committee-memo.md)
- [Historical source/normalization ledger](project1/historical-evidence-and-normalization.md)
- [Peer enterprise multiple definitions and input gaps](project1/peer-enterprise-multiples.md)
- [Validation and AI-use records](project1/validation-and-ai-use.md)

## Analysis and course notes
- [Walmart research](walmart-investment-analysis.md)
- [Reverse DCF notes](analysis/reverse_dcf.md)
- [Lab 8 triangulation working draft](labs/lab-08-valuation-triangulation.md)
- [Pro-forma assumptions and challenges](analysis/assumption-challenge-register.md)
- [Earlier sensitivity outputs](analysis/what_if_sensitivity.md)
- [Lab 12 review preparation](labs/lab-12-final-review.md)

## Known open items
1. Source-check same-date peer prices and contemporaneous annual EPS; resolve peer policy before finalizing.
2. Reconcile FY2026 opening balances and normalize one-time/basis-change items from SEC filings.
3. Build Walmart operating pro-forma-derived **FCFF**, discount at **WACC**, and reconcile enterprise to equity.
4. Validate training examples, check cash flows independently and keep error-producing tests.
5. Record **actual** partner questions, locked predictions, sources and class review results.
6. Add robust causal downside cases and a defensible final valuation range and conditional committee action.

Individual course requirements and historical frozen submissions must remain independently evidenced. No investment advice.

**Important:** The combined script is a snapshot; source model changes require embedding an updated copy. GitHub Actions runs the compiled standalone model and the combined model. Training examples are NOT Walmart fair value. Historical input verification, EV peer prices/claims and a committee valuation range remain uncompleted.
