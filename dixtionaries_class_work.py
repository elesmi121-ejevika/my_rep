item = {
    "title": "Кеды",
    "color": "black",
    "size": 42
    }
item["title"] = "Кепка"
print(item)

words = input().lower().split()
words_count = {}
for word in words:
    if word in words_count:
        words_count[word] += 1
    else:
        words_count[word] = 1
for key, value in words_count.items():
    print(f"{key}: {value}")
student_marks = {
    "Анна": 4,
    "Петр": 3,
    "Алекс": 5,
    "Иван": 5,
    "Ольга": 4,
    "Илья": 4,
    "Василий": 3,
}
marks = {}
for name, mark in student_marks.items():
    if mark in marks:
        marks[mark].append(name)
    else:
        marks[mark] = [name]
print(marks)