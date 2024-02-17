from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class InputData(BaseModel):
    name: str
    email: str
    phone: str
    transfer_limit: float
    nid: str

class OutputData(BaseModel):
    country: str = "Placeholder Country"
    birth_year: int = 1980
    anomaly: bool = False
    class_: str = "Placeholder Class"
    type: str = "Placeholder Type"
    gender: str = "Placeholder Gender"

@app.post("/process-data/", response_model=OutputData)
async def process_data(input_data: InputData):
    # Placeholder for logic to enrich and process the data
    
    return OutputData()  # Returning default values for now

