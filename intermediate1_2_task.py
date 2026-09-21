#string =(input())
#print(string.replace(",", ""))

#fruits = ["яблоко", "банан", "киви", "ананас", "груша"]
#count = 1
#for fruit in fruits:
#    print(f"{count}.", fruit)
#    count = count + 1

names = input().split()
longest_name = ""
for name in names:
    if len(name) > len(longest_name):
        longest_name = name
print(longest_name)