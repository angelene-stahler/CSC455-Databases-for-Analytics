import codecs

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
    sql = "INSERT INTO %s VALUES (%s);\n" % (table, ", ".join(data))
    return sql

rows = open("C:\\Users\Angelene\Documents\FinalProject_tweets2.txt", "r")
out = codecs.open("C:\\Users\Angelene\Documents\FinalProject_inserts3.sql", "w", "utf8")
for row in rows:
    row = row.split('\n')
    l = []
    for item in row:
        if type(item) is str:
            item = item.replace("'", "''")
            item = item.replace("&", "' || chr(38) || '")
        l.append(item)  
    out.write(generateInsert("User", l))

