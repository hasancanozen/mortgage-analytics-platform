import os

try:
    # Optional: load from .env if present
    from dotenv import load_dotenv  # type: ignore
    load_dotenv()
except Exception:
    pass

DB_CONFIG = {
    "dbname": os.getenv("DB_NAME", "mortgage"),
    "user": os.getenv("DB_USER", "mortgageuser"),
    "password": os.getenv("DB_PASSWORD", ""),
    "host": os.getenv("DB_HOST", "localhost"),
    "port": int(os.getenv("DB_PORT", "5432")),
}