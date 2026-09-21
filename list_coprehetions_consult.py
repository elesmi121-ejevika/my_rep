# text = list(input().split())
# words_list = [len(word) for word in text]
# print(words_list)

# n = int(input())
# m = int(input())
# matrix = []
# for row in range(n):
#     matrix.append([0] * m)
# for row in matrix:
#     print(*row)


# s1 = list(map(int, input().split()))
# s2 = list(map(int, input().split()))
# summa = []
# for l1, l2 in zip(s1, s2):
#     summa.append(l1 + l2)
# print(summa)

# n = int(input())
# matrix = []
# for row in range(n):
#     matrix.append(list(map(int, input().split())))
# main_diagonal_list = []
# for index in range(n):
#     main_diagonal_list.append(matrix[index][index])
# print(main_diagonal_list)

n = int(input())
matrix = [[1 if i == j else 0 for i in range(n)] for j in range(n)]
for row in matrix:
    print(*row)