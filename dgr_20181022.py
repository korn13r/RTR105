big = max('Hello world')
print(big)

tiny = min('Hello world')
print(tiny)

#type conversions

print(float(99) / 100)
i = 42
type(i)
f = float(i)
print(f)
type(f)
print(1 + 2 * float(3) / 4 - 5)

#Building our Own Functions

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')
    
x = 5
print('Hello')

def print_lyricd():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')
print('Yo')
x = x + 2
print(x)

# Once we have defined a function, we can call(or invoke) it as many times as we like
x = 5
print('Hello')
def print_lyricd():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')
print('Yo')
print_lyrics()
x = x + 2
print(x)

# parameters

def greet(lang):
    if lang == 'es':
        print('Hola')
    elif lang == 'fr':
        print('Bonjour')
    else:
        print('Hello')
greet('en')
greet('es')
greet('fr')


# Return Values
def greet():
    return "Hello"
print(greet(),"Glenn")
print(greet(),"Sally")


def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'
print(greet('en'),'Glenn')
print(greet('es'),'Sally')
print(greet('fr'),'Michael')

# Multiple Parameters/ Arguments

def addtwo(a, b):
    added = a + b
    return added
x = addtwo(3, 5)
print(x)






















