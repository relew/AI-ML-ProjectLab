# PJME Energy Consumption Forecasting

This project aims to forecast the energy consumption (PJME_MW) using historical time series data with feature engineering, outlier removal, and machine learning models. We utilize an XGBoost regressor model to predict energy consumption and evaluate its performance using Root Mean Squared Error (RMSE).

## Overview

The project processes and analyzes hourly energy consumption data (`PJME_hourly.csv`) from the PJM electricity grid. The main steps include:

1. **Data Loading & Preprocessing**: 
   - Load the energy consumption data.
   - Visualize energy consumption trends.
   - Split the data into training and test sets based on a specific date.

2. **Feature Engineering**: 
   - Create additional time-based features like `hour`, `dayofweek`, `month`, `year`, etc.
   - Generate a holiday feature using the US Federal Holidays.

3. **Outlier Removal**: 
   - Apply IQR-based filtering to remove outliers from the daily average consumption.

4. **Modeling**: 
   - Train an XGBoost regressor model to predict energy consumption.
   - Visualize feature importance and evaluate the model performance on the test set.

5. **Forecasting**: 
   - Use the trained model to forecast future energy consumption.
   - Calculate errors between predicted and actual values.

## How to Run

1. Clone the repository and navigate to the project directory.
2. Place the `PJME_hourly.csv` file in the `Data/` folder.
3. Run the Python script to train the model, visualize the results, and forecast energy consumption.

```bash
python energy_forecasting.py
```

## Results

The model predicts energy consumption within a reasonable range, and the performance is evaluated using RMSE. The visualizations help in understanding the actual vs. predicted consumption, and feature importance provides insights into the model.

## Future Improvements

- Experiment with other machine learning algorithms like Random Forest or ARIMA.
- Include additional features such as weather data or external factors affecting energy consumption.
- Apply cross-validation for better model performance evaluation.