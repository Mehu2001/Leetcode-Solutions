import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    own_articles = views[views['author_id']==views['viewer_id']]
    distinct_authors = own_articles['author_id'].unique()
    distinct_authors = sorted(distinct_authors)

    df = pd.DataFrame({'id': distinct_authors})

    return df
    
