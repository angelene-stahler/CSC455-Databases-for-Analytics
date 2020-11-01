import codecs
import sqlite3

def generatePipeoutput(table,data):
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

conn = sqlite3.connect('csc455_FinalProject.db')
cur = conn.cursor()
rows = cur.execute("SELECT * FROM User").fetchall()
rows2 = cur.execute("SELECT * FROM Tweets").fetchall()
rows3 = cur.execute("SELECT * FROM Geo").fetchall()
conn.close()

out = codecs.open("C:\\Users\Angelene\Documents\FinalProject_UserTable.txt", "w", "utf8")
for row in rows:
    l = []
    for item in row:
        if type(item) is str:
            item = item.replace("'", "''")
            item = item.replace("&", "' || chr(38) || '")
        l.append(item)
    out.write(generatePipeoutput("User", l))


out.close()

out2 = codecs.open("C:\\Users\Angelene\Documents\FinalProject_TweetsTable.txt", "w", "utf8")
for row in rows2:
    l = []
    for item in row:
        if type(item) is str:
            item = item.replace("'", "''")
            item = item.replace("&", "' || chr(38) || '")
        l.append(item)
    out2.write(generatePipeoutput("Tweets", l))

out2.close()

out3 = codecs.open("C:\\Users\Angelene\Documents\FinalProject_GeoTable.txt", "w", "utf8")
for row in rows3:
    l = []
    for item in row:
        if type(item) is str:
            item = item.replace("'", "''")
            item = item.replace("&", "' || chr(38) || '")
        l.append(item)
    out3.write(generatePipeoutput("Geo", l))

out3.close()