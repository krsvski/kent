import asyncio
import asyncpg
from asyncpg.pool import Pool
from database import config
from typing import Union


class Database:
    def __init__(self):
        self.pool: Union[Pool, None] = None
    
    async def create(self):
        pool = await asyncpg.create_pool(user=config.PGUSER, host=config.ip, database=config.PGDATABASE)
        self.pool = pool



    async def create_table_user(self):
        sql = """
        CREATE TABLE IF NOT EXISTS users(
            id serial PRIMARY KEY,
            user_id integer,
            user_name varchar(255),
            status boolean, 
            count integer, 
            tmp integer
        );
        """
        await self.pool.execute(sql)

