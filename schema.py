from pydantic import BaseModel

class CarbonInput(BaseModel):
    private_km_per_week: float
    fuel_type: str
    public_km_per_week: float
    electricity_per_month_kwh: float
    uses_renewable_energy: bool
    meat_frequency: str
    dairy_frequency: str
    short_flights_per_year: int
    long_flights_per_year: int
    clothing_shopping_freq: str
    electronics_shopping_freq: str
    recycles_regularly: bool
    waste_kg_per_week: float
    household_size: int
    home_type: str
