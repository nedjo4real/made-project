# Project Plan: Factors Influencing Income Levels and Educational Attainment in the Americas

## Overview
This project analyzes the relationship between education levels and income across the Americas. By integrating demographic data from the American Citizen Income dataset (Kaggle) with country-level education statistics (World Bank), we aim to identify trends and predictors for income levels based on education and related factors. The project will culminate in a cleaned and integrated dataset for further exploratory and statistical analysis.

---

## Goals
1. Extract income and education data from the respective sources.
2. Clean and preprocess both datasets to handle missing values and inconsistencies.
3. Integrate datasets by aligning education statistics with demographic and income information.
4. Transform the data to create new features (e.g., education categories, average literacy rates by group).
5. Store the cleaned and combined dataset for analysis.
6. Conduct an exploratory analysis to visualize and model the relationship between education and income levels.

---

## Dataset Description

### Dataset 1: American Citizen Income Dataset
* Metadata URL: [Kaggle: American Citizen Income](https://www.kaggle.com/datasets/amirhosseinmirzaie/americancitizenincome/data?select=income.csv)  
* Data URL: https://www.kaggle.com/datasets/amirhosseinmirzaie/americancitizenincome/data?select=income.csv  
* Data Type: CSV
* Description: Contains information on income levels, demographics (e.g., age, gender, state), and other related features.

### Dataset 2: World Bank Education Statistics
* Metadata URL: [World Bank Education Data](https://data.worldbank.org/indicator/SE.ADT.LITR.ZS) 
* Data URL: https://api.worldbank.org/v2/en/indicator/SE.ADT.LITR.ZS?downloadformat=excel
* Data Type: Excel
* Description: Provides country-level indicators on literacy rates, average years of schooling, and other education metrics.

---

## Work Packages

### WP 1: Data Exploration
- **Goal:** Explore the datasets to understand their structure and identify relevant features.
- **Tasks:**
  1. Load and inspect both datasets for missing or invalid values.
  2. Identify features needed for integration (e.g., state and country mappings).
  3. Analyze potential inconsistencies in demographic and education data.

### WP 2: Data Cleaning
- **Goal:** Handle missing values and inconsistencies in both datasets.
- **Tasks:**
  1. Impute missing values using appropriate techniques (e.g., mean, median, or interpolation).
  2. Standardize country and state names to enable dataset merging.
  3. Normalize education statistics to align with demographic information.

### WP 3: Data Integration
- **Goal:** Combine the two datasets into a unified dataset.
- **Tasks:**
  1. Link the datasets using country or state-level information.
  2. Aggregate education data (e.g., calculate average literacy rates for demographic groups).
  3. Ensure all features are aligned for analysis.

### WP 4: Data Transformation
- **Goal:** Create new features for richer analysis.
- **Tasks:**
  1. Derive education categories (e.g., primary, secondary, tertiary).
  2. Calculate demographic-based statistics (e.g., income brackets by education level).
  3. Standardize features for statistical modeling.

### WP 5: Data Storage
- **Goal:** Save the processed dataset for future analysis.
- **Tasks:**
  1. Store the combined and cleaned dataset as a CSV file in the `/data` directory.
  2. Ensure proper documentation of the dataset schema.

### WP 6: Data Analysis 
- **Goal:** Perform exploratory and statistical analysis to validate the dataset.
- **Tasks:**
  1. Visualize income levels and education distributions.
  2. Perform regression or classification to predict income based on education and demographics.
  3. Generate heatmaps and bar charts to identify key trends.

---

## Work Packages with Issues

### Linked Issues:
1. [Data Exploration](https://github.com/nedjo4real/made-project/issues/1)
2. [Data Cleaning](https://github.com/nedjo4real/made-project/issues/2)
3. [Data Integration](https://github.com/nedjo4real/made-project/issues/3)
4. [Data Transformation](https://github.com/nedjo4real/made-project/issues/4)
5. [Data Storage](https://github.com/nedjo4real/made-project/issues/5)
6. [Data Analysis](https://github.com/nedjo4real/made-project/issues/6)

---


