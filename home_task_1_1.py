a = int(input())
b = int(input())
c = int(input())

p = a + b + c
hp = p / 2
s  = (hp * (hp - a) * (hp - b) * (hp - c)) ** (1 / 2)
print(p)
print(format(s, ".2f"))
