def column(A,c):
    col=[]
    for rowIndex in range(len(A)):
        col.append(A[rowIndex][c])
    return col
# marks=[]
subjects=['Calculus','Algebra','Programming','Electronics','Statistics']
# for row in range(10):
#     a=[]
#     print(f'Enter the marks of Student-{row+1}')
#     for col in range(5):
#         m=eval(input(f'{subjects[col]}:'))
#         a.append(m)
#     marks.append(a)
# print(marks)

marks=[
[89,91,68,88,93],
[78,79,87,78,67],
[94,83,69,79,82],
[67,78,77,82,66],
[88,82,87,77,69],
[93,55,90,82,67],
[76,69,86,75,94],
[66,77,67,64,83],
[82,79,83,71,68],
[59,83,88,84,79]]



r=int(input('Enter the roll number: '))
avg=sum(marks[r-1])/len(marks[r-1])
maxMarks=max(marks[r-1])
minMarks=min(marks[r-1])
maxMarksIndex=marks[r-1].index(maxMarks)
minMarksIndex=marks[r-1].index(minMarks)
maxMarksSub=subjects[maxMarksIndex]
minMarksSub=subjects[minMarksIndex]
print(f'The average marks of roll number {r} are: {avg}')
print(f'Roll number {r} got max marks {maxMarks} in {maxMarksSub}')
print(f'Roll number {r} got min marks {minMarks} in {minMarksSub}')