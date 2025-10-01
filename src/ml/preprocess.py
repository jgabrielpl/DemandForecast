import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

from src.utils.logger import getLogger

logger = getLogger()

# Encodando as colunas categóricas do df
def encodeCategorical(df: pd.DataFrame, encoder_path: str, fit: bool = True) -> pd.DataFrame:
    categorical_cols = df.select_dtypes(include = ["object"]).columns
    encoders = {}

    # Se Fit = True -> treina os encoders e salva
    if fit:
        logger.info("Treinando e salvando encoders das variáveis categóricas")
        
        for col in categorical_cols:
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col].astype(str))
            encoders[col] = le

            joblib.dump(encoders, encoder_path)

            logger.info(f"Encoders salvos em {encoder_path}")

    # Se Fit = False -> carrega encoders salvos e aplica no df
    else:
        logger.info("Carregando encoders salvos")
        encoders = joblib.load(encoder_path)

        for col in categorical_cols:
            if col in encoders:
                df[col] = df[col].map(lambda x: encoders[col].transform([str(x)])[0]
                                      if str(x) in encoders[col].classes_ else -1)
            
            logger.info("Encoders aplicados no dataset com sucesso")

    return df

