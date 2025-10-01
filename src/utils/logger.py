import logging
import os

def getLogger():
    os.makedirs("artifacts/logs", exist_ok=True)

    logh_file_path = "artifacts/logs/Processo.log"

    logging.basicConfig(
        level = logging.INFO,
        format = "%(asctime)s - %(levelname)s - %(message)s",
        handlers = [logging.FileHandler(logh_file_path), logging.StreamHandler()]
    )
    return logging.getLogger(__name__)

