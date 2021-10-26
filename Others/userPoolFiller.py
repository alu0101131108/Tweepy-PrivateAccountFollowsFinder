import tweepy
import time
import pandas as pd

# Keys and tokens.
consumer_key="QdRbWGPs38mGey409MNxBg2ey"
consumer_secret="HHLKJEg1RBDiXHcPiKPsjOQwIE1yqV7CXaPPUIJbQSbzjmkYwF"
access_token="1369546171-yY2YLkcNVwTcK4GIg5iG0em582ApYgdkizBA0Zw"
access_token_secret="4jVUgXfi1o2m7k7rUEFq6PokpOfU000kgJmr9oG4I3ysn"

# OAuth.
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Consts and empty containers.
target1 = "saramambiche64"
target2 = "fisquit"

friendship = api.show_friendship(source_screen_name = target1, target_screen_name = target2)

A = friendship[0].screen_name
B = friendship[1].screen_name
if (friendship[0].followed_by and friendship[1].followed_by): 
    print(A, "mutuals", B)
elif (friendship[1].followed_by): 
    print(A, "follows", B)
elif (friendship[0].followed_by): 
    print(B, "follows", A) 
else:
    print("Non related")



