```python
def delete():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM emp WHERE id=?",(101,))
    conn.commit()
    conn.close()
```