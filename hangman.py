# Hang Man Game
import random
def updateGuessWord(w,a):
    wList=list(w)
    indices=[i for i in range(len(word)) if word[i].lower()==a.lower()]
    for i in indices:
        wList[i]=a.upper()
    return (''.join(wList))

country=['Pakistan','Japan','Turkey','India','England']
sport=['Cricket','Football','Hockey','Basketball','Golf']
animal=['Horse','Tiger','Monkey']
allWords=[country,sport,animal]
category=['Country','Sports','Animal']
a=random.randint(0,len(category)-1)
print(f'It is a name of a {category[a]}')
word=random.choice(allWords[a])
guessWord='-'*len(word) #--------
print(guessWord)
turns=6
guessedAlphabets=[]
while(turns>=1):
    a=input(f'Select Alphabet ({turns} Turns left):')
    if(a.lower() in guessedAlphabets):
        print('You already selected this alphabet.')
    elif(a.lower() in word.lower()):
        guessWord=updateGuessWord(guessWord,a)
        guessedAlphabets.append(a.lower())
        print(guessWord)
        if(guessWord==word.upper()):
            print('Congratulations!')
            break
    else:
        guessedAlphabets.append(a.lower())
        print('Wrong Guess!')
        turns-=1
        if(turns==0):
            print('Turns over! You Lost!')s