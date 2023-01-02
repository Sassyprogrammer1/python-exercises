from fastapi import FastAPI
from datetime import datetime,timedelta

app = FastAPI()

current_date = datetime.now()
converted = current_date.strftime('%Y-%m-%d')

@app.post("/api")
def dateConversion(date:str=converted):
    return current_date.isoformat()

@app.get("/today")
def today():
    # To return the date range for the past 24 hours
    base = datetime.now()
    hours = [base - timedelta(hours=x) for x in range(24)]
    return hours
  
@app.get("/lastweek")
def this_week():
    base = datetime.today()
    date_list = [base - timedelta(days=x) for x in range(7)]
    return date_list


@app.get("/thismonth")
def this_month():
    base = datetime.today()
    days = [base + timedelta(days=x-1) for x in range(31)]
    return days






