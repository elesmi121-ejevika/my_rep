# words = input().lower().split()
# count_words = {}
# for word in words:
#     if word in count_words:
#         count_words[word] += 1
#     else:
#         count_words[word] = 1
# for word in count_words:
#     print(f"{word}: {count_words[word]}")

# grades = {
#     "Анна": 5,
#     "Иван": 4,
#     "Мария": 5,
#     "Петр": 3,
#     "Елена": 4,
# }
# students_marks = {}
# for name, mark in grades.items():
#     if mark in students_marks:
#         students_marks[mark].append(name)
#     else:
#         students_marks[mark] = [name]
# print(students_marks)


n = int(input())
candidates = {}
for _ in range(n):
    name, value = input().split()
    value = int(value)
    if name in candidates:
        candidates[name] += value
    else:
        candidates[name] = value
max_value = 0
max_score_name = ''
for name, value in candidates.items():
    if candidates[name] > max_value:
        max_value = candidates[name]
        max_score_name = name
print(f"{max_score_name} {max_value}")
