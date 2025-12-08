# Mortgage Analytics Platform

## Purpose
- Simulate a production-like data environment for a mortgage lender, seed the database with realistic synthetic data, and expose endpoints to drive analytics/modeling workflows.
- Provide a clean FastAPI service layer to generate and manage data for downstream model experiments.

## Notes
- Environment variables are loaded from `.env`. Never commit real secrets; use `.env.example` as a template.
- PostgreSQL schema: `customer.customer` and `customer.address` tables. Columns align with the shared DDL.
- Synthetic data uses Turkish localization via `Faker("tr_TR")`.

## Setup
```zsh
cd /Users/hasancano/Documents/Projects/mortgage-analytics-platform
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Fill `.env` with real values
```

## Run
```zsh
uvicorn main:app --reload
```
- API docs: `http://127.0.0.1:8000/docs`

## Endpoints & Examples

### Generate Customers
- Path: `POST /generate/customers`
- Query params:
	- `count`: number of customers to generate (default: 1000)
- Curl:
```zsh
curl -X POST "http://127.0.0.1:8000/generate/customers?count=1000"
```
- Expected response:
```json
{"status":"success","count":1000}
```
- Note: If schema/tables are missing or column lengths are too strict, the DB may reject inserts.

### Generate Addresses (Only Missing)
- Path: `POST /generate/addresses`
- Query params:
	- `addresses_per_customer`: number of addresses to create for each customer lacking any address (default: 1)
- Curl:
```zsh
curl -X POST "http://127.0.0.1:8000/generate/addresses?addresses_per_customer=2"
```
- Expected response:
```json
{"status":"success","addresses_per_customer":2}
```
- Note: The service selects customers with no existing records in `customer.address` and populates `address_line1`, `address_line2`, `city`, `district`, `postal_code` per your schema.

## Database Schema (Summary)
- `customer.customer(customer_id, national_id, first_name, last_name, birth_date, phone, email, marital_status, created_at, updated_at)`
- `customer.address(address_id, customer_id -> customer.customer(customer_id), address_line1, address_line2, city, district, postal_code, created_at)`

## Development
- `.gitignore` excludes `.env` and virtualenv folders; do not commit secrets.
- Imports should match service filenames (e.g., `services/RandomDataService.py` → `from services.RandomDataService import RandomDataService`).
- On errors, the API returns 500 with a `detail` message; inspect it for diagnosis.
