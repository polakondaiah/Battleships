s = "there is a cat with a cat"
words = s.split()
d = {}
for i in words:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
print(d)            