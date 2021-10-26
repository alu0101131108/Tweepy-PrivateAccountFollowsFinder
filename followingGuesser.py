import tweepy
import time
import pandas as pd

# Keys and tokens. (Hidden from repo for security reasons)
consumer_key=""
consumer_secret=""
access_token=""
access_token_secret=""

# OAuth.
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Consts and empty containers.
target = "saramambiche64"
scrappingTargets = [
    "SobranManito",
    "vj_ebooks",
    "akcbrising",
    "scoopidiwoop",
    "trankilicese",
    "rafwiko",
    "venadojorafa",
    "perricao",
    "__aguaviva",
    "gatofresi",
    "ibenesuela",
    "rual_iuuu",
    "Barrancondo",
    "love_____sosa",
    "fulldestrabado",
    "sebalyce_"
]
userPool = []
friendships = []
user_data = []
relation_data = []


# # Fill userPool with logged data from previous analized users.
# with open('scraplog.txt', 'r') as scrapfile:
#     for line in scrapfile:   
#         user = line[:-1]            # Remove \n which is the last character of each user.       
#         if (user not in userPool):
#             userPool.append(user)

# Scrap each scrapping target and fill user Pool. It also saves progress in file "scraplog.txt".
with open('scraplog.txt', 'a') as scrapfile:
    for scrTarget in scrappingTargets:
        try:
            users = tweepy.Cursor(api.followers, screen_name=scrTarget).items()
            while True:
                try:
                    user = next(users)
                except tweepy.TweepError:
                    time.sleep(60*15)
                    try:  
                        user = next(users)
                    except tweepy.TweepError:
                        print("Error scrapping:", user.screen_name)
                        continue
                except StopIteration:
                    break
                if (user.screen_name not in userPool) and not user.protected:
                    userPool.append(user.screen_name)
                    scrapfile.write('%s\n' % user.screen_name)
                    print("Scrapping from:", scrTarget, "> User:", user.screen_name)
        except tweepy.TweepError:
            print("Error with scrapping target:", scrTarget)
            continue


# Analize friendships between target and users from the Pool.
for user in userPool:
    try:
        friendships.append(api.show_friendship(source_screen_name = target, target_screen_name = user))
    except tweepy.TweepError as e:
        if (e.args[0][0]['code'] == 50):
            print('User was not found:', user)
            continue
        else:
            time.sleep(60*15) 
            try:
                friendships.append(api.show_friendship(source_screen_name = target, target_screen_name = user))
            except tweepy.TweepError:
                print("Error analizing friendship with:", user)
                continue
    print("Friendship analized between target and", user)

#Save and output results.
print("Saving results")
for fs in friendships:  
    if (fs[0].followed_by and fs[1].followed_by): 
        relation = "Mutual"
    elif (fs[1].followed_by): 
        relation = "Followed by"
    elif (fs[0].followed_by): 
        relation = "Follows"
    else:
        relation = "Non related"
    user_data.append(fs[1].screen_name)
    relation_data.append(relation)

df = pd.DataFrame({
    "User": user_data,
    "Relation": relation_data
    }) 

print("Done, exporting and showing results")
print("Users analized:", len(userPool))
df.to_csv("data_" + scrappingTargets[0] + ".csv")
print(df)





