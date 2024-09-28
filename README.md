# Team Poseidon
# Groundwater Level Prediction Project

This project aims to predict groundwater levels using date features and the LightGBM model. The source code is provided as a Jupyter Notebook file, divided into the following sections:

## TASK 1

1. **Data Cleaning Process**:<br>
   - Download the `ehyd_messstellen_all_gw.zip` file (groundwater data) at https://ehyd.gv.at<br>
   - Unzip and rename the Grundwasserstand-Monatsmittel folder which contains 'Monthly Average Groundwater Level' data. To excecute this on the CLI, use:<br><br> `mv Grundwasserstand-Monatsmittel Monthly_Average_Groundwater_Level`<br><br>
   - Inside the same directory where the Monthly Average Groundwater Level directory is located, make two new directories    (487_sampling_points, 487_sampling_points_cleaned) using the following commands on the CLI: <br><br>`mkdir 487_sampling_points`<br><br>`mkdir 487_sampling_points_cleaned`<br><br>
**NB: Make sure the following are located within the directory:**
<br>`Monthly_Average_Groundwater_Level` - directory<br>`rename.py`<br>`clean_487.py`<br>`move.sh`<br>`487_sampling_points` - directory<br>`487_sampling_points_cleaned` - directory <br>`sampling_points_ids.txt`- This contains the IDs of the 487 sampling points<br>

   - Rename the data for each sampling point by running 'rename.py' : <br><br>`python rename.py`<br><br>
   - To filter the data for only the 487 sampling points, run 'move.sh': <br>`bash move.sh` or `./move.sh` - The output will be moved to the **`487_sampling_points`** directory.<br><br>
   - Clean the 487 sampling points' data to get the metadata (months and groundwater levels) by running 'clean_487.py':<br>`python clean_487.py` - The output will be moved to the **`487_sampling_points_cleaned`** directory.

## Sections of the Notebook
2. **Feature Extraction and LightGBM Model**: 
   - This section performs datetime feature extraction, then trains and tests a LightGBM model using the cleaned data.

3. **Forecast for 2022-2024 Feb**: 
   - This section extracts features from the datasets, trains the model, and makes forecasts for submission.

4. **Train and Make Predictions for Specific Geographic Locations**: 
   - This section contains code to train and make forecasts for any specific geographic location.

## How to Run the Source Code

1. **Set the Folder Path**:
   - Change the variable named `folder_path` to the path containing the CSV files you want to train and make predictions on. Note that this folder should only contain the 487 samples for which predictions are to be made.

2. **Run the Data Cleaning and Feature Extraction Sections**:
   - Run all the cells in the **Data Cleaning Process** section.
   - Run all the cells in the **Feature Extraction and LightGBM Model** section. This will return the SMAPE score of the model on the entire dataset, indicating the model's performance.

3. **Make Forecasts for 2022-2024 Feb**:
   - Run all the cells in the **Forecast for 2022-2024 Feb** section without making any changes. This will return and save a spreadsheet containing IDs and forecasts from 2022-2024 for the sites in the uploaded folder.

## How to Train and Make Forecasts for a Specific Geographic Location

1. **Adjust Variables**:
   - In the first cell of this section, adjust the following three variables:
     - `file_path`: Set this to the file path of the raw dataset containing the specific location.
     - `start_date`: Set this to the start date for forecasts in the format `YYYY-MM-DD`.
     - `end_date`: Set this to the last forecast date in the format `YYYY-MM-DD`.

2. **Run the Cells**:
   - After adjusting the variables, run all the other cells in this section. Running the last cell will return and save a spreadsheet of forecasted groundwater levels between the specified start and end dates.
