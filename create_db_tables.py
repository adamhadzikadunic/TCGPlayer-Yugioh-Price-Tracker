
from db_conn import conn


def create_db_tables():
    cur = conn.cursor()
    
    # for each set
    cur.execute("CREATE TABLE IF NOT EXISTS set (id INT PRIMARY KEY, name TEXT, setCode TEXT)")

    # for each card in the set
    cur.execute("CREATE TABLE IF NOT EXISTS card (id SERIAL PRIMARY KEY, name TEXT, setId INT REFERENCES set(id), rarity TEXT, edition TEXT)")

    # for each card's price
    cur.execute("CREATE TABLE IF NOT EXISTS price (id serial PRIMARY KEY,  marketPrice MONEY, lowPrice MONEY, midPrice MONEY, highPrice MONEY)")

    conn.commit()
    cur.close()

