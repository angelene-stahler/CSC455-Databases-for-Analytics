import urllib
import time
import codecs

def write_data(file, lst):
	out = codecs.open(file, "w", "utf8")
	for row in lst:
		out.write("%s\n" % str(row))
	out.close()
	print("Finished writing to %s." % file)
    
def write_tweets_to_text_file(URL, delimiter):
    tweets = urllib.request.urlopen(URL)
    tweets_dict = []
    errors = []
    count = 0
    for tweet in tweets:
        count += 1
        if count == 500000:
            break
        try:
            tweets_dict.append(tweet)
        except Exception as e:
            errors.append(tweet)
            continue
        			
    write_data(tweets_file, tweets_dict)
    write_data(error_file, errors)
    print("Finished reading and writing data to files.")


URL = "http://rasinsrv07.cstcis.cti.depaul.edu/CSC455/OneDayOfTweets.txt"
delimiter = '\n'
error_file = "C:\\Users\Angelene\Documents\FinalProject_errors2.txt"
tweets_file = "C:\\Users\Angelene\Documents\FinalProject_tweets2.txt"

start= time.time()
write_tweets_to_text_file(URL, delimiter)
end = time.time()
print("Writing 500K tweets to text file took %s seconds" % round((end-start), 4))