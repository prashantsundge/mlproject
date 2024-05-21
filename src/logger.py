# logger.py
import logging
import os
from datetime import datetime

LOG_DIR = os.path.join(os.getcwd(), "logs")
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.log"
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)


logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format="[%(asctime)s:%(lineno)d %(name)s %(levelname)s] %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
    
)

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.info("Logging Started - IN PROGRESS")
    logger.info(f"Logging file log Dir {LOG_DIR} , Log file{LOG_FILE} , log file path {LOG_FILE_PATH}")
