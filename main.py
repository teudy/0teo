
from fastapi import FastAPI, Form
import requests
import os

app = FastAPI()

BYBIT_API_KEY = os.getenv("BYBIT_API_KEY")
BYBIT_API_SECRET = os.getenv("BYBIT_API_SECRET")
BTC_WALLET = os.getenv("BTC_WALLET")

@app.get("/")
def root():
    return {"message": "API de retiro BTC activa."}

@app.post("/retirar")
def retirar_btc(monto: float = Form(...), direccion: str = Form(...)):
    headers = {
        "X-BYBIT-API-KEY": BYBIT_API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "coin": "BTC",
        "address": direccion,
        "amount": monto,
        "wallet_type": "spot"
    }
    response = requests.post(
        "https://api.bybit.com/v5/asset/withdraw/create",
        headers=headers,
        json=payload,
        auth=(BYBIT_API_KEY, BYBIT_API_SECRET)
    )
    return response.json()
