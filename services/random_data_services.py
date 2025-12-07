from faker import Faker
import random
from db.connection import Database


class FakeDataService:
    def __init__(self):
        self.fake = Faker("tr_TR")
        self.db = Database()

    def generate_customers(self, count=10000):
        conn = self.db.connect()
        cur = conn.cursor()

        for _ in range(count):
            cur.execute(
                """
                INSERT INTO customer.customer
                (
                    national_id,
                    first_name,
                    last_name,
                    birth_date,
                    phone,
                    email,
                    marital_status
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """,
                (
                    self.fake.ssn(),
                    self.fake.first_name(),
                    self.fake.last_name(),
                    self.fake.date_of_birth(minimum_age=20, maximum_age=70),
                    self.fake.phone_number(),
                    self.fake.email(),
                    random.choice(["Single", "Married"]),
                ),
            )

        conn.commit()
        print(f"{count} adet müşteri oluşturuldu.")
