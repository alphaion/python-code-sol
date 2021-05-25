import tweepy
from TwitterOAuth import OAuthVerifier
def getUserFollowers(api):
    print('\nFollowers')
    for follower in api.followers():
        print(follower.screen_name)
def getUserFriends(api):
    print('\nFriends')
    for friend in api.friends():
        print(friend.screen_name)
def getUserTweets(api):
    print('\nTweets')
    for tweet in api.user_timeline():
        print(tweet.text)
def main():
    api = OAuthVerifier()
    getUserFollowers(api)
    getUserFriends(api)
    getUserTweets(api)
if __name__ =='__main__':
    main()