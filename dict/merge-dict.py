dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50} 

for i in dict2:
    dict1[i] = dict2[i]
print(dict1)
    
# 2 nd method to merge
dict1.update(dict2)
print(dict1)



dict3 = {**dict1, **dict2}
print(dict3)