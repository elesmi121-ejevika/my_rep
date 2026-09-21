cost = int(input("Стоимость покупки: "))
if cost > 1000:
    cost = cost * 0.85
else:
    cost = cost
print("Итоговая цена: ", cost)
