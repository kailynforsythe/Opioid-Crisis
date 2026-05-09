## Opioid-Crisis
### Overview
This project analyzes opioid overdose and misuse data to understand who is most at risk and where prevention efforts should be focused. It uses national datasets on overdoses, drug use, treatment history, naloxone distribution, and arrest records to identify patterns associated with opioid misuse and overdose deaths.
The goal is to combine statistical analysis and geospatial mapping to determine key risk factors and geographic hotspots, with a focus on applying findings to Montgomery County, Maryland.

### Research Questions
This project explores:
- What type of opioids are people dying from the most and how are they obtained?
- What are the markers of an at-risk person to fall into opioid-use disorder?
- What are common circumstances surrounding overdose deaths?
- Does the distribution of naloxone have an impact on opioid deaths?
- Where is the most illegal possession of opioids in Montgomery County?
- How can we reform treatment facilities?

### Datasets Used:
- SUDORS: Overdose death data and circumstances (2020–2024)
- NSDUH: National survey on drug use and risk factors (2021–2024)
- CDC Naloxone Data: Naloxone distribution rates across states
- DataMontgomery: Opioid-related arrest locations in Montgomery County

### Methods
This project uses Python for all analysis, including:
- Data cleaning and filtering of large survey datasets
- Exploratory Data Analysis (EDA) to identify trends and distributions
- Pearson correlation tests to examine relationships between variables
- Chi-square tests to identify significant risk factors for opioid misuse
- OLS regression to analyze overdose circumstances
- GIS mapping to visualize geographic hotspots of opioid-related arrests

### Project Structure
- data: Raw and cleaned datasets
- ingestion: Data loading and cleaning scripts
- eda: Exploratory data analysis and visualizations
- analysis: Statistical models and tests
reports: Final report and presentation materials

### Goal of the Project
The main objective is to identify high-risk populations and geographic areas where intervention efforts would have the greatest impact, using insights found with multiple national and local sources.
