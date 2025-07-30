from fastapi import FastAPI, Form
from pydantic import BaseModel
import random

app = FastAPI()

# Input data structure
class NameInput(BaseModel):
    keyword: str

# A sample list of AI-themed suffixes
suffixes = ["Bot", "Spark", "AI", "Machine", "Drive", "Core", "Logic"]

@app.post("/generate-name")
def generate_name(data: NameInput):
    keyword = data.keyword.capitalize()
    suffix = random.choice(suffixes)
    return {"generated_name": f"{keyword}{suffix}"}
