from fastapi import FastAPI
import json

app = FastAPI()


with open('./data.json') as f:
    data = json.load(f)
data_length = len(data)



@app.get("/posts")
def read_posts():
    return data

@app.get("https://jsonplaceholder.typicode.com/posts")
def get_data():
    return
