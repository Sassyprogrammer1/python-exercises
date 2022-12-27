from datetime import datetime

current_date = datetime.now()

converted = current_date.strftime('%Y-%m-%d')

def dateConversion(date):
    return current_date.isoformat()

results = dateConversion(converted)
print(results)