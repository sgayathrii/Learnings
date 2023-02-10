def func():
    return 1

func()

s = "Global variable"

def func():
    print(locals()) 

func()
print(globals())
print(globals().keys())
print(globals()['s'])

#Decorator

#simple examples

def hello(name='John'):
    return 'Hello '+name

hello()

greet = hello

print(greet())

#define function in other funtions

def hello(name='John'):
    print('hello() function has been executed')

    def greet():
        return '\t This is inside the greet() function'

    def welcome():
        return '\t This is inside the welcome() function'
        print(greet())
        print(welcome())
         
hello()
#welcome() #this doesn't work

def hello(name='John'):
    print('hello() function has been executed')

    def greet():
        return '\t This is inside the greet() function'

    def welcome():
        return '\t This is inside the welcome() function'
    
    if name == 'John':
        return greet
    else:
        return welcome
      
x = hello()
print(x())

#Also try this changes

def hello(name='John'):
    print('hello() function has been executed')

    def greet():
        return '\t This is inside the greet() function'

    def welcome():
        return '\t This is inside the welcome() function'
    
    if name == 'John':
        return greet
    else:
        return welcome

x = hello('sam')
print(hello()())


def hello():
    return 'Hi John!'

def other(func):
    print('Other code would go here....')
    print(func())

other(hello)

#Now lets create progrom: Decorator

def new_decorator(func):

    def wrap_func():
        print("Code would e here, before executing the func...")

        func()

        print("Code here will execute after the func()")

    return wrap_func

def func_needs_decorator():
    print("This function is in need of a Decorator")

func_needs_decorator()

func_needs_decorator = new_decorator(func_needs_decorator)

#Now we introduce new character for decorator:

def new_decorator(func):

    def wrap_func():
        print("Code would e here, before executing the func...")

        func()

        print("Code here will execute after the func()")

    return wrap_func

@new_decorator
def func_needs_decorator():
    print("This function is in need of a Decorator")

func_needs_decorator()

#main
#there is no seperate main function like in other languages
#if __name__ == "__main__":
    #start()

#regular expression:(regex)

import re

patterns = ['term1', 'term2']

text = 'This is a string with term1 but id does not have the other term'

for pattern in patterns:
    print('Searching for "%s" in: \n "%s"' %(pattern, text))

    if(re.search(pattern, text)):
        print('\n')
        print("Match was found.  \n")
    else:
        print('\n')
        print("No match found. \n")

#another example
import re

pattern = 'term1'

text = 'This is a string with term1 but id does not have the other term'

match = re.search(pattern, text)

print(type(match))

####################
print(match.start())
print(match.end())
####################

split_term = '@'

phrase = 'What is the domain name of someone with the email: hello@gmail.com'

print(re.split(split_term, phrase))

####################
re.findall('match', 'a phrase')
#####################

#Another example
import re

def multi_re_find(patterns, phrase):
    """
     Take in a list of regex patterns 
     print a list of matches
    """
    for pattern in patterns:
        print("Seaching the phrase using the re check: %r"%pattern)
    print(re.findall(pattern,phrase))
    print('\n')

# * repeated zero or more times
# + must apper at lease once
# ? pattern appears zero or 1 time
# use {m} after the pattern where m is replaced with the number of times the pattern should repeat

# use {m,n} m is minimum and n is max

test_phrase = "sdsd... ssssdddd...sdddsddd...dsds...dsssss...sddddd"

test_patterns = ['sd*', 'sd+', 'sd?', 'sd{3}', 'sd{2,3}']

multi_re_find(test_patterns, test_phrase)

###########
test_phrase = "This is a string! But it has punctuation. How can i remove it?"
#[^!.?]
re.findall('[^!.?]+', test_phrase)

##########
test_phrase = "This is a example sentence. Lets see if we can find some letters."

test_patterns=['[a-z]', '[A-Z]', '[a-zA-Z]+','[A-Z][a-z]+']

multi_re_find(test_patterns, test_phrase)

############
tst_pharse = "This is a string_ with some numbers 1234 and a symbol #hashtag"

tst_patterns=[r'\d+', #sequence of digits
r'\D+', #Non-digits
r'\s+' #whitespace
r'\S+', #Non-whitespace
r'\w+' # alphanumeric characters
r'\W+', #Non-alphanumeric
]
#\wMatch a single word character: [A-Za-z0-9_]
#yes because underscore is a character allowed for naming convention in programing

multi_re_find(test_patterns, test_phrase)


