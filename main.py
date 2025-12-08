"""
Main module for the Mortgage Analytics Platform API.

This module initializes the FastAPI application and registers all API routers.
"""
from fastapi import FastAPI

from api.generate_random_address import router as address_data_router
from api.generate_random_data import router as fake_data_router

app = FastAPI(title="Mortgage Analytics Platform API")

app.include_router(fake_data_router)
app.include_router(address_data_router)
