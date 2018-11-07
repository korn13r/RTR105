#fhand = open('mbox-short.txt', 'r')     # 'r' - read the file /  'w' - wrie to the file

#handle = open(filename,'mode')   # filename is a string
#print(fhand)

#stuff = 'Hello\nWorld!'         # \n  - newline
#print(stuff)

#stuff = 'X\nY'
#print(stuff)
#print(len(stuff))              # \n - is one character


#           Reading files in python

#xfile = open('mbox-short.txt')
#for cheese in xfile:
#    print(cheese)



#        Counting lines in a file

#fhand = open('mbox-short.txt')
#count = 0
#for line in fhand:                   # Use a for loop to read each line
#    count = count + 1
#print('Line Count:', count)


#      Reading the *WHOLE* file

#fhand = open('mbox-short.txt')
#inp = fhand.read()
#print(len(inp))
#print(inp[:20])


#      Searching through a file

#fhand = open('mbox-short.txt')
#for line in fhand:
#    if line.startswith('From'):
#        print(line)                 # attēlot rindas, kuras sākas ar 'From:'



#fhand = open('mbox-short.txt')
#for line in fhand:
#    line = line.rstrip()         # The newline is considered “white space” and is stripped (no blank lines)
#    if line.startswith('From'):
#        print(line)


#            Skipping with continue

#fhand = open('mbox-short.txt')
#for line in fhand:
#    line = line.rstrip()            
#    if line.startswith('From'):
#        continue
#    print(line)



#           Using in to select lines

#fhand = open('mbox-short.txt')
#for line in fhand:
#    line = line.rstrip()
#    if not '@uct.ac.za' in line:
#        continue
#    print(line)



# Promt for File Name
 
fname = input('Enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)





























































