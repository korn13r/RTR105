# reading and converting

#name = input('Enter:')

#apple  = input ('Enter:')
#Enter: 100
#x = apple - 10
#x = int(apple) - 10
#print(x)


# looking inside strings

#fruit = 'banana'
#letter = fruit[1]
#print(letter)

#x = 3
#w = fruit[x - 1]
#print(w)


# strings have length : function len (gives length of a string)

#fruit = 'banana'
#print(len(fruit))

#x = len(fruit)
#print(x)

# Looping through strings (while)

#fruit = 'banana'
#index = 0
#while index < len(fruit):
#    letter = fruit[index]
#    print(index, letter)
#    index = index + 1

# Looping through string (for)

#fruit = 'banana'
#for letter in fruit:
#    print(letter)


# Looping and counting Looping and Counting
#This is a simple loop that 
#loops through each letter in a 
#string and counts the number 
#of times the loop encounters 
#the 'a' character

#word = 'banana'
#count = 0
#for letter in word:
#    if letter == 'a':
#        count = count + 1
#print(count)


# Slicing strings

#s = 'Monty Python'
#print(s[0:4])       # Mont
#print(s[6:7])       # P
#print(s[6:20])      # Python
#print(s[:2])        # Mo
#print(s[8:])        # thon
#print (s[:])        # Monty Python

#String Concatenation
#When the  + operator is applied to strings, it means “concatenation”

#a ='Hello'
#b = a + 'There'
#print(b)

#c = a + ' ' + 'There'
#print(c)


# Using in as a Logical Operator

#fruit = 'banana'
#'n' in fruit         # True
#'m' in fruit         # False
#'nan' in fruit       # True
#if 'a' in fruit:
#    print('Found it!')


# String Library
#stuff = 'Hello world'
#type(stuff)
#print(stuff.lower.__doc__)
#print(stuff.index.__doc__)
#print(stuff.capitalize.__doc__)
#print(stuff.casefold.__doc__)
#print(stuff.endswith.__doc__)
#print(stuff.isalnum.__doc__)
#print(stuff.isspace.__doc__)
#print(stuff.join.__doc__)
#print(stuff.find.__doc__)
#print(stuff.count.__doc__)
#print(stuff.maketrans.__doc__)

#greet = 'Hello Bob'
#zap = greet.lower()
#print(zap)
#print(greet)
#print('Hi There'.lower())



# Searching a String ( find() )

#fruit = 'banana'
#pos = fruit.find('na')
#print(pos)

#aa = fruit.find('z')
#print(aa)                 # string position starts at zero


# search and replace

#greet = 'Hello Bob'
#nstr = greet.replace('Bob','Jane')
#print(nstr)

#nstr = greet.replace('o','X')

# Striping Whitespace

greet = ' Hello Bob '
greet.lstrip()           # remove space on left
greet.rstrip()           # remove space on right









































    
