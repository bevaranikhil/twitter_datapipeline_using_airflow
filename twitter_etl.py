import tweepy
import pandas as pd 
import json
from datetime import datetime
import s3fs 
import boto3
from io import StringIO

def run_twitter_etl():

    API_KEY = 'your_api_key'
    API_SECRET_KEY = 'your_api_secret_key'
    ACCESS_TOKEN = 'your_access_token'
    ACCESS_TOKEN_SECRET = 'your_access_token_secret'

    # AWS S3 credentials 
    aws_access_key_id = 'YOUR_ACCESS_KEY'
    aws_secret_access_key = 'YOUR_SECRET_KEY'

    #AWS S3 object storage information 
    S3_BUCKET_NAME = 'your_s3_bucket_name'
    S3_FILE_NAME = 'twitter_data.csv'


    # Twitter authentication
    auth = tweepy.OAuthHandler(access_key, access_secret)   
    auth.set_access_token(consumer_key, consumer_secret) 

###extration###
    # # # Creating an API object 
    api = tweepy.API(auth)
    tweets = api.user_timeline(screen_name='@viratkohli', 
                            # 200 is the maximum allowed count
                            count=200,
                            include_rts = False,
                            # Necessary to keep full_text 
                            # otherwise only the first 140 words are extracted
                            tweet_mode = 'extended'
                            )
###Transformation###
    list = []
    for tweet in tweets:
        text = tweet._json["full_text"]

        refined_tweet = {"user": tweet.user.screen_name,
                        'text' : text,
                        'favorite_count' : tweet.favorite_count,
                        'retweet_count' : tweet.retweet_count,
                        'created_at' : tweet.created_at}
        
        list.append(refined_tweet)

    df = pd.DataFrame(list)

###Loading###
    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)
    
    # Upload CSV to S3
    s3_client = boto3.client('s3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
    )
    s3_client.put_object(
        Bucket=S3_BUCKET_NAME,
        Key=S3_FILE_NAME,
        Body=csv_buffer.getvalue()
    )
    
