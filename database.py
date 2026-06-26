import sqlite3

conn = sqlite3.connect("linkverse.db", check_same_thread=False)

conn.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    username TEXT,
    balance REAL DEFAULT 0
)
""")
conn.commit()


def add_user(user_id, username):
    cur = conn.cursor()
    cur.execute(
        "INSERT OR IGNORE INTO users (user_id, username) VALUES (?, ?)",
        (user_id, username)
    )
    conn.commit()
    cur.close()


def get_balance(user_id):
    cur = conn.cursor()
    cur.execute(
        "SELECT balance FROM users WHERE user_id=?",
        (user_id,)
    )
    result = cur.fetchone()
    cur.close()

    if result:
        return result[0]
    return 0