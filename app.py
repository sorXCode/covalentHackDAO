import os
from dotenv import load_dotenv
from flask import Flask
import requests

load_dotenv()
CONVALENT_API_KEY = os.getenv('COVALENT_API_KEY')
app = Flask(__name__)


@app.route("/")
def home():
    return {"ho": "me"}


@app.route("/transactions_erc20/<string:address>/<string:contract_address>")
def get_erc20_transactions(address, contract_address):
    """
    args:
    address: EOA
    contract_address: token address
    """
    CHAIN_ID = '1'  # ethereun chain
    url = 'https://api.covalenthq.com/v1/{CHAIN_ID}/address/{EOA}/transfers_v2/?quote-currency=USD&format=JSON&contract-address={CONTRACT_ADDRESS}&key={COVALENT_API_KEY}'
    response = requests.get(url.format(CHAIN_ID=CHAIN_ID, EOA=address, CONTRACT_ADDRESS=contract_address, COVALENT_API_KEY=CONVALENT_API_KEY))
    result = response.json()
    return result, response.status_code
