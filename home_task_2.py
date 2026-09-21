#text = input().split()
#target_word = ""
#for word in text:
#    if word.startswith("б"):
#        target_word = word
#        break
#if target_word != "":
#    print(target_word)
#else:
#    print("слов на б нет")
from itertools import count

#text = input().lower()
#ot_consonant = {'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я', 'ь', 'ъ'}
#counter = 0
#for letter in text:
#    if letter not in not_consonant:
#        counter = counter + 1
#print(counter)


#names = input()
#print(names.replace(" ", ","))


#numbers.txt = list(map(int, input().split()))
#total = 0
#for number in numbers.txt:
#    if number > 0:
#        total = total + number
#print(total)


fruits = input().split()
count = 1
max_length = 0
for fruit in fruits:
    if len(fruit) > max_length:
        max_length = len(fruit)
for fruit in fruits:
    i = max_length-len(fruit)
    print(f"{count}.", f"{fruit:>{max_length}}")
    count += 1
