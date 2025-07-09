import joblib
import pandas as pd
import os

# Load trained model
model = joblib.load(os.path.join("model", "carbon_model.pkl"))

# Load the column structure used during training
TRAIN_COLUMNS = list(pd.read_csv("cleaned_carbon_footprint_data.csv").drop("annual_carbon_footprint_tonnes", axis=1).columns)

def preprocess_input(data: dict) -> pd.DataFrame:
    df = pd.DataFrame([data])
    df_encoded = pd.get_dummies(df)

    # Add missing columns from training, fill with 0
    for col in TRAIN_COLUMNS:
        if col not in df_encoded:
            df_encoded[col] = 0

    # Ensure column order matches training
    df_encoded = df_encoded[TRAIN_COLUMNS]

    return df_encoded

def predict_carbon_footprint(input_data: dict) -> float:
    clean_data = preprocess_input(input_data)
    prediction = model.predict(clean_data)[0]
    return round(prediction, 3)