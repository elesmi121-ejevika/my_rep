# num = int(input())
# if num % 3 == 0 and num % 5 != 0:
#     print("Foo")
# if num % 5 == 0 and num % 3 != 0:
#     print("Bar")
# if num % 3 == 0 and num % 5 == 0:
#     print("Foobar")


x = int(input())
y = int(input())
xr = int(input())
yr = int(input())
r = int(input())
l = ((x - xr) ** 2 + (y - yr) ** 2) ** 0.5
if l <= r:
    print("Да")
else:
    print("Нет")
