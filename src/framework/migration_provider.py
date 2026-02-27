import os
import psycopg2
from psycopg2.extensions import connection, cursor

class MigrationProvider:
    def __init__(self):
        connection_info = self.__load_database_connection_settings()
        
        self.conn: connection = psycopg2.connect(**connection_info)
        self.cur: cursor = self.conn.cursor()

        self.__create_migration_table_if_not_exists()

    def exists(self, name: str) -> bool:
        self.cur.execute("SELECT * FROM migrations WHERE name = %s;", (name,))
        migration = self.cur.fetchall()
        return len(migration) > 0

    def execute(self, query: str, params: list) -> None:
        self.cur.execute(query, params)
        self.conn.commit()

    def add(self, name: str) -> None:
        self.cur.execute("INSERT INTO migrations (name) VALUES (%s);", (name,))
        self.conn.commit()

    def __create_migration_table_if_not_exists(self) -> None:
        self.cur.execute("""
            CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
            CREATE TABLE IF NOT EXISTS migrations (
                id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
                name VARCHAR(255) NOT NULL,
                CONSTRAINT unique_migration_row UNIQUE (name)
            );
        """)
        self.conn.commit()

    def __load_database_connection_settings(self) -> dict:
        host = os.getenv("DB_HOST")
        if not host:
            raise ConnectionError("Could not find database connection host.")
        
        user = os.getenv("DB_USER")
        if not user:
            raise ConnectionError("Could not find database connection user.")
        
        password = os.getenv("DB_PASSWORD")
        if not password:
            raise ConnectionError("Could not find database connection password.")
        
        dbname = os.getenv("DB_NAME")
        if not dbname:
            raise ConnectionError("Could not find database connection dbname.")

        port = os.getenv("DB_PORT")
        if not port:
            raise ConnectionError("Could not find database connection port.")
        
        return {
            "host": host,
            "user": user,
            "password": password,
            "dbname": dbname,
            "port": int(port)
        }