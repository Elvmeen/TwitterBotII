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

def post_quote():
    try:
        # Request a random quote from quotable API
        url = "https://api.quotable.io/random"
        response = requests.get(url)
        
        if response.status_code == 200:
            res = response.json()
            print(res)
            # Post the quote to Twitter
            api.update_status(res['content'])
        else:
            print(f"Error fetching quote. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
