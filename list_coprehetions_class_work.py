# text = input()
# my_list = text.split()
# count = 0
# for word in my_list:
#     if len(word) > 5:
#         count += 1
# print(count)
#
# numbers.txt = list(map(int,input().split()))
# target = int(input())
# for number in range(len(numbers.txt)-1,-1,-1):
#     if numbers.txt[number] == target:
#         numbers.txt.remove(numbers.txt[number])
# numbers.txt = list(map(str, numbers.txt))
# result = (' '.join(numbers.txt))
# print(result)

a = list(input().lower())
b = list(input().lower())
if sorted(a) == sorted(b):
    print("Да")
else:
    print("Нет")

