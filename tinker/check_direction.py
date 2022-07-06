def isHorizontal(ship):
    ship.sort()
    if ship[0][0] == ship[1][0] and ship[1][0] == ship[2][0]:
        if (ship[0][1]+1) == (ship[1][1]) and (ship[1][1]+1) == (ship[2][1]):
            return True
        else:
            return False
    else:
        return False
    
def isVertical(ship):
  #  for i in range(len(ship))
    ship.sort()
    if ship[0][1] == ship[1][1] and ship[1][1] == ship[2][1]:
        if (ship[0][0]+1) == (ship[1][0]) and (ship[1][0]+1) == (ship[2][0]):
            return True
        else:
            return False
    else:
        return False
