from fastapi import APIRouter
from app.models.transactions import Transaction as TransactionModel
from app.controllers import transactions as TransactionController

router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"]
)

@router.post("")
async def create(transaction: TransactionModel):
    return await TransactionController.create_transaction(transaction)

@router.get("")
async def get_all():
    return await TransactionController.get_transactions()

@router.get("/top5")
async def get_top_5():
    return await TransactionController.get_top_5_transactions()

@router.get("/type/{transaction_type}")
async def get_by_type(transaction_type: str):
    return await TransactionController.get_transactions_by_type(transaction_type)

@router.delete("/{transaction_id}")
async def delete(transaction_id: str):
    return await TransactionController.delete_transaction(transaction_id)
