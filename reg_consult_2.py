text = input()
numbers = list(map(int, text.split()))
result = 0
numbers_dict = dict()
for number in numbers:
    if number not in numbers_dict:
        numbers_dict[number] = 1
    else:
        numbers_dict[number] += 1
for key, value in numbers_dict.items():
    if value > 1:
        result = key
        break
if result == 0:
    print("None")
if result != 0:
    i = 0
    while i < len(numbers):
        if numbers[i] == result:
            print(f"{numbers[i]} {i}")
            break
        i += 1