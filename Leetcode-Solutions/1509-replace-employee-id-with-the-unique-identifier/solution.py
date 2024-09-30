import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    rslt = pd.merge(employees,employee_uni,left_on='id',right_on='id',how='left')[['unique_id','name']]
    return rslt
