import os

import requests
from dotenv import load_dotenv
from flask import Flask

load_dotenv()
COVALENT_API_KEY = os.getenv("COVALENT_API_KEY")
CHAIN_ID = "1"  # ethereun chain
app = Flask(__name__)


@app.route("/")
def home():
    return {"ho": "me"}


@app.route("/transactions_erc20/<string:address>/<string:contract_address>")
def get_erc20_transactions(address, contract_address):
    """
    args:
    address: sender address
    contract_address: token address
    """
    url = "https://api.covalenthq.com/v1/{CHAIN_ID}/address/{ADDRESS}/transfers_v2/?quote-currency=USD&format=JSON&contract-address={CONTRACT_ADDRESS}&key={COVALENT_API_KEY}"
    response = requests.get(
        url.format(
            CHAIN_ID=CHAIN_ID,
            ADDRESS=address,
            CONTRACT_ADDRESS=contract_address,
            COVALENT_API_KEY=COVALENT_API_KEY,
        )
    )
    result = response.json()
    return result, response.status_code


@app.route("/transactions/<string:address>")
def get_transactions(address):
    url = "https://api.covalenthq.com/v1/{CHAIN_ID}/address/{ADDRESS}/transactions_v2/?quote-currency=USD&format=JSON&block-signed-at-asc=false&no-logs=false&key={COVALENT_API_KEY}"
    response = requests.get(
        url.format(
            CHAIN_ID=CHAIN_ID,
            ADDRESS=address,
            COVALENT_API_KEY=COVALENT_API_KEY
        )
    )
    result = response.json()
    return result, response.status_code
