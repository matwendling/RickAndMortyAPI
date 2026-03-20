import os


def load_database_connection_settings() -> dict:
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