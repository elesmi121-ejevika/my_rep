import re
pattern = r"[.!,:—()«»\"']"
text = "Утром Аня ела аппетитное яблоко, а Игорь, — апельсин."
cleared_text = text.replace(r"[.!,:—()«»\"']", "")
words = text.split()
new_text = []
print(cleared_text) #список слов из теста
vowels = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
for word in words:
    if word[0].lower() in vowels:
        new_text.append(word)
print(new_text)
print(",".join(filter(str.isalnum, new_text))) #список слов на гласную через запрятую без знаков препинания


pattern = r"[.!,:—()«»\"']"
#pattern = r"[!\"#$%&'()*+,-.—/:;<=>?@[\\\]_`{|}~]"
matches = re.findall(pattern, text)
#pattern = r"[^\w\s..]+"
#matches = re.findall(pattern, text)

print("список всех знаков препинания", matches) #список всех знаков препинания
unique_matches = []
for symbol in matches:
    if symbol not in unique_matches:
        unique_matches.append(symbol)
print(*unique_matches)
