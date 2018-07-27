import tweepy
from textblob import TextBlob

# Step 1 - Authenticate
consumer_key= 'YqrIzOKQXt5QSSpjB0KJR7bjb'
consumer_secret= 'LI1pLUqFuYQryxhko5SHfm1Ttg2xdjSRP2LA50FH1aqusp6la0'

access_token='1020959073213091840-2x45m50uFReth2SVpIN1J82HaSugbr'
access_token_secret='RQBkXhvPmnIg7WRRMQrTiCOvUEuh89Fu8KXwZUIbR6nMd'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
public_tweets = api.search('Trump')


filename = "tweet.csv"
f = open(filename,"w")
header = "tweet,reaction\n"
f.write(header)

#CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
#and label each one as either 'positive' or 'negative', depending on the sentiment 
#You can decide the sentiment polarity threshold yourself


for tweet in public_tweets:
    print(tweet.text)
    text=tweet.text
    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    polarity=analysis.sentiment.polarity
    if(polarity>=0):
        reaction='positive'
    else:
        reaction='negative'
    f.write(text.replace(',','|')+ "," +reaction+ "\n")
    print(analysis.sentiment)
    print("")
f.close()