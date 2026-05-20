from dataclasses import asdict
from uuid import uuid4
import psycopg2 as pg
import psycopg2.extras as extras
from psycopg2.extensions import connection, cursor
from framework.database.load_database_connection_settings import (
    load_database_connection_settings as _load_database_connection_settings
)

class PsycopgRepository:
    def __init__(self, table: str, keys: list[str]):
        connection_info = _load_database_connection_settings()
        
        self.conn: connection = pg.connect(**connection_info)
        self.cur: cursor = self.conn.cursor()
        self.table = table
        self.keys = keys

    def create(self, create: dict) -> None:
        create["id"] = str(uuid4())

        keys = ""
        values = ""
        for k in create.keys():
            keys += f"{k}, "
            values += f"%({k})s, "

        if keys.endswith(", "):
            keys = keys.removesuffix(", ")

        if values.endswith(", "):
            values = values.removesuffix(", ")

        sql_query = f"INSERT INTO {self.table} ({keys}) VALUES ({values}) RETURNING id;"
        self.cur.execute(sql_query, create)
        self.conn.commit()
        return self.cur.fetchall()[0][0]
    
    def create_many(self, create_list: list[dict]) -> list[str]:
        values = []

        for create in create_list:
            item = [str(uuid4())]
            item.extend(create.values())
            values.append(tuple(item))

        keys = self.__keys_to_str()

        sql_query = f"INSERT INTO {self.table} ({keys}) VALUES %s RETURNING id;"
        extras.execute_values(self.cur, sql_query, values, page_size=1000,)
        self.conn.commit()
        return [str(e[0]) for e in self.cur.fetchall()]
    
    def get(self, where: dict) -> list[dict]:
        sql_query = f"SELECT * FROM {self.table} WHERE "
        filter_values = []

        for filter, value in where.items():
            if value is not None:
                sql_query += f"{filter} = %s AND "
                filter_values.append(value)

        if sql_query.endswith(" AND "):
            sql_query = sql_query.removesuffix(" AND ")

        if sql_query.endswith(" WHERE "):
            sql_query = sql_query.removesuffix(" WHERE ")

        sql_query += ";"
        self.cur.execute(sql_query, filter_values)

        if not self.cur.description:
            raise pg.errors.QueryCanceled("Could not find table column names.")
        
        column_names = [desc.name for desc in self.cur.description]

        return [dict(zip(column_names, row)) for row in self.cur.fetchall()]

    def update(self, uuid: str, update: dict) -> str:
        sql_query = f"UPDATE {self.table} SET "
        filter_values = []

        for filter, value in update.items():
            if value is not None:
                sql_query += f"{filter} = %s, "
                filter_values.append(value)

        if len(filter_values) == 0:
            raise pg.errors.QueryCanceled("Could not complete query due to unexisting values.")
        
        if sql_query.endswith(", "):
            sql_query = sql_query.removesuffix(", ")
        
        sql_query += f" WHERE id = %s;"

        filter_values.append(uuid)

        self.cur.execute(sql_query, filter_values)
        self.conn.commit()

        return uuid
    
    def delete(self, uuid: str) -> None:
        sql_query = f"DELETE FROM {self.table} WHERE id = %s;"
        self.cur.execute(sql_query, (uuid, ))
        self.conn.commit()
    
    def __keys_to_str(self) -> str:
        keys = ""
        for k in self.keys:
            keys += f"{k}, "
        if keys.endswith(", "):
            keys = keys.removesuffix(", ")
        return keys