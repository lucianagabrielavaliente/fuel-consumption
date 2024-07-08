# Vehicle Fuel Consumption Analysis

## Table of Contents
1. [Aims, Objectives, and Background](#aims-objectives-and-background)
   - [Introduction](#introduction)
   - [Aims and Objectives](#aims-and-objectives)
   - [Steps of the Project](#steps-of-the-project)
   - [Dataset](#dataset)
     - [Data Selection](#data-selection)
     - [Data Limitations](#data-limitations)
     - [Ethics of Data Source](#ethics-of-data-source)
2. [EDA (Exploratory Data Analysis)](#eda-exploratory-data-analysis)
   - [Preprocessing & Feature Engineering](#preprocessing--feature-engineering)
   - [Exploratory Analysis](#exploratory-analysis)
     - [Engine Size Distribution](#engine-size-distribution)
     - [Correlation Analysis](#correlation-analysis)
   - [Conclusions from EDA](#conclusions-from-eda)
3. [Model Training](#model-training)
4. [Dependencies](#dependencies)
5. [Usage](#usage)

---

## 1. Aims, Objectives, and Background

### Introduction
This project aims to analyze the fuel consumption patterns of vehicles manufactured in the year 2000 using the Vehicle Attributes and Emissions Dataset. The analysis focuses on understanding the factors influencing fuel efficiency and their implications for environmental sustainability and transportation policies.

### Aims and Objectives
- Conduct exploratory data analysis (EDA) to understand the characteristics of the dataset.
- Preprocess the data and perform feature engineering to prepare it for modeling.
- Train a regression model to predict fuel consumption based on vehicle attributes.
- Provide insights into the relationship between engine size, cylinders, and fuel consumption.
- Create an API using FastAPI for making real-time predictions based on the trained model.

### Steps of the Project
1. **Data acquisition and initial exploration.**
2. **Data preprocessing and feature engineering.**
3. **Exploratory data analysis (EDA) to derive insights.**
4. **Model training and evaluation.**
5. **Deployment of the model as a FastAPI application.**

### Dataset

#### Data Selection
The dataset used in this project is the "Vehicle Attributes and Emissions Dataset," which contains comprehensive information on vehicles manufactured in the year 2000, including make, model, vehicle class, engine size, cylinders, transmission type, fuel type, fuel consumption, and CO2 emissions.

#### Data Limitations
- Limited to vehicles manufactured in the year 2000.
- The dataset may not represent the latest technological advancements or trends in vehicle fuel efficiency.

#### Ethics of Data Source
- The dataset is sourced from Kaggle and is used strictly for educational and research purposes.

---

## 2. EDA (Exploratory Data Analysis)

### Preprocessing & Feature Engineering
- Removed unnecessary columns such as "Year" and corrected column names.
- Addressed missing values and handled duplicates in the dataset.

### Exploratory Analysis

#### Engine Size Distribution
- Visualized the distribution of engine sizes using a histogram.
  - **Sample Output**: The histogram of 'Engine size' shows a peak around larger engine sizes, indicating variability in vehicle types.

#### Correlation Analysis
- Investigated correlations among variables using a correlation matrix.
  - **Sample Output**: The correlation matrix highlights a strong positive correlation between 'Engine size' (0.858) and 'Cylinders' (0.826) with 'Fuel consumption' (1.000), suggesting these variables influence fuel efficiency.

### Conclusions from EDA
Based on the exploratory data analysis:
- Engine size and cylinders exhibit strong correlations with fuel consumption, indicating that larger engines and more cylinders generally result in higher fuel consumption.

---

## 3. Model Training

- Trained a regression model using the features "Engine size" and "Cylinders" to predict "Fuel consumption."
- Achieved a mean absolute error (MAE) of 1.31, which is considered satisfactory given the dataset's variability.
- Saved the trained model using joblib for future predictions.

---

## 4. Dependencies
Ensure you have the following dependencies installed to run the project:

- Python 3.12.4 
- pandas
. numpy
- scikit-learn
- FastAPI
- uvicorn
- joblib


```bash
pip install pandas numpy scikit-learn fastapi uvicorn joblib
```

## 5. Usage

### Using the Trained Model and API

#### Using the Trained Model

To use the trained regression model for predicting fuel consumption:

```python
import joblib

# Load the trained model
model = joblib.load("LinearModel.pkl")

# Example input values (Engine size and Cylinders)
input_values = [[2.5, 4]]

# Predict fuel consumption
prediction = model.predict(input_values)[0]
print(f"Predicted Fuel Consumption: {prediction} liters/100km")
```