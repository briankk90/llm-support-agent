import json
import random
import os

def generate_dialogue():
    queries = ["How do I return a product?", "My order is delayed, help!"]
    responses = ["Please visit our returns page...", "Let me check your order status..."]
    return {"query": random.choice(queries), "response": random.choice(responses)}

# Ensure raw directory exists
os.makedirs("raw", exist_ok=True)

# Write dialogues to raw directory
output_path = os.path.join("raw", "dialogues.jsonl")
with open(output_path, "w") as f:
    for _ in range(1000):
        f.write(json.dumps(generate_dialogue()) + "\n")
