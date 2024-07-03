import tweepy
import json

def crawl():
    # Authentication
    api = None
    with open('auth.txt', 'r') as authFile:
        btoken = authFile.readline()
        api = tweepy.Client(btoken)

    # Read the list of accounts / hashtags
    crawllist = list()
    with open('target.txt', 'r') as targetFile:
        name,prop,num = targetFile.readline().split(',')
        crawllist.append((name, prop, num))

    # Start Crawling
    for name, prop, num in crawllist:
        if prop == 0:
            # Account Handler
            tweets = api.get_users_tweets(name, max_results=num)
        else:
            # Hashtag
            query = '#' + name
            tweets = api.search_recent_tweets(query, max_results=num)
        # Store the tweets
        fname = 'original/' + name + '.json'
        with open(fname, 'w') as storeFile:
            json.dump(tweets, storeFile)