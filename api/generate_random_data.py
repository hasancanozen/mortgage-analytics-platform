from fastapi import APIRouter, HTTPException
from services.random_data_services import FakeDataService

router = APIRouter()
service = FakeDataService()

@router.post("/generate/customers")
def generate_customers(count: int = 1000):
    try:
        service.generate_customers(count)
        return {"status": "success", "count": count}
    except Exception as e:
        # Hata detayını istemciye dönerek teşhisi kolaylaştırır
        raise HTTPException(status_code=500, detail=str(e))
