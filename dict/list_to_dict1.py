keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# empty dictionary
res1_dict = dict()

for i in range(len(keys)):
    res1_dict.update({keys[i]: values[i]})
print(res1_dict)