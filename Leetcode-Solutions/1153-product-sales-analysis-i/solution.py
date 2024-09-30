import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    rslt = pd.merge(sales,product,left_on='product_id',right_on='product_id',how='left')[['product_name','year','price']]
    return rslt
