# Final Report: Mapping DoD Supply Chain Disruptions (Integrated)

## Introduction
This study examines how supply chain disruptions influence DoD procurement schedules, focusing on vendor concentration and logistics bottlenecks.

## Methods
**Data sources.** FPDS procurement records (contracts, vendors, NAICS, dollars, dates), BTS Port Performance (monthly turnaround, percent on-time by state), and an OpenSanctions vendor list (entity name, jurisdiction, type, dates).  
**Processing.** Column normalization, robust date parsing, numeric coercion for dollars, rule-based vendor normalization, NAICS cleaning and sector extraction.  
**Integration.** We merged BTS metrics to FPDS by `place_of_performance_state` (standardized to USPS codes) and `year_month`. We created a sanctions signal by normalizing vendor names and performing fuzzy matching (RapidFuzz) against the sanctions list with a conservative threshold.

### Metadata Utilization
- **NAICS**: cleaned to 6 digits; sector bucket from first two digits.  
- **Dates**: `action_date` → `year`, `month`, `year_month` for temporal grouping and joins.  
- **Location**: state names mapped to USPS codes; used to join BTS performance metrics.  
- **Vendor identity**: normalized `vendor_group` for grouping; used in fuzzy comparison against sanctions list.

## Results (Illustrative with sample data)
- **Temporal volume:** clear month buckets and skewed value distribution.  
- **Vendor concentration:** a few vendor groups dominate counts.  
- **Logistics context:** states with higher average turnaround times appear alongside heavier contract activity in the sample months.  
- **Sanctions signal:** no sample vendors matched the sanctions list (demonstration only).

## Discussion
Combining FPDS with BTS and sanctions metadata exposes where logistics frictions may coincide with procurement activity and where vendor identity hygiene matters for risk flags.

## Conclusion
The integrated pipeline supports repeatable EDA and can be extended with real BTS/OpenSanctions extracts for richer insights.
