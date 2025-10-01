import pandas as pd
import joblib

from src.utils.logger import getLogger

from src.ml.preprocess import encodeCategorical
from src.ml.evaluate import evaluateModel
from src.ml.mlmodels.random_forest import getModel

from sklearn.model_selection import train_test_split

logger = getLogger()

def trainModel(
        train_path: str = "data/processed/train_processed.csv",
        model_path: str = "artifacts/models/model.pkl",
        encoder_path: str = "artifacts/models/encoders.pkl"
) -> None:

    logger.info("Carregando dados de treino...")
    df = pd.read_csv(train_path)

    x = df.drop(columns=["Id", "Sales", "Customers"], errors="ignore")
    y = df["Sales"]

    logger.info("Aplicando encoder nas variáveis categóricas")
    x = encodeCategorical(x, encoder_path = encoder_path, fit = True)

    logger.info("Separando treino e validação")
    x_train, x_val, y_train, y_val = train_test_split(
        x, y, test_size = 0.3, random_state = 42
    )

    logger.info("Treinando modelo...")
    model = getModel()
    model.fit(x_train, y_train)

    y_pred = model.predict(x_val)
    metrics = evaluateModel(y_val, y_pred)
    logger.info(f"Avaliação --> RMSE: {metrics['RMSE']:.2f} ; MAE: {metrics['MAE']:.2f} ; R2: {metrics['R2']:.2f}")

    joblib.dump(model, model_path)
    logger.info(f"Modelo salvo com sucesso em {model_path}")

    