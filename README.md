# DoD Supply Chain Disruption — Integrated

This version **merges** FPDS with mock BTS Port Performance and OpenSanctions vendor data to demonstrate metadata joins and a sanctions signal.

## How to run
1. Open `notebooks/01_cleaning_fpds.ipynb` and run all cells (installs any missing packages into your active kernel).
2. Then run `02_supply_visuals.ipynb` and `03_dashboard.ipynb`.
3. Replace the mock CSVs in `data/raw/` with your real extracts when ready:
   - `fpds_contracts.csv`
   - `bts_port_performance.csv` (columns: year_month, state, average_turnaround_time, percent_on_time)
   - `opensanctions_vendors.csv` (columns: entity_name, jurisdiction, sanction_type, start_date, end_date)

The processed file is written to `data/processed/fpds_cleaned.csv`.
