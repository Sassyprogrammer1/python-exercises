from fastapi import FastAPI
import json

app = FastAPI()

with open('./data.json') as f:
    data = json.load(f)