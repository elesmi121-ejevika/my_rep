# import pandas as pd
#
# salaries = pd.read_csv('salaries.csv', encoding='utf-8', sep=';')
# # print(salaries)
# max_salary = salaries["salary"].max()
# # print(max_salary)
# employee_max_salary = salaries[salaries["salary"] == max_salary]
# # print(type(employee_max_salary["name"]))
# max_employee = employee_max_salary.iloc[0]
# # print("max_employee: ", type(max_employee))
# # print("max_employee_max_salaries: ", type(employee_max_salary))
# # print(max_employee['name'])
# print(f"Сотрудник: {max_employee['name']} | Отдел: {max_employee['department']} | Оклад: {max_employee['salary']:.2f}")

import pandas as pd

prices = pd.read_csv('price_list.csv',
                     encoding='utf-8',
                     sep=','
                     )
prices['price'] = prices['price'].astype('Int64')
filtered_items = prices.loc[
    prices['price'].isna()
]

print(f"Пропусков цены: {len(filtered_items)}")
print("Артикулы:", ", ".join(filtered_items['item_code'].astype(str)))