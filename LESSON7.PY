import psycopg

conn = psycopg.connect(
    host="192.168.90.44",
    dbname="LEO_NEOT_WF",
    user="postgres",
    password="Po84140188",
    port=5432
)

cur = conn.cursor() #準備執行 SQL

cur.execute("""
    SELECT
        SONO
    FROM LCDISSalesOrder
""")

rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()




#Python
#   ↓
#conn
#   ↓
#PostgreSQL
#   ↓
#cur
#   ↓
#執行 SQL