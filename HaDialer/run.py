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
    "description": "Action USB Python",
    "fields": {
        "cmd": {"description":"Commande USB"}
    }
})

@app.route("/dial", methods=["POST"])
def dial():
    data = request.json or {}
    log.info("Commande reçue:", data)
    return "OK"

app.run(host="0.0.0.0", port=8124, debug=True)
