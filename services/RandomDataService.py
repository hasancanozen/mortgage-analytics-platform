"""Module for generating random customer data."""

import random
from faker import Faker

from db.connection import Database


class RandomDataService:
    """
    Service class responsible for generating random customer data
    and inserting it into the database.
    """

    def __init__(self):
        """Initialize Faker and the database connection."""
        self.fake = Faker("tr_TR")
        self.db = Database()

    def generate_customers(self, count=10000):
        """
        Generate a specified number of random customer records and insert them into the database.

        Args:
            count (int): Number of customers to generate.
        """
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
