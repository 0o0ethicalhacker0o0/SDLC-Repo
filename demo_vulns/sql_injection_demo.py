import sqlite3

def search_user(username):
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    # Intentionally insecure for demo purposes
    cur.execute("SELECT * FROM users WHERE username = '" + username + "'")
    return cur.fetchall()
