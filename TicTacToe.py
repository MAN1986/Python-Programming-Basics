'''
Grid 3x3
Take slot from players
Fill the grid with X or O
Check Winning Condition
if Wins, annpunce the winner
if all slots are filled without winner, announce the Draw
'''
def displayGrid():
    print(f'{grid[0][0]} | {(grid[0][1])} | {(grid[0][2])}')
    print("----------")
    print(f'{grid[1][0]} | {(grid[1][1])} | {(grid[1][2])}')
    print("----------")
    print(f'{grid[2][0]} | {(grid[2][1])} | {(grid[2][2])}')
def fillSlot(s,mark):
    col=(s%3)-1
    row=((s-1)//3)
    if(grid[row][col] in list(range(1,10))):
        grid[row][col]=mark
        return True
    return False
def isWinner():
    if (grid[0][0]==grid[0][1]==grid[0][2] or 
        grid[1][0]==grid[1][1]==grid[1][2] or 
        grid[2][0]==grid[2][1]==grid[2][2] or 
        grid[0][0]==grid[1][0]==grid[2][0] or 
        grid[0][1]==grid[1][1]==grid[2][1] or 
        grid[0][2]==grid[1][2]==grid[2][2] or 
        grid[0][0]==grid[1][1]==grid[2][2] or 
        grid[2][0]==grid[1][1]==grid[0][2]):
        return True
    else:
        return False

## Main Program ##
grid=[[1,2,3],[4,5,6],[7,8,9]]
displayGrid()
blanks=9
while(True):
    f=False
    while(not f):
        print('Player 1 Turn')
        p1=int(input('Enter a slot to fill:'))
        f=fillSlot(p1,'X')
        if(not f):
            print('The slot is already filled.')
        if(f):
            blanks-=1
        displayGrid()
    if(isWinner()):
        print('Player 1 Wins!')
        break
    if(blanks==0):
        break
    f=False
    while(not f):
        print('Player 2 Turn')
        p2=int(input('Enter a slot to fill:'))
        f=fillSlot(p2,'O')
        if(not f):
            print('The slot is already filled.')
        if(f):
            blanks-=1
        displayGrid()
    if(isWinner()):
        print('Player 1 Wins!')
        break
    if(blanks==0):
        break

if(not isWinner()):
    print('Game Ended in Draw!')
