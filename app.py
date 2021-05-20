from loader import dt, db

async def on_startup(dp):
    await dt.create()
    print("Database created✅")
    await db.create()
    print("Database connected✅")
    await dt.create_table_user()
    print("Table user created✅")


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)


