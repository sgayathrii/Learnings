"""
x = 15
def printer():
    x= 30
    return x
print(x)
print(printer())
"""

#Modules in python
#LEGB rule - 
#local
#f = lambda x:x*2 
 
#enclosing function
def greet():
    name = "Bob" 
    def hello():
        print('Hello '+  name)
    hello()
greet() 

#global
name = "Bob"
def greet():
    def hello():
        print('Hello '+  name)
    hello()
greet()  
print(name)




x= 50
def func(x):
    print('x is' , x)
    x = 2
    print("Changed loacl x to", x)
func(x)
print('x is still', x)

#built-in
x= 50
def func():
    global x
    print("This function is now using the global x")
    print("Because of global x is: ", x)
    x=2
    print("Ran func() changed global x to: " , x)
print("Before calling func() x is: ", x)
func()
print("Value of x (outside of func()) is : ", x)

l = [1,2,3]
l.count(2)
print(type(l))
print(type([]))
print(type(()))
print(type({}))

class Sample(): #Class name always starts with capital letter. Better we follow that
    pass

x = Sample()
print(type(x))

# self.attributes = something...
#__init__()

class Dog():
    def __init__(self,breed):
        self.breed = breed
bob = Dog(breed='Terrier') 
frank = Dog(breed = 'Lab')

bob.breed
frank.breed

class Dog():
    #Class Object Attribute
    species = 'mamma'
    def __init__(self,breed, name):
        self.breed = breed
        self.name = name
bob = Dog('Terrier', 'Bob') 
print(bob.name)
print(bob.species)

# methods are function defined 

class Circle():
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return self.radius *self.radius * Circle.pi
    
    def setRadius(self, radius):
        self.radius = radius
    
    def getRadius(self):
        return self.radius


c = Circle()
c.setRadius(2)
print('Radius is: ', c.getRadius())
print('Area is: ', c.area())


#Inheritence:
#Newly formed classes
#Benefit of Inheritence is reduce complexity of coding
        
class Animal():
    def __init__(self):
        print("Animal created")
    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating...nom nom...")
    
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")
    
    def whoAmI(self):
        print("Dog")

    def bark(self):
        print("Woof woof!")

d = Dog()
d.whoAmI()
d.eat()
d.bark()

#Create another example

class Book():
    def __init__(self, title, author, pages):
        print("A book is created")
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title:%s, authoer:%s, pages:%s " %(self.title, self.author, self.pages)
    
    def __len__(self):
        return self.pages
    
    def __del__(self):
        print("A book is destroyed")
    
book = Book("Python", "Joh Andersson", 180)
print(book)
print(len(book))
del book

#Special Methods: built in
"""
__init__
__str__
__len__
__del__

"""
#Error Handling
#print("Hello"  Syntax Error unexpected EOF while parsing

# print("Hello  SystaxError EOL while scanning string literal 

# try and except
# try: 
#Operations here...
#except: Ex1
#if there is an exception then execute this block...
#except: Ex2
#if there is an exception then execute this block...
#except: Ex3
#if there is an exception then execute this block...
#else:

#An example:

try:
    f = open('testfile' 'w')
    #f = open('testfile' 'r') if we give r and then try to write, then it will throw error.
    f.write('Test write this...')
except IOError:
    print('Error: Could not find file or read data.')

else:
    print("Content written successfully")
    f.close()

#the program is crashed now.. but we want our program to run..

try:
    f = open('testfile' 'r')
    f.write('Test write this...')
except:
    print("Error... Could not read file...")
finally:
    print('Always execute finnaly code blocks')
    f.close() #this will continue the code blocks

"""
doubt asked in class by someone.
if(something...):
    if(something....):
        continue
        if(something...):
            continue
"""

   

