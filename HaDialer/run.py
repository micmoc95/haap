import os, requests, logging
from flask import Flask, request

SUPERVISOR = "http://supervisor"
TOKEN = os.environ["SUPERVISOR_TOKEN"]

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
log = logging.getLogger("hadialer")
log.info("Starting ...")

def ha(url, data=None):
    return requests.post(
        SUPERVISOR + url,
        headers={"Authorization": f"Bearer {TOKEN}"},
        json=data
    )

ha("/core/api/services/hadialer/dial", {
    "description": "Composition d'un numéro de téléphone",
    "fields": {
        "num": {"description":"Numéro à composer"}
    }
})

@app.route("/dial", methods=["POST"])
def dial():
    data = request.json or {}
    log.info("Commande reçue: %s", data.get("num"))
    return "OK"

app.run(host="0.0.0.0", port=8124)
