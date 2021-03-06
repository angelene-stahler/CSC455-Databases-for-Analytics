import json
import sqlite3
import time

def run_sqlfile(file, cur):
	infile = open(file, "r")
	cmds = infile.read().split(";")	
	infile.close()
	for cmd in cmds:
		print("Running command: %s" % cmd.strip())
		try:
			cur.execute(cmd)
			print("Completed")
		except:
			print("Failed")

def get_record(dct, fields):
	record = []
	for field in fields:
		record.append(dct[field])
	return record

def batch_insert(cur, table, data):
	placeholders = ", ".join(["?" for x in range(len(data[0]))])	
	sql = "INSERT INTO %s VALUES (%s);" % (table, placeholders)	
	cur.executemany(sql, data)
	print("Finished loading data into %s." % table)	
    
def write_data(file, lst):
	out = open(file, "w")
	for row in lst:
		out.write("%s\n" % str(row))
	out.close()
	print("Finished writing to %s." % file)
    
def sanity_check(cur):
    cur.execute("SELECT COUNT(*) FROM Tweets;")
    print("\nTweets COUNT(*) Result: %s\n" % str(cur.fetchall()[0][0]))
    cur.execute("SELECT COUNT(*) FROM User;")
    print("User COUNT(*) Result: %s\n" % str(cur.fetchall()[0][0]))
    cur.execute("SELECT COUNT(*) FROM Geo;")
    print("Geo COUNT(*) Result: %s\n" % str(cur.fetchall()[0][0]))
       
def read_and_load_tweets(file, delimiter, tweet_fields, user_fields, cur, error_file, conn):
    tweets = open(file, "r")
    errors = []
    count = 0
    for tweet in tweets:
        try:
            tweets_dict = json.loads(tweet.decode('utf8'))
            if tweets_dict['geo'] is None:
                geoid = None
            else:
                geoid = tweets_dict['id_str']
                geotype = tweets_dict['geo']['type']
                latitude = tweets_dict['geo']['coordinates'][0]
                longitude = tweets_dict['geo']['coordinates'][1]
                try:
                    record = [geoid, geotype, latitude, longitude]
                    cur.execute("INSERT INTO Geo VALUES(?, ?, ?, ?);", record)
                except Exception as e:
                    pass
        except Exception as e:
            errors.append(tweet)
            continue
        
        try:
            record = get_record(tweets_dict['user'], user_fields)
            cur.execute("INSERT INTO User VALUES(?, ?, ?, ?, ?);", record)
        except Exception as e:
                    pass
        try:
            record = get_record(tweets_dict, tweets_fields)
            record.append(geoid)
            record.append(tweets_dict['user']['id'])
            cur.execute("INSERT INTO Tweets VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", record)
        except Exception as e:
                    pass


conn=sqlite3.connect('csc455_FinalProject.db')
cur=conn.cursor()

final_project_tables = "C:\\Users\Angelene\Documents\CSC455_FinalProject_1a.txt"
file = "C:\\Users\Angelene\Documents\FinalProject_tweets2.txt"
delimiter = '\n'
tweets_fields = ['created_at', 'id_str', 'text', 'source', 'in_reply_to_user_id', 'in_reply_to_screen_name', 'in_reply_to_status_id', 'retweet_count', 'contributors']
user_fields = ['id', 'name', 'screen_name', 'description', 'friends_count']
error_file = "C:\\Users\Angelene\Documents\FinalProject_errors2.txt"

run_sqlfile(final_project_tables, cur)
start = time.time()
read_and_load_tweets(file, delimiter, tweets_fields, user_fields, cur, error_file, conn)
end = time.time()
sanity_check(cur)
print("Reading and loading 500K tweets took %s seconds" % round((end-start), 4))