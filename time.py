hour = int(input())
minutes = int(input())
if hour <= 23 and minutes <60:
    print("Корректное время")
else:
    print("Некорректное время")