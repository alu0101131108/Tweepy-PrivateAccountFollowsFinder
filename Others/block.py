#KEYS AND TOKENS
#API key: QdRbWGPs38mGey409MNxBg2ey
#API Secret key: HHLKJEg1RBDiXHcPiKPsjOQwIE1yqV7CXaPPUIJbQSbzjmkYwF
#Bearer Token: AAAAAAAAAAAAAAAAAAAAABzIMQEAAAAAiGorNIQZH3iqzqL80xaLmV4hNwI%3DBuozbewOPN2GmbUnKuYG5umYvtAQ45sOU09tSCDvy2PxIfN64L
#Access Token: 1369546171-yY2YLkcNVwTcK4GIg5iG0em582ApYgdkizBA0Zw
#Access Token Secret: 4jVUgXfi1o2m7k7rUEFq6PokpOfU000kgJmr9oG4I3ysn



# sample @'s
# luida = 'arepera23'
# berto = 'cardi_bii'
# sara = 'saramambiche64'
# yop = 'sebalyce_'
# cr7 = 'Cristiano'
# nati = 'nathypeluso'
# awa = 'babyLaCuesta'



#TWEEPY TEMPLATE
# import tweepy
# import time

# consumer_key="QdRbWGPs38mGey409MNxBg2ey"
# consumer_secret="HHLKJEg1RBDiXHcPiKPsjOQwIE1yqV7CXaPPUIJbQSbzjmkYwF"
# access_token="1369546171-yY2YLkcNVwTcK4GIg5iG0em582ApYgdkizBA0Zw"
# access_token_secret="4jVUgXfi1o2m7k7rUEFq6PokpOfU000kgJmr9oG4I3ysn"

# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)

# api = tweepy.API(auth)



#GET FRIENDSHIP INFO
# friendship = api.show_friendship(source_screen_name = awa, target_screen_name = sara)

# A = friendship[0].screen_name
# B = friendship[1].screen_name
# if (friendship[0].followed_by and friendship[1].followed_by): 
#     print(A, "mutuals", B)
# elif (friendship[1].followed_by): 
#     print(A, "follows", B)
# elif (friendship[0].followed_by): 
#     print(B, "follows", A) 
# else:
#     print("Non related")



#GET FOLLOWERS WITH LIMIT HANDLING
#users = tweepy.Cursor(api.followers, screen_name=target).items()

#while True:
#    try:
#        user = next(users)
#    except tweepy.TweepError:
#        time.sleep(60*15)
#        user = next(users)
#    except StopIteration:
#        break
#    print("@" + user.screen_name)