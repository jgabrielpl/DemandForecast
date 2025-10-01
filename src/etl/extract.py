import pandas as pd
from pathlib import Path

from src.utils.logger import getLogger

logger = getLogger()

def extract(data_path: str):
    logger.info("Processo de ingestão iniciado")

    datasets = {}
    data_files = {
        "train": Path(data_path) / "train.csv", 
        "test": Path(data_path) / "test.csv", 
        "store": Path(data_path) / "store.csv"
    }

    train_df = pd.read_csv(data_files["train"])
    test_df = pd.read_csv(data_files["test"])
    store_df = pd.read_csv(data_files["store"])

    for name, path in data_files.items():
        try:
            datasets[name] = pd.read_csv(path)
            logger.info(f"Arquivo {name} carregado com {datasets[name].shape[0]} linhas e {datasets[name].shape[1]} colunas")
        
        except Exception as exc:
            logger.error(f"Erro ao carregar o arquivo {name}.csv: {exc}")
        
    return train_df, test_df, store_df

