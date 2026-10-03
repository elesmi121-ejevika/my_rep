import pandas as pd

subs = pd.read_csv('subscriptions.csv',
                   encoding='utf-8',
                   sep=','
                   )
subs['is_active'] = subs['is_active'].fillna(False).astype(bool)

active_subs = subs.loc[
    subs['is_active'] == True
    ]
print("Активных подписок:", len(active_subs))
