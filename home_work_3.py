# a = int(input())
# b = int(input())
# while a <= b:
#     if a % 2 == 0:
#         print(a)
#     a += 1


# n = int(input())
# number = 1
# numbers.txt = [number for number in range(1, n + 1)]
# fact_numbers = []
# while number <= n-1:
#     card_number = int(input())
#     fact_numbers.append(card_number)
#     number += 1
# for number in numbers.txt:
#     if number not in fact_numbers:
#         print(number)

# n = int(input())
# i = 1
# for i in range(n+1):
#     print('*' * i)


# n = int(input())
# i = 1
# total_sum = 0
# intermediate_sum = 0
# for i in range(1,n+1):
#     intermediate_sum = i ** 2
#     total_sum += intermediate_sum
# print(total_sum)


# n = int(input())
# i = 1
# while i <= n:
#     print (f"{'#':>{i}}" + f"{' '*(n-1-i-1)}" + '#')
#     i += 1

n = int(input())
my_list = list(' '*n)
index = 0
while index < n:
    my_list[index] = "#"
    my_list[n-1 - index] = "#"
    print(''.join(my_list))
    my_list = list(' '*n)
    index +=1

