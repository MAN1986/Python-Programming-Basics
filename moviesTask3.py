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

# Find the movie title with maximum Runtime
print(max(myCollection,key=lambda m:m['Runtime']))
print(max(myCollection,key=lambda m:m['Runtime'])['Title'])

# Sort the movies from Oldest to Newest.
# If year is same, sort them based on Title
# Then generate a list of just the titles from above list
s=sorted(myCollection,key=lambda m:(m['Year'],m['Title']))
t=[m['Title'] for m in s]
print(t)


# Display the movie title with maximum Genres in the Genre Tuple
print(max(myCollection,key=lambda m:len(m['Genre']))['Title'])


# Generate a List of movie titles with Genre Action
print([m['Title'] for m in myCollection if 'Action' in m['Genre']])
f=filter(lambda m:'Action' in m['Genre'],myCollection)
print([m['Title'] for m in f])

from sys import getsizeof
# What is maximum Runtime of movie with Genre Action
a=[m for m in myCollection if 'Action' in m['Genre']]
print(getsizeof(a))
print(max(a,key=lambda m:m['Runtime']))

f=filter(lambda m:'Action' in m['Genre'],myCollection)
print(getsizeof(f))
print(max(f,key=lambda m:m['Runtime']))


# Display the movie title with maximum Genres in the Genre Tuple
print(max(myCollection,key=lambda m:len(m['Genre']))['Title'])

maxGenre=len(max(myCollection,key=lambda m:len(m['Genre']))['Genre'])
f=filter(lambda m:len(m['Genre'])==maxGenre,myCollection)
print([m['Title'] for m in f])
