import numpy as np
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import xgboost as xgb

import mlflow.xgboost

if __name__ == '__main__':
    # データの準備
    data = load_boston()
    x_train, x_validation, y_train, y_validation = train_test_split(data.data, data.target, train_size=0.8, random_state=0)

    params = {
        'objective': 'reg:linear',
        'max_depth': 6
    }

    with mlflow.start_run() as run:
        # 学習
        model = xgb.XGBRegressor(
            objective=params['objective'],
            max_depth=params['max_depth']
        )
        model.fit(x_train, y_train)

        # 予測
        y_pred = model.predict(x_validation)

        # 評価
        rmse = np.sqrt(mean_squared_error(y_validation, y_pred))

        mlflow.log_params(params)
        mlflow.log_metric('rmse', rmse)
        mlflow.xgboost.log_model(model, 'model')
        print('Model logged in run {}'.format(run.info.run_uuid))
