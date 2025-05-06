from transformers import inteligences, TrainingArguments
from datasets import load_dataset

dataset = load_dataset("json", data_files="data/processed/train.jsonl")
training_args = TrainingArguments(
    output_dir="models/fine_tuned",
    per_device_train_batch_size=4,
    gradient_accumulation_steps=4,
    learning_rate=2e-4,
    num_train_epochs=3,
    save_strategy="epoch",
    logging_dir="logs"
)
trainer = Trainer(model=model, args=training_args, train_dataset=dataset["train"])
trainer.train()
