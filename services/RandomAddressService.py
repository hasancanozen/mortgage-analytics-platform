"""
Service module for generating random addresses and storing them in the database.
"""

import random
from faker import Faker
from data.city_data import CITY_DATA
from db.connection import Database


class RandomAddressService:
    """
    Service class responsible for generating random customer addresses
    and inserting them into the database.
    """

    def __init__(self):
        """Initialize Faker and database connection."""
        self.fake = Faker("tr_TR")
        self.db = Database()

    def generate_addresses(self, addresses_per_customer=1):
        """
        Generate random addresses for customers who do not already have one.

        Args:
            addresses_per_customer (int): How many addresses to create per customer.
        """
        conn = self.db.connect()
        cur = conn.cursor()

        cur.execute(
            """
            SELECT c.customer_id
            FROM customer.customer AS c
            WHERE NOT EXISTS (
                SELECT 1 FROM customer.address AS a
                WHERE a.customer_id = c.customer_id
            )
            """
        )
        customers = cur.fetchall()

        if not customers:
            print("Customer tablosunda kayıt bulunamadı!")
            return

        for (customer_id,) in customers:
            for _ in range(addresses_per_customer):
                city = random.choice(list(CITY_DATA.keys()))
                district = random.choice(list(CITY_DATA[city].keys()))
                postal_code = CITY_DATA[city][district]

                street = self.fake.street_name()
                building_no = str(random.randint(1, 200))
                apartment_no = str(random.randint(1, 50))

                address_line1 = (
                    f"{street} No: {building_no} Daire: {apartment_no}"
                )
                address_line2 = None

                cur.execute(
                    """
                    INSERT INTO customer.address
                    (customer_id, address_line1, address_line2, city,
                     district, postal_code)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    """,
                    (
                        customer_id,
                        address_line1,
                        address_line2,
                        city,
                        district,
                        postal_code,
                    ),
                )

        conn.commit()
        print(
            f"Adresi olmayan müşteriler için kişi başı "
            f"{addresses_per_customer} adres oluşturuldu."
        )
