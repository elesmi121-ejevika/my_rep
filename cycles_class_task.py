# n = int(input())
# text = "Я учу питон"
# while n > 0:
#     print(text)
#     n -= 1


# a = int(input())
# b = int(input())
# while a <= b:
#     if a % 2 == 0:
#         print(a)
#     a += 1

# n = int(input())
# summa = 0
# for i in range(n):
#     if i % 2 == 0:
#         summa += i
# print(summa)

num = int(input())
i = 2
flag = False
while i < num-1:
    if num % i == 0:
        print(i)
        flag = True
    i+=1
if flag == False:
    print("Число простое")