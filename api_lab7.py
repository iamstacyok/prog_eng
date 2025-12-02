from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel

class Item(BaseModel):
    prompt: str
    tokens: int = 300
    temperature: float = 0.7

app = FastAPI()
generator = pipeline("text-generation", model="ai-forever/rugpt3small_based_on_gpt2")

@app.get('/')
def root():
    return {"message": "privet mir and lab7"}

@app.get("/generate")
def generate(item: Item):
    result = generator(
        item.prompt,
        max_new_tokens = item.tokens,
        temperature=item.temperature)
    return result[0]["generated_text"]