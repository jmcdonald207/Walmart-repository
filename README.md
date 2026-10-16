# Walmart valuation coursework — FIN 43900

This is a collection of student research, training calculators, and work-in-progress Walmart valuation components. **It is not yet one validated investment application.** Files use differing dates and valuation bases; read limitations before comparing results.

## Run (Python standard library)
- Lab 5 training FCFF calculator: `python models/fcff_dcf.py`
- Lab 7 Asbury training case: `python references/abg_lab07_calculator.py`
- Walmart five-year FCFE pro forma: `python models/walmart_proforma.py`
- Lab 11 sensitivity reruns on Walmart pro forma: `python models/walmart_sensitivity.py`
- Walmart peer P/E candidate calculator: `python models/walmart_peer_pe.py`

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
