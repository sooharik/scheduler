import sqlite3

base = sqlite3.connect('orders.db')
cur = base.cursor()

create_query = """CREATE TABLE IF NOT EXISTS holidays(
    id INT PRIMARY KEY,
    day TEXT,       
    HOL TEXT);
"""
cur.execute(create_query)
base.commit()
id = 1

with open("Каждый день - праздник.txt", encoding="utf-8") as f:
    for x in f:
        date, day = x.split(' - ')
        day = day[:-1]
        line = (id, date, day)
        print(line)
        insert_query = f'insert into holidays values (?, ?, ?);'
        cur.execute(insert_query, line)
        base.commit()
        id += 1
    else:
        cur.close() 

def bd(mounth):
    base = sqlite3.connect('orders.db')
    cur = base.cursor()
    cur.execute("select HOL from holidays where day=?;", (mounth,))
    return (cur.fetchone()[0])
print(bd("29 января"))

