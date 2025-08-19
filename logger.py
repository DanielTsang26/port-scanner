import logging
import os
from utils import LOG_DIR

os.makedirs(LOG_DIR, exist_ok = True)

def setup_logger(name:str, filename: str = "porthound.csv") -> logging.Logger:

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    file_handler = logging.FileHandler(os.path.join(LOG_DIR, filename))
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)

    if not logger.handlers:
        logger.addHandler(file_handler)

    return logger
