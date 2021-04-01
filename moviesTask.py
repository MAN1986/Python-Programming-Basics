m1={
    "Title":"12 Angry Men",
    "Year":1957,
    "Runtime":96,
    "Genre":("Crime", "Drama"),
    "Director":"Sidney Lumet",
    "Actors":["Martin Balsam", "John Fiedler", "Lee J. Cobb", "E.G. Marshall"]
    }
m2={
    "Title":"Inception",
    "Year":2010,
    "Runtime":148,
    "Genre":("Action", "Adventure", "Sci-Fi", "Thriller"),
    "Director":"Christopher Nolan",
    "Actors":["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Elliot Page"," Tom Hardy"]
    }
m3={
    "Title":"The Dark Knight",
    "Year":2008,
    "Runtime":152,
    "Genre":("Action", "Crime", "Drama", "Thriller"),
    "Director":"Christopher Nolan",
    "Actors":["Christian Bale", "Heath Ledger", "Aaron Eckhart", "Michael Caine"]
    }
m4={
    "Title":"Lawless",
    "Year":2012,
    "Runtime":116,
    "Genre":("Crime", "Drama"),
    "Director":"John Hillcoat",
    "Actors":["Shia LaBeouf", "Tom Hardy", "Jason Clarke", "Guy Pearce"]
    }
m5={
    "Title":"The Godfather",
    "Year":1972,
    "Runtime":175,
    "Genre":("Crime", "Drama"),
    "Director":"Francis Ford Coppola",
    "Actors":["Marlon Brando", "Al Pacino", "James Caan", "Richard S. Castellano"]
    }
m6={
    "Title":"The Expendables 2",
    "Year":2012,
    "Runtime":103,
    "Genre":("Action", "Adventure", "Thriller"),
    "Director":"Simon West",
    "Actors":["Sylvester Stallone", "Jason Statham", "Jet Li", "Dolph Lundgren"],
    }
m7={
    "Title":"Scent of a Woman",
    "Year":1992,
    "Runtime":156,
    "Genre":("Drama",),
    "Director":"Martin Brest",
    "Actors":["Al Pacino", "Chris O'Donnell", "James Rebhorn", "Gabrielle Anwar"]
    }
m8={
    "Title":"The Italian Job",
    "Year":2003,
    "Runtime":111,
    "Genre":("Action", "Crime", "Thriller"),
    "Director":"F. Gary Gray",
    "Actors":["Mark Wahlberg", "Charlize Theron", "Donald Sutherland", "Jason Statham"]
    }
m9={
    "Title":"Parker",
    "Year":2013,
    "Runtime":118,
    "Genre":("Action", "Crime", "Thriller"),
    "Director":"Taylor Hackford",
    "Actors":["Jason Statham", "Jennifer Lopez", "Michael Chiklis", "Wendell Pierce"]
    }
m10={
    "Title":"Venom",
    "Year":2018,
    "Runtime":112,
    "Genre":("Action", "Adventure", "Sci-Fi"),
    "Director":"Ruben Fleischer",
    "Actors":["Tom Hardy", "Michelle Williams", "Riz Ahmed", "Scott Haze"]
    }

myCollection=[m1,m2,m3,m4,m5,m6,m7,m8,m9,m10]

# Display First actor in the actor list of the Last movie in collection
# print(myCollection[-1]['Actors'][0])

# Generate a List of All movie Titles
# print([m['Title'] for m in myCollection])
## Without List Comprehension
# t=[]
# for m in myCollection:
#     t.append(m['Title'])
# print(t)

# Generate a List of movie titles with Genre Action
# print([m['Title'] for m in myCollection if 'Action' in m['Genre']])
## Without List Comprehension
# t=[]
# for m in myCollection:
#     if('Action' in m['Genre']):
#         t.append(m['Title'])
# print(t)

# Generate a List of all Genres in the collection
# print(list({g for m in myCollection for g in m['Genre']}))
## Without Set Comprehension
# gen=set()
# for m in myCollection:
#     for g in m['Genre']:
#         gen.add(g)
# gen=list(gen)
# print(gen)

# Generate a List of all Actors who have worked with Director "Christopher Nolan"
# print(list({a for m in myCollection for a in m['Actors'] if m['Director']=="Christopher Nolan"}))
## Without Set Comprehension
# act=set()
# for m in myCollection:
#     if(m['Director']=="Christopher Nolan"):
#         for a in m['Actors']:
#             act.add(a)
# act=list(act)
# print(act)

# Create a Dictionry with key as Director name and value as list of his Movie Titles
# d={}
# for m in myCollection:
#     if(m['Director'] not in d):
#         d[m['Director']]=[m['Title']]
#     else:
#         d[m['Director']].append(m['Title'])
# print(d)

# Create a Dictionry with keys as Actor Names and value as number of movies
# d={}
# for m in myCollection:
#     for a in m['Actors']:
#         if(a not in d):
#             d[a]=1 
#         else:
#             d[a]+=1
# print(d) 

# Create a Ditionary with key as Genre and Value as List of Movies of that Genre
# d={}
# for m in myCollection:
#     for g in m['Genre']:
#         if(g not in d):
#             d[g]=[m['Title']]
#         else:
#             d[g].append(m['Title'])
# for k,v in d.items():
#     print(f'{k}\t{v}')

# Generate a List of Actors who have worked in both Drama and Action movies
## Wrong Approach
# a=[]
# for m in myCollection:
#     for act in m['Actors']:
#         if({'Action','Drama'}.issubset(m['Genre'])):
#             a.append(act)
# print(a)
## Correct Approach
# actionActors={a for m in myCollection for a in m['Actors'] if 'Action' in m['Genre']}
# dramaActors={a for m in myCollection for a in m['Actors'] if 'Drama' in m['Genre']}
# print(list(actionActors.intersection(dramaActors)))

# Find total RunTime of all movies in collection
# t=0
# for m in myCollection:
#     t+=m['Runtime']
# print(t)
