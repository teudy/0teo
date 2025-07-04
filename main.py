from fastapi import FastAPI

app = FastAPI(
    title="API de Retiros BTC",
    docs_url="/docs"  # 👈 esto activa la documentación
)

@app.get("/")
def home():
    return {"msg": "Bienvenido a la API de retiro BTC"}
