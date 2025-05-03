# Flight Delay Prediction Model

This repository contains a machine learning model designed to predict flight delays based on various factors such as departure and arrival delays, carrier performance, and expected delays. The model utilizes a **Decision Tree Classifier** to categorize flights into different delay buckets and make predictions about departure delay times.

## Features:
- **Data Preprocessing:** Data cleaning and transformation, including categorical encoding, feature selection, and engineering.
- **Modeling:** A Decision Tree Classifier trained to predict flight delays.
- **Evaluation:** Model performance is evaluated using accuracy metrics and visualized through scatter plots and regression plots.
- **Model Saving:** The trained model is saved as a `.bin` file, ensuring it can be reused for testing or deployment.
- **Testing:** The model is tested on new data and evaluated against real-world scenarios.

## Methodology:
The methodology for this flight delay prediction model consists of several key steps:

### 1. Data Preparation:
- **Dataset:** The dataset includes features related to both the departure and arrival delays of flights, such as departure time, weather delays, carrier delays, NAS delays, and more. 
- **Feature Engineering:** Various features were selected and engineered to improve the model's predictive power, including:
    - **Categorical Encoding:** Airports and airlines were encoded using one-hot encoding.
    - **Handling Missing Data:** Missing columns were filled with default values to ensure consistency.
    - **Lagged Features:** Previous flights' delays were used as additional features.

### 2. Feature Selection:
- **Relevant Features:** A subset of features was chosen for training the model, which includes departure delay, expected delays, and categorical features related to airlines and airports.
- **Categorical Features:** Columns like `departure_OP_UNIQUE_CARRIER` and `departure_ORIGIN` were transformed into numerical representations for use in the model.

### 3. Bucketization:
- **Delay Buckets:** The target variable (`departure_DEP_DELAY`) was bucketed into various predefined intervals (e.g., -60 to 30, -30 to 15, etc.) to simplify the prediction into a classification task.
    - Bucket values are assigned based on the delay range.
    - This allowed the model to predict flight delays in terms of relative buckets rather than exact delay times.
  
### 4. Model Selection:
- **Decision Tree Classifier:** The Decision Tree Classifier was chosen because of its simplicity and interpretability. It was trained with the following hyperparameters:
    - `max_depth=11`: To control overfitting and generalize better.
    - Random state set for reproducibility.
  
### 5. Model Evaluation:
- **Accuracy Metrics:** The model's accuracy was evaluated on both training and validation datasets using the `accuracy_score`.
- **Visualization:** Results were visualized using scatter plots and regression plots to compare actual vs predicted delays.
- **Confusion Matrix:** A confusion matrix was also used to understand how well the model is performing on each delay bucket.

### 6. Model Testing:
- **Testing:** The model was tested on new data not seen during training, including flight data from subsequent months.
- **Performance:** Despite challenges in predicting extreme delays (60+ minutes), the model performed adequately for more typical delays.

### 7. Model Deployment:
- **Model Saving:** The trained model was saved to a `.bin` file using Python’s `pickle` module to ensure it could be reused without retraining.
- **Loading for Predictions:** The saved model can be loaded for future predictions on new flight data.

## Project Structure:
- `flight_delay_prediction.ipynb`: Jupyter notebook with the full code for data preprocessing, model training, evaluation, and testing.
- `hire_me_model.bin`: Saved Decision Tree model, ready for future use or deployment.
- `DS_data_input/`: Directory containing the raw input CSV files for flight data.
- `DS_intermediate_data/`: Intermediate data files including processed and feature-engineered data.
- `model_support_functions.py`: Python script with helper functions used for model evaluation, feature engineering, and preprocessing.

## Requirements:
To run the project, install the following Python packages:

```bash
pip install -r requirements.txt
```

## How to Run:

1. **Load the flight data** from the `DS_data_input/` directory.
2. **Perform data preprocessing** and feature engineering using the provided functions in the notebook.
3. **Train the model** with the `DecisionTreeClassifier` on the processed data.
4. **Evaluate the model** using various metrics and visualizations.
5. **Save the trained model** using `pickle` for later use.
6. **Test the model** on new flight data by running the test section of the notebook.

## Results:

The model predicts flight delays within predefined buckets, and while it performs reasonably well, future improvements could be made by:
- Adding more features (e.g., weather data, airport-related data).
- Handling larger datasets with tools like Spark.
- Refining the model to better predict extreme delays.

## Conclusion:

The `DecisionTreeClassifier` performed decently for predicting flight delays in various buckets. Although the model may not predict extreme delays (60+ minutes) as accurately, it performs well within the typical delay ranges. Future improvements could involve:
- Using larger datasets.
- Incorporating more features (e.g., weather data, additional airport-related features).
- Experimenting with other algorithms to boost accuracy.