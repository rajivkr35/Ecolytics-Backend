from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schema import CarbonInput
from predictor import predict_carbon_footprint

app = FastAPI(title="Carbon Footprint Estimator API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://ecolytics.netlify.app/"],  # or ["http://127.0.0.1:3000"] for stricter
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "✅ Carbon Footprint API is running"}

@app.post("/predict")
def predict(payload: CarbonInput):
    input_data = payload.dict()
    result = predict_carbon_footprint(input_data)  # result in tonnes
    return {
        "predicted_carbon_footprint_kg_per_year": round(result * 1000, 2),
    }

# uvicorn backend.main:app --reload