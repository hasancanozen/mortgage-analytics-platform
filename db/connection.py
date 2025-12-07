import psycopg2
from config.settings import DB_CONFIG

class Database:
    def __init__(self):
        self.conn = None

    def connect(self):
        if self.conn is None:
            self.conn = psycopg2.connect(**DB_CONFIG)
        return self.conn

    def cursor(self):
        return self.connect().cursor()

    def commit(self):
        if self.conn:
            self.conn.commit()

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None