import yaml
from src.utils.logger import logger

def load_config(file_path):
    try:
        with open(file_path, 'r') as f:
            config = yaml.safe_load(f)
        if not config:
            raise ValueError(f"Configuration file {file_path} is empty")
        logger.info(f"Loaded configuration from {file_path}")
        return config
    except FileNotFoundError:
        logger.error(f"Configuration file {file_path} not found")
        raise
    except yaml.YAMLError as e:
        logger.error(f"Error parsing YAML file {file_path}: {str(e)}")
        raise
