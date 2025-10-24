from DAL import init_db, DB_PATH
import sqlite3

def main():
    init_db()
    conn = sqlite3.connect(DB_PATH)
    cur = conn.execute("SELECT name, sql FROM sqlite_master WHERE type='table' AND name='projects';")
    row = cur.fetchone()
    if row:
        print('FOUND')
        print(row[1])
    else:
        print('NOT FOUND')
    conn.close()

if __name__ == '__main__':
    main()
