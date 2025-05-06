import json
import os
from datasets import Dataset

def format_dataset(input_file, output_file):
    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    # Read and format dialogues
    formatted_data = []
    with open(input_file, "r") as infile:
        for line in infile:
            try:
                dialogue = json.loads(line.strip())
                # Format as a single text field for training
                formatted_text = f"Customer: {dialogue['query']} Assistant: {dialogue['response']} <|END|>"
                formatted_data.append({"text": formatted_text})
            except json.JSONDecodeError:
                continue
    
    # Convert to Hugging Face dataset and save
    dataset = Dataset.from_list(formatted_data)
    dataset.to_json(output_file, orient="records", lines=True)

if __name__ == "__main__":
    input_path = "data/processed/cleaned_dialogues.jsonl"
    output_path = "data/processed/train.jsonl"
    format_dataset(input_path, output_path)
