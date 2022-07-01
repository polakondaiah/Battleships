import random
    row = random.randint(1,8)
    col = random.randint(1,8)
    hv = random.randint(0,1)
    if hv == 0: 
        ship = [[row,col-1],[row,col],[row,col+1]]   
    else:
        ship = [[row-1,col],[row,col],[row+1,col]]
    return ship    