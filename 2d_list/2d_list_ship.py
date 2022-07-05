import random
x = random.randint(1,8)
y = random.randint(1,8)
h_or_v = random.randint(0,1)
ship = []
if h_or_v == 0:
   ship = [[x,y-1],[x,y],[x,y+1]]
else:
   ship = [[x-1,y],[x,y],[x+1,y]]
print(ship)    