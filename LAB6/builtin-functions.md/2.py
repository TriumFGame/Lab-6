t = input()
upper = 0
lower = 0
for i in t:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower += 1
print(upper, lower)