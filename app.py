import os
from dotenv import load_dotenv
from flask import Flask
from covalent_api.class_a import ClassA
from covalent_api.session import Session

load_dotenv()

session = Session(server_url="https://api.covalenthq.com", api_key=os.getenv("API_KEY"))
covalent = ClassA(session)
CHAIN_ID = "1"  # ethereun chain

app = Flask(__name__)


@app.route("/")
def home():
    return {"ho": "me"}


@app.route("/transactions/erc20/<string:address>/<string:contract_address>")
def get_erc20_transactions(address, contract_address):
    """
    args:
    address: sender address
    contract_address: token address
    """
    result = covalent.get_erc20_token_transfers(CHAIN_ID, address, contract_address)
    return result


@app.route("/transactions/<string:address>")
def get_transactions(address):
    result = covalent.get_transactions(CHAIN_ID, address)
    return result


@app.route("/balances/<string:address>")
def get_token_balances(address):
    result = covalent.get_token_balances_for_address(CHAIN_ID, address)
    return result


@app.route("/portfolio/<string:address>")
def get_historical_portfolio(address):
    result = covalent.get_historical_portfolio_value_over_time(CHAIN_ID, address)
    return result
