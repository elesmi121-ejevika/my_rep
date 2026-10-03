import numpy as np
import pandas as pd

from pandas_home_work_7_3 import subs

application = pd.read_csv('credit_applications.csv',
                          encoding='utf-8',
                          sep=',',
                          dtype={
                              'monthly_income': 'Float64',
                              'loan_amount': 'float'
                          }
                          )

# print(application)
# print('-' * 100)

dubious_applications = application.loc[
    ((application['loan_amount'] > 1000000) & (application['monthly_income'].isna())) |
    (application['age'] < 18) |
    (application['age'] > 100)
    ]

# print(dubious_applications)
# print('-' * 100)
print("Сомнительных заявок:", len(dubious_applications))
print("Первая заявка ID:", dubious_applications['app_id'].iloc[0])
