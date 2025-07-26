from fastapi import HTTPException
from bson import ObjectId
from app.models import transactions as Transaction
from app.database import db
import traceback
#hello saya add comment ini untuk menambahkan komentar di file transactions.py! sangat membantu karena saya tidak tahu apa yang harus saya tambahkan di file ini.
async def create_transaction(transaction: Transaction):
    try:
        result = await db.transactions.insert_one(transaction.dict())
        return {"id": str(result.inserted_id)}
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail="Failed to create transaction")

async def get_transactions():
    try:
        transactions = []
        async for item in db.transactions.find():
            item["_id"] = str(item["_id"])
            transactions.append(item)
        return transactions
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail="Failed to fetch transactions")

async def get_top_5_transactions():
    try:
        pipeline = [
            { "$match": { "amount": { "$type": "number" } } },
            { "$sort": { "amount": -1 } },
            { "$limit": 5 }
        ]
        results = []
        async for item in db.transactions.aggregate(pipeline):
            item["_id"] = str(item["_id"])
            results.append(item)
        return results
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

async def get_transactions_by_type(transaction_type: str):
    try:
        transactions = []
        async for item in db.transactions.find({
            "type": {"$regex": f"^{transaction_type}$", "$options": "i"}
        }):
            item["_id"] = str(item["_id"])
            transactions.append(item)
        return transactions
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail="Failed to fetch transactions by type")

async def delete_transaction(transaction_id: str):
    try:
        result = await db.transactions.delete_one({"_id": ObjectId(transaction_id)})
        if result.deleted_count:
            return {"message": "Transaction deleted"}
        raise HTTPException(status_code=404, detail="Transaction not found")
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail="Failed to delete transaction")
    
    
