from fastapi import FastAPI
import json

app = FastAPI()


with open('./data.json') as f:
    data = json.load(f)
data_length = len(data)



@app.get("/posts")
def read_posts(page_num: int = 10, page_size: int = 10):
    return data
