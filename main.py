from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="Spendy REST API",
    description="API untuk mengelola transaksi keuangan (pemasukan dan pengeluaran)",
    version="1.0.0"
)

app.include_router(router)