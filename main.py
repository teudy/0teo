from fastapi import FastAPI

app = FastAPI(
    title="API de Retiros BTC",
    docs_url="/docs",
    redoc_url=None
)

@app.get("/")
def home():
    return {"msg": "Bienvenido a la API de retiro BTC"}

@app.post("/retirar")
def retirar(monto: float, wallet: str):
    return {"msg": f"Retiro de {monto} BTC enviado a {wallet}"}
