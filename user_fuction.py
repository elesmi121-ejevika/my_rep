# def my_abs(num):
#     if num >= 0:
#         return num
#     else:
#         return num + 2 * (-num)
#
#
# result = my_abs(float(input()))
# print(result)
#
# def my_max(a, b):
#     if a > b:
#         return a
#     return b
#
#
# n1 = float(input())
# n2 = float(input())
# result = my_max(n1, n2)
# print(result)


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

n = int(input())
print(is_even(n))
