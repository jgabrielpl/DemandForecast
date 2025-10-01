import argparse

from src import extract, transform, load

from src.utils.logger import getLogger
from src.ml.train import trainModel
from src.ml.predict import predictModel

logger = getLogger()

# Executa o pipeline ETL
def run_etl():
    logger.info("Iniciando processo ETL")
    raw_paths = "data/raw"

    train_df, test_df, store_df = extract(raw_paths)
    
    datasets = {"train": train_df, "test": test_df, "store": store_df}
    transformed = transform(datasets)
    train_df = transformed["train"]
    test_df = transformed["test"]

    load(train_df, test_df)
    logger.info("Processo da pipeline ETL realizada com sucesso ")


# Executa o treinamento de ML, treinando e salvando modelo
def run_train():
    logger.info("Iniciando treinamento ML")
    trainModel()
    logger.info("Treinamento ML realizado com sucesso")


# Vai gerar as previsões com o modelo treinado
def run_predict():
    logger.info("Iniciando predições")
    predictModel()
    logger.info("Predições realizadas com sucesso")


# Definindo e executando cada etapa escolhida do pipeline
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description= "Pipeline de Previsão de Demanda - com dataset Rossmann(Kaggle)")
    parser.add_argument(
        "stage",
        choices = ["etl", "train", "predict", "all"],
        help = "Escolha qual etapa rodar: etl, train, predict ou all"
    )

    args = parser.parse_args()

    stages = {
        "etl": run_etl,
        "train": run_train,
        "predict": run_predict,
        "all": lambda: (run_etl(), run_train(), run_predict())
    }

    stages[args.stage]()

