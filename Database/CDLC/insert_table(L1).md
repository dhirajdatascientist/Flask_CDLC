```
def insert_table():
    conn=connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO emp(id,username,email) VALUES (?,?,?)",("101","Sahil","sahil@gmail.com"))
    conn.commit()
    conn.close()
```