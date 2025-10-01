from sklearn.ensemble import RandomForestRegressor

def getModel():
    mlmodel = RandomForestRegressor(
        n_estimators = 100,
        max_depth = 10,
        random_state = 42,
        n_jobs = -1
    )
    return mlmodel

