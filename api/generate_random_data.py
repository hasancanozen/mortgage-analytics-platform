"""
API endpoint responsible for generating random customer data.
"""

from fastapi import APIRouter, HTTPException

from services.RandomDataService import RandomDataService

router = APIRouter()
service = RandomDataService()


@router.post("/generate/customers")
def generate_customers(count: int = 1000):
    """
    Generate a specified number of random customers.

    Args:
        count (int): Number of customers to generate.

    Returns:
        dict: Operation status and generated count.
    """
    try:
        service.generate_customers(count)
        return {"status": "success", "count": count}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e
