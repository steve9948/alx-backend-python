import aiomysql
import asyncio

# MySQL configuration
db_config = {
    "host": "localhost",
    "user": "your_username",
    "password": "your_password",
    "db": "test_db",
}

async def async_fetch_users():
    """Fetch all users from the MySQL database."""
    async with aiomysql.connect(**db_config) as conn:
        async with conn.cursor() as cursor:
            await cursor.execute("SELECT * FROM users")
            rows = await cursor.fetchall()
            print("All users:")
            for row in rows:
                print(row)
            return rows

async def async_fetch_older_users():
    """Fetch users older than 40 from the MySQL database."""
    async with aiomysql.connect(**db_config) as conn:
        async with conn.cursor() as cursor:
            await cursor.execute("SELECT * FROM users WHERE age > %s", (40,))
            rows = await cursor.fetchall()
            print("\nUsers older than 40:")
            for row in rows:
                print(row)
            return rows

async def fetch_concurrently():
    """Run both fetch operations concurrently."""
    results = await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users(),
    )
    print("\nFetched results concurrently:")
    return results

if __name__ == "__main__":
    # No separate setup script; direct script integration for database queries
    asyncio.run(fetch_concurrently())
