from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field, field_validator
from typing import Annotated, Literal
import pandas as pd
import pickle

# ------------------ Constants ------------------

tier_1_cities = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Hyderabad", "Pune"]
tier_2_cities = [
    "Jaipur", "Chandigarh", "Indore", "Lucknow", "Patna", "Ranchi", "Visakhapatnam", "Coimbatore",
    "Bhopal", "Nagpur", "Vadodara", "Surat", "Rajkot", "Jodhpur", "Raipur", "Amritsar", "Varanasi",
    "Agra", "Dehradun", "Mysore", "Jabalpur", "Guwahati", "Thiruvananthapuram", "Ludhiana", "Nashik",
    "Allahabad", "Udaipur", "Aurangabad", "Hubli", "Belgaum", "Salem", "Vijayawada", "Tiruchirappalli",
    "Bhavnagar", "Gwalior", "Dhanbad", "Bareilly", "Aligarh", "Gaya", "Kozhikode", "Warangal",
    "Kolhapur", "Bilaspur", "Jalandhar", "Noida", "Guntur", "Asansol", "Siliguri"
]

@field_validator('city')
@classmethod
def normalize_city(cls,v:str) -> str:
    v=v.strip().title()
    return v
# ------------------ Load Model ------------------

try:
    with open('model (1).pkl', 'rb') as f:

        model = pickle.load(f)
except FileNotFoundError:
    model = None
    print(" Model file not found: 'model(1).pkl'")

# ------------------ FastAPI App ------------------

app = FastAPI()

# ------------------ Pydantic Model ------------------

class UserInput(BaseModel):
    age: Annotated[int, Field(..., gt=0, lt=120, description='Age of the user')]
    weight: Annotated[float, Field(..., gt=0, lt=200, description='Weight in kg')]
    height: Annotated[float, Field(..., gt=0, lt=2.5, description='Height in meters')]
    income_lpa: Annotated[float, Field(..., gt=0, description='Annual income in LPA')]
    smoker: Annotated[bool, Field(..., description='Is the user a smoker?')]
    city: Annotated[str, Field(..., description='City of residence')]
    occupation: Annotated[
        Literal[
            'retired', 'freelancer', 'student', 'government_job',
            'business_owner', 'unemployed', 'private_job'
        ],
        Field(..., description='Occupation of the user')
    ]

    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height ** 2), 2)

    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smoker and self.bmi > 30:
            return "high"
        elif self.smoker or self.bmi > 27:
            return "medium"
        else:
            return "low"

    @computed_field
    @property
    def age_group(self) -> str:
        if self.age < 25:
            return "young"
        elif self.age < 45:
            return "adult"
        elif self.age < 60:
            return "middle_aged"
        return "senior"

    @computed_field
    @property
    def city_tier(self) -> int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        return 3

# ------------------ Prediction Route ------------------
@app.get('/')
def home():
    return {'message':'Insurance Premium Prediction'}


@app.post("/predict")
def predict_premium(data: UserInput):
    if not model:
        raise HTTPException(status_code=500, detail="Model file not found. Please upload model(1).pkl.")

    input_df = pd.DataFrame([{
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }])

    prediction = model.predict(input_df)[0]

    return JSONResponse(
        status_code=200,
        content={"predicted_category": prediction}
    )
