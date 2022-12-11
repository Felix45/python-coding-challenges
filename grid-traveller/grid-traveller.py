'''
  Say you are a traveller on 2 dimension grid. You begin in the
  top-left corner and your goal is to travel to the bottom-right
  corner. You may only move down or right. In how many ways can
  you travel to the goal on a grid with dimensions m * n

'''

def grid_traveller(m, n):
  if m == 1 and n == 1:
    return 1
  if m == 0 or n == 0:
    return 0
  
  return grid_traveller(m-1, n) + grid_traveller(m, n-1)

print(grid_traveller(0,0))
print(grid_traveller(1,1))
print(grid_traveller(2,1))
print(grid_traveller(3,2))