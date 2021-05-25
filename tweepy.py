import tweepy
from TwitterOAuth import OAuthVerifier
def getuser(user):
	print(user.name)
	print(user.id)
def main():
	api = OAuthVerifier()
	user = api.me()
	getuser(user)
	name = (input())
	user = api.get_user(name)
	getuser(user)
if __name__ =='__main__':
	main()