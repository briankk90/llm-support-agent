from fastapi import FastAPI
from src.deployment.model_loader import load_model
from pydantic import BaseModel

app = FastAPI()
model, tokenizer = load_model()

class Query(BaseModel):
    text: str

@app.post("/predict")
async def predict(query: Query):
    inputs = tokenizer(query.text, return_tensors="pt").to("cuda")
    outputs = model.generate(**inputs, max_length=100)
    return {"response": tokenizer.decode(outputs[0], skip_special_tokens=True)}
