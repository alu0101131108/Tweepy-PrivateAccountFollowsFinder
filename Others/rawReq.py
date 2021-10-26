import requests
from requests_oauthlib import OAuth1
API_KEY="QdRbWGPs38mGey409MNxBg2ey"
API_SECRET="HHLKJEg1RBDiXHcPiKPsjOQwIE1yqV7CXaPPUIJbQSbzjmkYwF"
ACCESS_TOKEN="1369546171-yY2YLkcNVwTcK4GIg5iG0em582ApYgdkizBA0Zw"
ACCESS_TOKEN_SECRET="4jVUgXfi1o2m7k7rUEFq6PokpOfU000kgJmr9oG4I3ysn"
url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
auth = OAuth1(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

requests.get(url, auth=auth)


r = requests.get('https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=arepera23&count=20', auth=auth)
for tweet in r.json():
    print(tweet['text'])




