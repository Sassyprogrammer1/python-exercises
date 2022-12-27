from datetime import datetime


# # datetime.today().strftime('%Y-%m-%d')
current_date = datetime.now()
# # print(current_date.isoformat())

converted = current_date.strftime('%Y-%m-%d')

# print(converted)
# .strftime('%Y-%m-%dT%H:%M:%S.%f%z')

def dateConversion(date):
    return current_date.isoformat()

results = dateConversion(converted)

print(results)