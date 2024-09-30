import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    merged_df = pd.merge(visits, transactions, on='visit_id', how='left')
    no_transaction_visits = merged_df[merged_df['transaction_id'].isna()]
    result = no_transaction_visits.groupby('customer_id').size().reset_index    (name='count_no_trans')
    return result
