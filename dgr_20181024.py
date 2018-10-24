# Repeated Steps
# Loops (repeated steps) have iteration variablesthat change each time through a loop.
# Often these iteration variables go through a sequence of numbers.

#n = 5
#while n > 0:
#    print(n)
#    n = n - 1
#print('Blastoff!')
#print(n)

# Infinite Loop
#n = 5
#while n > 0:
#     print('Lather')
#     print('Rinse')
#print('Dry off!')

# Breaking Out of a Loop

#while True:
#    line = input('>')
#    if line == 'done':
#        break
#    print(line)
#print('Done!')

# A Simple Definite Loop

for i in [5, 4, 3, 2, 1]:
    print(i)
print('Blastoff!')


# Definite Loop with Strings
friends = ['joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year:', friend)
print('Done!')

#Looping Through a Set

print('Before')
for thing in [9, 41, 12, 3, 74, 15]:
    print(thing)
print('After')

# Finding the Largest Value
largest_so_far = -1
print('Before', largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print('After', largest_so_far)

# Counting in a Loop
zork = 0
print('Before', zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + 1
    print(zork, thing)
print('After', zork)

# Summing in a Loop

zork = 0
print('Before', zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + thing
    print(zork, thing)
print('After', zork)

# Finding the Average in a Loop
count = 0
sum = 0
print('Before', count, sum)
for value in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print('After', count, sum, sum / count)


























