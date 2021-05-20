from typing import List, Union
import asyncio
import asyncpg
from asyncpg.pool import Pool
from database import config

class Data_comands:

    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        pool = await asyncpg.create_pool(user=config.PGUSER, host=config.ip,  database=config.PGDATABASE)
        self.pool = pool
    
    ###COMMANDS###

    async def add_user(self, user_id, user_name, status=False, count=0, tmp=0):
        sql = "INSERT INTO users (user_id, user_name, status, count, tmp) VALUES ($1, $2, $3, $4, $5)"
        await self.pool.execute(sql, user_id, user_name, status, count, tmp)

    async def sub_exist(self, user_id: int):
        sql = "SELECT * FROM users WHERE user_id = $1"
        return bool(await self.pool.fetchrow(sql, user_id))

    async def subscriptions_exist(self, user_id):
        sql = "SELECT status FROM users WHERE user_id = $1"
        return await self.pool.fetchrow(sql, user_id)

    async def add_counts(self, count, user_id):
        sql = "UPDATE users SET count = $1 where user_id=$2"
        await self.pool.execute(sql, count, user_id)

    async def get_counts(self, user_id):
        sql = 'SELECT count FROM users WHERE user_id = $1'
        return await self.pool.fetchrow(sql, user_id)

    async def setTrue(self, user_id):
        sql = "UPDATE users SET status = '1' where user_id = $1"
        await self.pool.execute(sql, user_id)

    async def setFalse(self, user_id):
        sql = "UPDATE users SET status = '0' where user_id = $1"
        await self.pool.execute(sql, user_id)

    async def countMinus(self, user_id):
        sql = "UPDATE users SET count=count-1 WHERE user_id=$1"
        await self.pool.execute(sql, user_id)

    async def getUsers(self):
        sql = "SELECT user_id FROM users WHERE count>='1'"
        return await self.pool.fetch(sql)

#################    COUNTS ############################

    async def tmpCount(self, tmp, user_id):
        sql = "UPDATE users SET tmp=$1 WHERE user_id=$2"
        await self.pool.execute(sql, tmp, user_id)

    async def getTmp(self, user_id):
        sql = "SELECT tmp FROM users WHERE user_id=$1"
        return await self.pool.fetchrow(sql, user_id)
