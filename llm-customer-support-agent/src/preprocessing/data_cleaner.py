import json
import os
import re

def clean_data(input_file, output_file):
    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    with open(input_file, "r") as infile, open(output_file, "w") as outfile:
        for line in infile:
            try:
                dialogue = json.loads(line.strip())
                # Clean query and response (remove special chars, normalize case)
                dialogue["query"] = re.sub(r'[^\w\s]', '', dialogue["query"]).lower()
                dialogue["response"] = re.sub(r'[^\w\s]', '', dialogue["response"]).lower()
                # Write cleaned dialogue
                outfile.write(json.dumps(dialogue) + "\n")
            except json.JSONDecodeError:
                continue

if __name__ == "__main__":
    input_path = "data/raw/dialogues.jsonl"
    output_path = "data/processed/cleaned_dialogues.jsonl"
    clean_data(input_path, output_path)
