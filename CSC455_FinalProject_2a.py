import sqlite3
import time

conn=sqlite3.connect('csc455_FinalProject.db')
cur=conn.cursor()

q2ai = "SELECT id_str FROM Tweets WHERE id_str LIKE '%44%'"
start= time.time()
cur.execute(q2ai)
end = time.time()
print("Part 2ai")
print(cur.fetchall())
print("The query for Part 2ai took %s seconds" % round((end-start), 4))

q2aii = "SELECT COUNT(DISTINCT in_reply_to_user_id) FROM Tweets"
start= time.time()
cur.execute(q2aii)
end = time.time()
print("Part 2aii")
print(cur.fetchall())
print("The query for Part 2aii took %s seconds" % round((end-start), 4))
                     
q2aiii = "SELECT id_str FROM Tweets WHERE LENGTH(text) = (SELECT MAX(LENGTH(text)) FROM Tweets)"
start= time.time()
cur.execute(q2aiii)
end = time.time()
print("Part 2aiii")
print(cur.fetchall())
print("The query for Part 2aiii took %s seconds" % round((end-start), 4))

q2aiv = "SELECT screen_name, AVG(latitude), AVG(longitude) FROM Geo, User, Tweets WHERE id = user_id AND geoid = t_geoid GROUP BY screen_name"
start= time.time()
cur.execute(q2aiv)
end = time.time()
print("Part 2aiv")
print(cur.fetchall())
print("The query for Part 2aiv took %s seconds" % round((end-start), 4))

q2aiv = "SELECT screen_name, AVG(latitude), AVG(longitude) FROM Geo, User, Tweets WHERE id = user_id AND geoid = t_geoid GROUP BY screen_name"
start= time.time()
cur.execute(q2aiv)
end = time.time()
print("Part 2aiv")
print(cur.fetchall())
print("The query for Part 2aiv took %s seconds" % round((end-start), 4))

def rerun_query10(query):
    count = 1
    for count in range(1,10):
        count +=1
        cur.execute(query)

def rerun_query100(query):
    count = 1
    for count in range(1,100):
        count +=1
        cur.execute(query)

start = time.time()        
rerun_query10(q2aiv)
end = time.time()
print(cur.fetchall())
print("The query run 10 times for Part 2aiv took %s seconds" % round((end-start), 4))

start = time.time()        
rerun_query100(q2aiv)
end = time.time()
print(cur.fetchall())
print("The query run 100 times for Part 2aiv took %s seconds" % round((end-start), 4))