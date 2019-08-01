import responder
from sklearn.datasets import load_iris

app = responder.API()

@app.route("/")
async def index(request, response):
    data = load_iris()
    response.text = str(data['DESCR'])
