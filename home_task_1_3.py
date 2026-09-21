m = int(input())
n = int(input())
k = int(input())

if (((k % m == 0) and k >= m) or ((k % n == 0) and k >= n)) and k < m * n:
    print("Да")
else:
    print("Нет")
