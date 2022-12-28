from fastapi import FastAPI
import json

app = FastAPI()

with open('./data.json') as f:
    data = json.load(f)
data_length = len(data)

@app.get("/posts")
def read_posts():
    return data
