from fastapi import FastAPI
from api.generate_random_data import router as fake_data_router

app = FastAPI(title="Mortgage Analytics Platform API")

app.include_router(fake_data_router)
