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

## Predictive Analytics Methodologies for TASK 1

### Introduction
This report presents a comparative analysis of two predictive analytics methodologies applied to the dataset for forecasting purposes. The methodologies implemented are the Window Framing Method and the Feature Extraction Method. The performance of various machine learning models was evaluated using the Symmetric Mean Absolute Percentage Error (SMAPE) score.

### Methodologies

#### 1. Window Framing Method
1. **Description**: In this approach, the dataset was split into a window frame of 3 timesteps. This means that the data was segmented into overlapping windows, each containing three consecutive time points.
2. **Test Dataset**: The dataset from the year 01-11-2019 to 01-12-2021 was used as the test dataset.
3. **Models Used**: Various machine learning algorithms were applied to this windowed data to predict future values.

#### 2. Feature Extraction Method
1. **Description**: In this approach, additional features were extracted from the date feature. These features included day, day of the week, month, year, and quarter.
2. **Feature Engineering**: The extracted features were used to train different machine learning models, aiming to improve the predictive performance.
3. **Test Dataset**: The dataset from the year 01-11-2019 to 01-12-2021 was used as the test dataset.
4. **Models Used**: Various machine learning algorithms were applied to these features to predict future values.


### Results
The table below summarizes the SMAPE scores for each model using both methodologies:

| Model             | Window Sliding SMAPE Score | Feature Extraction SMAPE Score |
|-------------------|----------------------------|--------------------------------|
| Decision Tree     | 0.175777226                | 0.136648929                    |
| Random Forest     | 0.155971905                | 0.126089096                    |
| Linear Regression | 0.138594464                | 0.173424928                    |
| Gradient Boosting | 0.139667607                | 0.12958155                     |
| Neural Network    | 6.59628559                 | 2.416215092                    |
| XGBoost           | 0.162519258                | 0.13342507                     |
| LightGBM          | 0.156632604                | 0.120822192                    |
| CatBoost          | 0.150084579                | 0.130839256                    |

### Analysis
- **Decision Tree**: The Feature Extraction Method significantly improved the SMAPE score compared to the Window Sliding Method.
- **Random Forest**: Similar to the Decision Tree, the Feature Extraction Method yielded a better SMAPE score.
- **Linear Regression**: Interestingly, the Window Sliding Method performed better than the Feature Extraction Method for Linear Regression.
- **Gradient Boosting**: The Feature Extraction Method slightly outperformed the Window Sliding Method.
- **Neural Network**: Both methods resulted in high SMAPE scores, but the Feature Extraction Method was notably better.
- **XGBoost**: The Feature Extraction Method provided a better SMAPE score.
- **LightGBM**: This model showed the best performance with the Feature Extraction Method.
- **CatBoost**: The Feature Extraction Method also improved the performance for CatBoost.

 ## Conclusion: The best performing methodology is feature extraction with the LightGBM model




## TASK 2
**Identify exogenous variables for forecasting GRACE time series**<br>
A Markdown guide to run the codes for task 2 is well documented in the colab script `supplemental_material_for_task_2/Task_2_GRACE_ERA5_Exogenous_var.ipynb`. <br><br>
This is documented under the following steps:
- GRACE Data Sorting
- Exogenous Variables Sorting
- Data Merging - GRACE and ERA5
- Data Visualisation
- Multiple Model Trainings
- Model Evaluation
- Identifying Predictive power of Exogenous Variables
- Test: Performance of Model after Removing Non-essential Variables
- Findings <br><br>

Data source for the ERA5 can be found here: https://cds.climate.copernicus.eu/datasets/reanalysis-era5-land-monthly-means?tab=overview

**`NOTE:`** Due to limited compute power and the intensive demand of our best performing model, we worked with numerous batches of 1% of the dataset by changing the random_state values for each model iteration (hence, multiple batches of 1% with shape (805105,14) each). The metric score for all the multiple 1% datasets were highly similar with minimal variances, reinforcing the validity of our findings. The average of the metrics was used in the final output. This ensured the reliability and generalizability of our approach to globally represent the dataset while preventing overdependence on any specific subset of the data. 
