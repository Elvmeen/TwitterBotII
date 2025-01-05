import os
import tweepy
import requests
from dotenv import load_dotenv

# Load environment variables from the system's environment (or .env for local testing)
load_dotenv()

# Get Twitter API keys from environment variables
CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

# API authorization
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Create API object
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication Successful!")
except tweepy.TweepError as e:
    print(f"Error during Authentication: {e}")

# Fetching a random quote and posting it
url = "http://api.quotable.io/random"
response = requests.get(url, verify=False)
res = response.json()  # Parse JSON response directly
print(f"Quote fetched: {res['content']}")

try:
    tweet = api.update_status(res['content'])
    print(f"Successfully posted tweet: {tweet.text}")
except tweepy.TweepError as e:
    print(f"Error posting tweet: {e}")
