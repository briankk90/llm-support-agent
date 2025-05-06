import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from transformers import Trainer, TrainingArguments
from datasets import load_dataset
from src.training.qlora_peft import setup_peft_model
from src.utils.config_parser import load_config
from src.utils.logger import logger

def train_model(config_path="src/training/config.yaml"):
    try:
        # Load configuration
        config = load_config(config_path)
        logger.info("Configuration loaded successfully")
        
        # Load dataset
        dataset_path = "data/processed/train.jsonl"
        if not os.path.exists(dataset_path):
            raise FileNotFoundError(f"Dataset not found at {dataset_path}")
        dataset = load_dataset("json", data_files=dataset_path)
        logger.info("Dataset loaded successfully")
        
        # Setup model and tokenizer
        model, tokenizer = setup_peft_model()
        logger.info("Model and tokenizer initialized")
        
        # Define training arguments
        training_args = TrainingArguments(
            output_dir=config["training"]["output_dir"],
            per_device_train_batch_size=config["training"]["batch_size"],
            gradient_accumulation_steps=config["training"]["gradient_accumulation_steps"],
            learning_rate=config["training"]["learning_rate"],
            num_train_epochs=config["training"]["num_train_epochs"],
            save_strategy="epoch",
            logging_dir="logs",
            logging_steps=10,
            fp16=True,  # Enable mixed precision for GPU
        )
        
        # Initialize trainer
        trainer = Trainer(
            model=model,
            args=training_args,
            train_dataset=dataset["train"],
            tokenizer=tokenizer
        )
        logger.info("Trainer initialized")
        
        # Run training
        trainer.train()
        logger.info("Training completed")
        
        # Save final model
        final_model_path = os.path.join(config["training"]["output_dir"], "final")
        trainer.save_model(final_model_path)
        logger.info(f"Model saved to {final_model_path}")
        
    except Exception as e:
        logger.error(f"Training failed: {str(e)}")
        raise

if __name__ == "__main__":
    train_model()
