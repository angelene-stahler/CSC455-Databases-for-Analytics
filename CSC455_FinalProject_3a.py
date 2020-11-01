import codecs
import sqlite3

def generateInsert(table,data):
    for i in range (len(data)):
        if data[i] is None:
            data[i] = "NULL"
        elif type(data[i]) in (str,bytes):
            data[i] = "'%s'" % data[i]
        elif type(data[i]) is int:
            data[i] = str(data[i])
        else:
            return "WARNING! We have a new data type."
    sql = "| ".join(data)
    return sql

conn = sqlite3.connect("csc455_FinalProject.db")
cur = conn.cursor()
rows = cur.execute("SELECT * FROM User").fetchall()


out = codecs.open("C:\\Users\Angelene\Documents\FinalProject_inserts.sql", "w", "utf8")
for row in rows:
    l = []
    for item in row:
        if type(item) is str:
            item = item.replace("'", "''")
            item = item.replace("&", "' || chr(38) || '")
        user_id =cur.execute("SELECT id FROM User").fetchall()
        for char in user_id:
            unique_id = 0
            n = 0
            n += 1
            if char is int:
                char = chr(ord('a')+n)
                unique_id.append(char)
            else:
                continue
        l.append(item)  
    l.append(unique_id)
    out.write(generateInsert("User", l))

conn.close()
out.close()

