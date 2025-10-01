import pandas as pd
import joblib

from src.utils.logger import getLogger
from src.ml.preprocess import encodeCategorical

logger = getLogger()

def predictModel(
        test_path: str = "data/processed/test_processed.csv", 
        model_path: str = "artifacts/models/model.pkl", 
        encoder_path: str = "artifacts/models/encoders.pkl",
        output_path: str = "data/predictions/predictions.csv"
) -> None:
    
    logger.info("Carregando novos dados de teste")

    df = pd.read_csv(test_path)

    # Criando a coluna date, sem ficar toda aquelas informações de data que tem nos test e train
    if all(col in df.columns for col in ["Year", "Month", "Day"]):
        df["Date"] = pd.to_datetime(df[["Year", "Month", "Day"]])
        logger.info("Criando coluna Date com ano, mês e dia")
    else:
        logger.warning("Erro ao criar Date, colunas Year, Month ou Day não foram encontradas")

    # Guardando store, date e id para mostrar na predictions mas não ir para o test da ml
    store_date_cols = df[["Store", "Date"]].copy()
    if "Id" in df.columns:
        store_date_cols["Id"] = df["Id"]

    x_test = df.drop(columns=["Date", "Id"], errors = "ignore")
    x_test = encodeCategorical(x_test, encoder_path= encoder_path, fit = False)

    logger.info("Carregando modelo treinado")
    model = joblib.load(model_path)

    logger.info("Gerando previsões")
    preds = model.predict(x_test)
    
    # Arredondando o resultado de cada previsão em 3 casas depois do .
    preds = [round(float(p), 3) for p in preds]

    result = store_date_cols.reset_index(drop = True)
    result["prediction"] = preds
    
    result.to_csv(output_path, index = False)
    logger.info(f"Previsões feitas som sucesso e salvas em {output_path}")

    