from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

current_date = datetime.now()

converted = current_date.strftime('%Y-%m-%d')
@app.post("/api")
def dateConversion(date:str=converted):
    return current_date.isoformat()

