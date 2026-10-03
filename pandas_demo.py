import pandas as pd
# 1. Загрузка данных из CSV-файла
df = pd.read_csv("students_data.csv", index_col=0, sep=",")
# 2. Просмотр датасета
print(df)
print("-"*100)
# 3. Размерность таблицы
print("Размер датасета:", df.shape)
# 4. Полная сводка о типах и значениях
df.info()