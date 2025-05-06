import json
import random

def generate_dialogue():
    queries = ["How do I return a product?", "My order is delayed, help!"]
    responses = ["Please visit our returns page...", "Let me check your order status..."]
    return {"query": random.choice(queries), "response": random.choice(responses)}

with open("data/raw/dialogues.jsonl", "w") as f:
    for _ in range(1000):
        f.write(json.dumps(generate_dialogue()) + "\n")
