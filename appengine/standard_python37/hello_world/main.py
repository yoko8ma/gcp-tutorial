import responder
from sklearn.datasets import load_iris
from google.cloud.logging import Client

client = Client.from_service_account_json("./service_account.json")
client.setup_logging()

app = responder.API()

@app.route("/")
async def index(request, response):
    import logging

    logging.info('================= Hello Logging =================')

    data = load_iris()
    response.text = str(data['DESCR'])
