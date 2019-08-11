import logging
import pickle
import responder
import numpy as np

app = responder.API()

@app.route('/')
def index(request, response):
    # 予測データ
    sepal_length = request.params.get("sepal_length")
    sepal_width = request.params.get("sepal_width")
    petal_length = request.params.get("petal_length")
    petal_width = request.params.get("petal_width")

    # TODO: validation
    data = [sepal_length, sepal_width, petal_length, petal_width]
    logging.info(data)

    # 標準化オブジェクトの読込
    file_name = "./static/scaler.pkl"

    with open(file_name, 'rb') as f:
        scaler = pickle.load(f)

    # 標準化
    X = scaler.transform(np.array([data]))
    logging.info(X)

    # 学習済みモデルの読込
    file_name = "./static/model.pkl"

    with open(file_name, 'rb') as f:
        model = pickle.load(f)

    # 予測
    y = model.predict(X, batch_size=1)
    logging.info(y)
    response.headers.update({'Content-Type': 'application/json'})
    response.media = {"label": int(y[0].argmax()), "accuracy": float(y[0].max())}

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
