from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

current_date = datetime.now()

converted = current_date.strftime('%Y-%m-%d')
@app.post("/api")
def dateConversion(date:str=converted):
    return current_date.isoformat()

@app.get("/today")
def today():
    # To return the date range for the past 24 hours
    return 

@app.get("/lastweek")
def this_week():
    # To return the date range for the past 7 days
    return

@app.get("/thismonth")
def this_month():
    # To return the date range for the current month from the beginnng of it,ie from 1st January to 2nd
    return 


