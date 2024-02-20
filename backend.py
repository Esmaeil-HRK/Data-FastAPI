from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class InputData(BaseModel):
    name: str
    email: str
    phone: str
    transfer_limit: float
    nid: int

class OutputData(BaseModel):
    country: str = "Placeholder Country"
    type: str = "Placeholder Type"
    gender: str = "Placeholder Gender"

@app.post("/process-data/", response_model=OutputData)
async def process_data(input_data: InputData):
    # Classify type based on name
    type_ = classify_type(input_data.name)
    
    # Classify gender based on NID, type, or name
    gender = classify_gender(input_data.name, input_data.nid, type_)
    
    country = determine_country(input_data.phone)
    
    birth_year = classify_birth_year(input_data.nid)

    anomaly_detected = False
    # Classify the transfer limit into financial classes
    financial_class = classify_transfer_limit(input_data.transfer_limit)
    # Detect anomalies in the input data
    if check_for_anomalies(input_data):
        anomaly_detected = True

    return OutputData(
        gender=gender,
        type=type_,
        birth_year=birth_year,
        country=country,
        class_=financial_class,
        anomaly = anomaly_detected,
    )
