from pathlib import Path

from src.utils.logger import getLogger

logger = getLogger()

def load(train_df, test_df, output_path: str = "data/processed"):
    Path(output_path).mkdir(parents = True, exist_ok = True)

    train_df.to_csv(Path(output_path) / "train_processed.csv", index=False)
    test_df.to_csv(Path(output_path) / "test_processed.csv", index=False)

    logger.info(f"Arquivo salvo com sucesso: {output_path}")

