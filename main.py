from fastapi import FastAPI

app = FastAPI(docs_url="/docs")

@app.get("/")
def home():
    return {"msg": "Bienvenido a la API de retiro BTC"}

@app.post("/retirar")
def retirar(wallet: str, monto: float):
    # lógica real de retiro aquí
    return {"status": "ok", "wallet": wallet, "monto": monto}
