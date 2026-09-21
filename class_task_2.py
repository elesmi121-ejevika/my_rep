#string = "питон, ПИТОН,Питон,   питон"
#string = "яблоко, груша, Яблоко, банан, груша"
#string = input().lower()
#string = string.replace(" ", "")
#uniq_fruits =  set(string.split(','))
#print(len(uniq_fruits))

#numbers.txt = list(map(int, input().split()))
#numbers.txt.sort()
#print(sum(numbers.txt[-3:]))


str1 = list(map(int, input().split()))
str2 = list(map(int, input().split()))
numbers1 = list(map(int, str1))
numbers2 = list(map(int, str2))
uniq_numbers1 = set(numbers1)
uniq_numbers2 = set(numbers2)
uniq_numbers1_2 = uniq_numbers1 - uniq_numbers2
result = ""
result_list = list(uniq_numbers1_2)
for number in result_list:
    result += str(number) + " "
result = result.strip()
print(result)
