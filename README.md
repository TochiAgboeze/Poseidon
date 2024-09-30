# Team Poseidon

## TASK 1
## Groundwater Level Prediction Project

This project aims to predict groundwater levels using date features and the LightGBM model. The source code is provided as a Jupyter Notebook file, divided into the following sections:

## Sections of the Notebook:
1. **Data Cleaning Process**:
    - This section contains the code to clean the datasets and prepare them for downstream analysis.
      
2. **Feature Extraction and LightGBM Model**: 
   - This section performs datetime feature extraction, then trains and tests a LightGBM model using the cleaned data.

3. **Forecast for 2022-2024 Feb**: 
   - This section extracts features from the datasets, trains the model, and makes forecasts for submission.

4. **Train and Make Predictions for Specific Geographic Locations**: 
   - This section contains code to train and make forecasts for any specific geographic location.

## How to Run the Source Code

- Download the `ehyd_messstellen_all_gw.zip` file (groundwater data) at https://ehyd.gv.at<br>
- Unzip the downloaded file and copy the path to the folder named `Grundwasserstand-Monatsmittel`
- Open the jupyter notebook source code
- Replace the path in the variable name `directory` on the first cell of the source code to the path of the folder named `Grundwasserstand-Monatsmittel`
- Run all the cells in the **Data Cleaning Process** section.
- Run all the cells in the **Feature Extraction and LightGBM Model** section. This will return the SMAPE score of the model on the entire dataset, indicating the model's performance.
- Run all the cells in the **Forecast for 2022-2024 Feb** section without making any changes. This will return and save a spreadsheet containing IDs and forecasts from 2022-2024 for the sites in the uploaded folder.

## How to Train and Make Forecasts for a Specific Geographic Location

1. **Adjust Variables**:
   - In the first cell of this section, adjust the following three variables:
     - `file_path`: Set this to the file path of the **raw/uncleaned dataset** from the `Grundwasserstand-Monatsmittel folder` containing the specific location.
     - `start_date`: Set this to the start date for forecasts in the format `YYYY-MM-DD`.
     - `end_date`: Set this to the last forecast date in the format `YYYY-MM-DD`.

2. **Run the Cells**:
   - After adjusting the variables, run all the other cells in this section. Running the last cell will return and save a spreadsheet of forecasted groundwater levels between the specified start and end dates. <br><br>

**`NOTE:`** During model Exploration for task 1, we initially experimented with linear regression, which achieved a SMAPE score of 0.13. However, we chose the LightGBM model which provided slightly better performance (0.12).<br><br>

## TASK 2
**Identify exogenous variables for forecasting GRACE time series**<br>
A Markdown guide to run the codes for task 2 is well documented in the colab script `supplemental_material_for_task_2/Task2_GRACE_ERA5_Exogenous_var.ipynb`. <br><br>
This is documented under the following steps:
- GRACE Data Sorting
- Exogenous Variables Sorting
- Data Merging - GRACE and ERA5
- Data Visualisation
- Multiple Model Trainings
- Model Evaluation
- Identifying Predictive power of Exogenous Variables
- Test: Performance of Model after removing non-essential variables
- Findings <br><br>
**`NOTE:`** Due to the large size of the dataset, we split the data into 5 different globally representative batches (1% each). This ensured the reliability and generalizability of our approach, preventing overdependence on any specific subset of the data. Each batch yielded similar outputs, reinforcing the validity of our findings.
