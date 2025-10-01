import pandas as pd

from src.utils.logger import getLogger

logger = getLogger()

def transform(datasets: dict) -> dict:
    store = datasets["store"]
    train = datasets["train"].merge(store, how = "left", on = "Store")
    test = datasets["test"].merge(store, how = "left", on = "Store")

    train.fillna(0, inplace = True)
    test.fillna(0, inplace = True)

    # Criando colunas temporais úteis, em ano, mês, dia, semana do ano, dia da semana e se é final de semana
    for df in [train, test]:
        df["Date"] = pd.to_datetime(df["Date"])
        df["DayOfWeek"] = df["Date"].dt.dayofweek
        df["Year"] = df["Date"].dt.year
        df["Month"] = df["Date"].dt.month
        df["Day"] = df["Date"].dt.day
        df["WeekOfYear"] = df["Date"].dt.isocalendar().week.astype(int)

    for df in [train, test]:
        df.drop(columns = ["Date"], inplace = True)

    # Filtrando vendas invalidas
    train = train[(train["Open"] != 0) & (train["Sales"] > 0)]

    for col in ["CompetitionDistance"]:
        median = train[col].median()
        train[col].fillna(median, inplace = True)
        test[col].fillna(median, inplace = True)

    logger.info("Tratamento feito com sucesso")

    return {"train": train, "test": test}

