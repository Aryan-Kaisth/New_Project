import os
import logging
from datetime import datetime

# Create timestamp once
timestamp = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")

# Log file name
LOG_FILE = f"{timestamp}.log"

# logs/<timestamp>/
log_dir = os.path.join(os.getcwd(), "logs", timestamp)
os.makedirs(log_dir, exist_ok=True)

# logs/<timestamp>/<timestamp>.log
LOG_FILE_PATH = os.path.join(log_dir, LOG_FILE)

# Logging setup
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(filename)s:%(lineno)d - %(levelname)s - %(message)s",
    level=logging.INFO,
    filemode="a"   # append mode (safe if re-run)
)
