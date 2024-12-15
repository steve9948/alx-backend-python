import aiosqlite
import asyncio

# Specify the database file
DB_FILE = "test_db.db"  # Ensure this matches the actual SQLite database file path

async def async_fetch_users():
    """Fetch all users from the database."""
    async with aiosqlite.connect(DB_FILE) as db:
        async with db.execute("SELECT * FROM users") as cursor:
            rows = await cursor.fetchall()
            print("All users:")
            for row in rows:
                print(row)
            return rows

async def async_fetch_older_users():
    """Fetch users older than 40 from the database."""
    async with aiosqlite.connect(DB_FILE) as db:
        async with db.execute("SELECT * FROM users WHERE age > ?", (40,)) as cursor:
            rows = await cursor.fetchall()
            print("\nUsers older than 40:")
            for row in rows:
                print(row)
            return rows

async def fetch_concurrently():
    """Run both fetch operations concurrently."""
    results = await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )
    print("\nFetched results concurrently:")
    return results

if __name__ == "__main__":
    asyncio.run(fetch_concurrently())