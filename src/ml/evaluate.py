import numpy as np

from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from src.utils.logger import getLogger

logger = getLogger()

# Avalia o desempenho do modelo com múltiplas métricas de regressão
def evaluateModel(y_true, y_pred):
    logger.info("Calculando as métricas de avaliação")

    y_true = np.asarray(y_true).ravel()
    y_pred = np.asarray(y_pred).ravel()

    if y_true.shape != y_pred.shape:
        logger.error("Shapes diferentes em evaluateModel")
        raise ValueError("y_true e y_pred deve ter o mesmo shape")

    mae = mean_absolute_error(y_true, y_pred)
    mse = mean_squared_error(y_true, y_pred)
    rmse = float(np.sqrt(mse))
    r2 = float(r2_score(y_true, y_pred))

    metrics = {"RMSE": rmse, "MAE": mae, "R2": r2}

    logger.info(f"Resultados --> RMSE: {metrics['RMSE']} ; MAE: {metrics['MAE']} ; R2: {metrics['R2']}")

    return metrics

