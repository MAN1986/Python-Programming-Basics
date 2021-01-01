## Game of Life
import random
def displayGrid():
    'This funtion should display the grid in 5x5 shape.'
    pass
def neighbors(r,c):
    '''This function will return a list of all neighbors of the cell
    provided as input argument as row=r and colum=c
    The output list will be a nested list, each inner list will be row and
    column number of each neighbor.
    Handle the cases of cells on sides and at corner'''
    pass

## Main Program ##
# print(chr(9650))  #Alive
# print(chr(9679))  #Dead
grid=a=[[chr(9679)]*5,[chr(9679)]*5,[chr(9679)]*5,[chr(9679)]*5,[chr(9679)]*5]
# displayGrid()

# Make 6 random cell alive 
n=list(range(1,26))
s=random.sample(n,6)
for i in s:
    c=(i%5)-1
    r=abs(i-1)//5
    grid[r][c]=chr(9650)
displayGrid()

# Next Generation Calculations
getDie=[]
getAlive=[]
for r in range(5):
    for c in range(5):
        n=neighbors(r,c) # Get the list of all neighbors
        # Conditions when cell will change the status
        if(grid[r][c]==chr(9650) and n.count(chr(9650))<2):
            getDie.append([r,c])
        elif(grid[r][c]==chr(9650) and n.count(chr(9650))>3):
            getDie.append([r,c])
        elif(grid[r][c]==chr(9679) and n.count(chr(9650))==3):
            getAlive.append([r,c])

# Cell status update
for i in getDie:
    grid[i[0]][i[1]]=chr(9679)
for i in getAlive:
    grid[i[0]][i[1]]=chr(9650)

print('__________')
displayGrid()