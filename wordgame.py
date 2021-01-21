## Word Game ##
## LOST --> SLOT, LOTS
from itertools import permutations
import words
while(True):
    w=words.genWord()
    # print(w)
    allPoss=[''.join(i) for i in list(permutations(list(w)))]
    allPoss=list(set(allPoss))
    # print(allPoss)
    validPoss=[i for i in allPoss if i in words.words and i!=w]
    # print(validPoss)
    if(len(validPoss)>=2):
        break
print(f'The word is: {w}')
total=len(validPoss)
print(f'Make {len(validPoss)} words form it.')
count=0
while(count<total):
    s=input('Enter word:')
    if(s in validPoss):
        print('Good Job')
        validPoss.remove(s)
        count+=1
        if(count!=total):
            print(f'{total-count} more words to create.')
    else:
        print('That is not a valid word.')
print('You completed all words.')