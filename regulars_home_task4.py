# keys = input().split()
# values = input().split()
# new_dict = dict()
# for key, value in zip(keys, values):
#     new_dict[key] = value
# print(new_dict)

# n = int(input())
# telephone_directory = dict()
# for i in range(n):
#     name, number = input().split()
#     telephone_directory[name] = number
# target = input()
# result = telephone_directory.get(target)
# if result:
#     print(result)
# else:
#     print("Контакты не найдены")


# n = int(input())
# synonyms = dict()
# for i in range(n):
#     synonym1, synonym2 = input().split()
#     synonyms[synonym1] = synonym2
# word = input()
# for key, value in synonyms.items():
#     if word == value:
#         print(key)
#     if word == key:
#         print(synonyms[key])

# import re
#
# text = input()
# pattern_word = r"#[A-Za-zА-Яа-я0-9]+"
# matches_words = re.findall(pattern_word, text)
# for match in matches_words:
#     print(match)

# import re
#
# text = input()
# pattern_word = r"[A-Za-zА-Яа-я]+"
# clean_text = re.sub(r'[^\w\s-]', '', text)      #убираем из строки все кроме слов
# words = clean_text.lower().split()                          #создаем список из строки выше в нижнем регистре
# words_count = dict()                                        #пустой словарь, заполняем парой слово: количество в тексте
# for word in words:
#     if word in words_count:
#         words_count[word] += 1
#     else:
#         words_count[word] = 1
# compare = 0                                                 #переменные чтобы выяснить наибольшее число повторов
# target_key = ''
# for key, value in words_count.items():
#     if value > compare:
#         compare = value
#         target_key = key
# max_list = []                                               #создаем список из слов с максимальным количесивом повторов
# for key, value in words_count.items():
#     if value == compare:
#         max_list.append(key)
# max_list.sort()                                             #сортируем и выводим первое слово по алфавиту
# print((max_list[0]))


card = input()
visible = card[-4:]
if card[4].isdigit():
    mask = '*'*12
else:
    mask = ('*'*4 + card[4]) * 3
print(mask+visible)