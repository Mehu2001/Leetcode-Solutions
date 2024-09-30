import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    rslt = tweets[tweets['content'].str.len()>15]['tweet_id']
    df = pd.DataFrame(rslt)
    return df
