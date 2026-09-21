import re

text = input()
words = text.split()
pattern_word = r"[A-Za-zА-Яа-я]+"
clean_word = re.sub(r'[^\w\s-]', '', words[0])
print(clean_word)
template_words = r"\b([A-Za-zА-Яа-я]{1,2})[-A-Za-zА-Яа-я]*"
result = re.findall(template_words, text)
print(*result)


# import re
# text = input()
# ### pattern_symbols = r"[.!,:—()«»\"']"
# pattern_words = r"[A-Za-zА-Яа-я]+"
# matches_words = re.findall(pattern_words, text)
# new_text = []
# vowels = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
# for word in matches_words:
#     if word[0].lower() in vowels:
#         new_text.append(word)
# print(",".join(new_text))
### matches_symbols = re.findall(pattern_symbols, text)
### unique_matches = []
### for symbol in matches_symbols:
###     if symbol not in unique_matches:
###         unique_matches.append(symbol)
### print(*unique_matches)


# import re
# text = input()
# pattern = r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"
# matches_words = re.findall(pattern, text)
# for match in matches_words:
#     print(match)




