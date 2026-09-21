# a = int(input())
# b = int(input())
# p = 2 * a + 2 * b
# s = a * b
# print(p)
# print(s)

# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# l = ((x1 - x2)**2 + (y1 - y2)**2) ** 0.5
# print(l)

# number = int(input())
# if 100 <= abs(number) <= 999:
#     print("Да")
# else:
#     print("Нет")


number = int(input())
if abs(number) % 10 == 5:
    print("Да")
else:
    print("Нет")