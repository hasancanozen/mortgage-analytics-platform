"""
API endpoint responsible for generating random address data.
"""

from fastapi import APIRouter, HTTPException

from services.RandomAddressService import RandomAddressService

router = APIRouter()
service = RandomAddressService()


@router.post("/generate/addresses")
def generate_addresses(addresses_per_customer: int = 1):
    """
    Generate random addresses for customers.

    Args:
        addresses_per_customer (int): Number of addresses to generate per customer.

    Returns:
        dict: Status information and generation parameters.
    """
    try:
        service.generate_addresses(addresses_per_customer)
        return {
            "status": "success",
            "addresses_per_customer": addresses_per_customer,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e
