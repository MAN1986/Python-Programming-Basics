import csv
def calcGPA(s):
    num=0
    den=0
    for k,v in s['Courses'].items():
        num+=subjects[k]*gDict[v]
        den+=subjects[k]
    return num/den
courses=['DLD','CP','ED','VCA','EM']
with open('studentsData.csv','r') as f:
    r=csv.DictReader(f)
    data=[]
    d={}
    for rec in r:
        d={}
        for k,v in rec.items():
            if(k in ['Reg','Name','Sec']):
                d[k]=v
            if (k in courses and v!='NR'):
                if ('Courses' not in d):
                    d['Courses']={k:v}
                else:
                    d['Courses'][k]=v
        data.append(d)

#Task-1
# Sort the list based on number of courses registered by student
# If the number is same, sort them on the basis of Reg.
# a=sorted(data,key=lambda s:(len(s['Courses']),s['Reg']))
# Then generate a list of just the Reg from sorted list
# print([s['Reg'] for s in a])



#Task-2
# We have the courses list (line 2 of the program)
# Detail of Credit Hours of the Courses is given below
# courses=['DLD','CP','ED','VCA','EM']
CH=[3,2,3,3,2]
# We can create a Dictionary of subjects as:
subjects=dict(zip(courses,CH)) # Keys=CourseName value=CH
# Here is details of letter grades as Dictionary
gLetter=['A+','A','A-','B+','B','B-','C+','C','C-','D+','D','F']
gPoints=[4.0,4.0,3.7,3.3,3.0,2.7,2.3,2.0,1.7,1.3,1.0,0]
gDict=dict(zip(gLetter,gPoints))

# Task is to sort the list based on GPA of the student
# Then generate a list of just the Reg from sorted list
# GPA calculation forlmula is as under:
# GPA=sum(product of GP and CH)/sum(CH)




# Task-3
# First filter the students who registered 5 subjects
# Then sort those on the basis of GPA in Descending order
# Then generate a list of just Reg of those students
# f=filter(lambda s:len(s['Courses'])==5,data)
# a=sorted(f,key=calcGPA,reverse=True)
# print(list(map(lambda s:s['Reg'],a)))



# Task-4
# Find the Reg with highest GPA in Sec A provided the student
# registered at least 4 subjects

f=filter(lambda s:s['Sec']=='A' and len(s['Courses'])>=4,data)
print(max(f,key=calcGPA)['Reg'])

# Do the same for Sec B


# Task-5
# Generate GPA of all Students
# Then Add GPA of the student as a new Key-Value Pair
