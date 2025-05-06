from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import LoraConfig, get_peft_model
import torch
from src.utils.logger import logger

def setup_peft_model(model_name="mistralai/Mixtral-8x7B-Instruct-v0.1"):
    try:
        # Check for CUDA availability
        device = "cuda" if torch.cuda.is_available() else "cpu"
        logger.info(f"Using device: {device}")
        
        # Load model with 4-bit quantization
        model = AutoModelForCausalLM.from_pretrained(
            model_name,
            load_in_4bit=True,
            device_map="auto" if device == "cuda" else None
        )
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        logger.info(f"Model {model_name} and tokenizer loaded")
        
        # Configure LoRA
        lora_config = LoraConfig(
            r=16,
            lora_alpha=32,
            target_modules=["q_proj", "v_proj"],
            lora_dropout=0.05,
            bias="none",
            task_type="CAUSAL_LM"
        )
        model = get_peft_model(model, lora_config)
        logger.info("LoRA configuration applied")
        
        return model, tokenizer
    except Exception as e:
        logger.error(f"Failed to setup model: {str(e)}")
        raise
