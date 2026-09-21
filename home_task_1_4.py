k = int(input())

while k > 0:
    if (k % 3 == 0 or k % 5 == 0):
        print("Да")
        break
    elif k in (1, 2, 4, 7):
        print("Нет")
        break
    elif k <= 0:
        print ("Нет")
    else:
        k -= 5