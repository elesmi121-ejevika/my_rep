# def is_strong_password(password):
#     import re
#     template = r"(?=.*[A-ZА-ЯЁ])(?=.*[a-zа-яё])(?=.*\d).{8,}"
#     result = bool(re.findall(template, password))
#     return result
#
# is_strong_password(input())

# summa = 0
# length = 0
# with open("numbers.txt", "r", encoding="utf-8") as f:
#     for line in f:
#         summa += int(line.strip())
#         length += 1
# print(f"{summa} {summa/length:.2f}")



# summa = 0
# maximum = 0
# with open("sold.txt", "r", encoding="utf-8") as file:
#     first_line = file.readline()
#     first_line_list = first_line.strip().split()
#     minimum = float(first_line_list[0])
#     file.seek(0)
#     for line in file:
#         for price in list(map(float, line.strip().split())):
#             summa += float(price)
#             if price > maximum:
#                 maximum = price
#             if price < minimum:
#                 minimum = price
#     print(f"{summa:.2f}")
#     print(maximum)
#     print(minimum)

# def get_word_stats (word: str):
#     consonant_num = 0
#     vowel_num = 0
#     for char in word:
#         if char.lower() in 'аеёиоуыэюя':
#             vowel_num += 1
#         if char.lower() in 'бвгджзйклмнпрстфхцчшщ':
#             consonant_num += 1
#     return len(word), vowel_num, consonant_num
#
# print(get_word_stats("Экзамен"))


# with open("salaries.txt", "r", encoding="utf-8") as file:
#     next(file)
#     for_write = []
#     for line in file.readlines():
#         surname = line.split()[0].strip()
#         name_first_letter = line.split()[1][0].strip() + "."
#         patronymic_first_letter = line.split()[2][0].strip() + "."
#         if int(line.split()[3]) > 60000:
#             for_write.append(f"{surname} {name_first_letter}{patronymic_first_letter}\n")
# with open("highly_paid.txt", "w", encoding="utf-8") as file:
#     file.writelines(for_write)

s1 = "aaaabbcccccdddggggggggggeeeeeeetttttt"

def rle_encode(s):
    prev_char = s[0]
    count = 0
    result = ''
    for char in s:
        if char != prev_char:
            result += f"{count}{prev_char}"
            count = 0
        prev_char = char
        count += 1
    result += f"{count}{prev_char}"
    return result

print(rle_encode(s1))
print(s1)