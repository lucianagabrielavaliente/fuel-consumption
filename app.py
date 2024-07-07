from fastapi import FastAPI
from pydantic import BaseModel
import joblib

class InputData(BaseModel):
    input1: float
    input2: float

model = joblib.load("LinearModel.pkl")

app = FastAPI()

@app.post("/predict/")
def predit(data: InputData):
    input_values = [[data.input1, data.input2]]

    prediction = model.predict(input_values)[0]

    return {"Prediction": prediction}
