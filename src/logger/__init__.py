import logging
import os
from logging.handlers import RotatingFileHandler
from datetime import datetime

LOG_DIR = 'logs'
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
MAX_LOG_SIZE = 5 * 1024 * 1024  # 5 MB
BACKUP_COUNT = 3

# Ensure log directory exists
os.makedirs(LOG_DIR, exist_ok=True)
log_file_path = os.path.join(LOG_DIR, LOG_FILE)

def configure_custom_logger():
    """
    Configures and returns a logger with both file and console handlers.
    """
    logger = logging.getLogger("custom_logger")
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter("[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s")

    # File handler
    file_handler = RotatingFileHandler(log_file_path, maxBytes=MAX_LOG_SIZE, backupCount=BACKUP_COUNT)
    file_handler.setFormatter(formatter)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    return logger

# Create the logger instance
custom_logger = configure_custom_logger()
