# -*- coding: utf-8 -*-
"""
Software Development: progarmming and algorithms (SDPA) 
EMATM0048
Session 5A
@author: Zahraa Abdallah
"""

#slide 18
class Dog:
	"""definition of the dog class"""
	def __init__(self, name, age):
		"""initialise name and age attributes"""
		self.name= name
		self.age= age
        
        
#slide 20
my_dog= Dog("Bandit", 9)
friend_dog= Dog("Willie", 10)
print (my_dog.name)
print(friend_dog.name)

#slide 22
class Dog:
    """definition of the dog class"""
    def __init__(self, name, age):
        """initialise name and age attributes"""
        self.name= name
        self.age= age
    def sit(self):
        print(self.name.title() + " is now sitting.")
    def roll_over(self):
        print(self.name.title() + " rolled over!")

#slide 23
my_dog= Dog("Willie", 9)
my_dog.sit()
my_dog.roll_over()

#slide 24
print (my_dog)

class Dog:
    """definition of the dog class"""
    def __init__(self, name, age):
        """initialise name and age attributes"""
        self.name= name
        self.age= age
    def sit(self):
        print(self.name.title() + " is now sitting.")
    def roll_over(self):
        print(self.name.title() + " rolled over!")
    def __str__(self):
        return "Dog’s name is " + str(self.name) + " of age "+str(self.age)

my_dog= Dog("Willie", 9)
print (my_dog)

#slide 22
class Dog:
    """definition of the dog class"""
    def __init__(self, age):
        """initialise name and age attributes"""
        self.name= "Default name"
        self.age= age
    def sit(self):
        print(self.name.title() + " is now sitting.")
    def roll_over(self):
        print(self.name.title() + " rolled over!")
    def __str__(self):
        return "Dog’s name is " + str(self.name) + " of age "+str(self.age)


my_dog= Dog(9)
print (my_dog)

#slide 23
my_dog.name="Willie"
print (my_dog)

# slide 26
class Dog:
    """definition of the dog class"""
    def __init__(self, name= 'def', age=9):
        """initialise name and age attributes"""
        self.name=name
        self.age= age
    def sit(self):
        print(self.name.title() + " is now sitting.")
    def roll_over(self):
        print(self.name.title() + " rolled over!")
    def __str__(self):
        return "Dog’s name is " + str(self.name) + " of age "+str(self.age)
    def set_name(self, newname= ""):
        self.name= newname
    def get_name (self):
        return self.name
    
my_dog= Dog()
print ('Dog default name', my_dog.get_name())

my_dog.set_name("Willie")
print ('Dog name', my_dog.get_name())


#slide 32
class Animal:
    """definition of the Animal class"""                                                
    def __init__(self, name, age):
        """initialise name and age attributes"""
        self.name= name
        self.age= age
    def set_name(self, newname=""):
        self.name= newname
    def get_name(self):
    		return self.name
    def set_age(self, newage):
    		self.age= newage
    def get_age(self):
    		return self.age

#slide 34
#class Cat(Animal):
#    def sleep(self):
#        print(self.name.title() + " is now sleeping.")
#    def roll_over(self):
#        print(self.name.title() + " rolled over!")

#slide 37
class Cat(Animal):
    def __init__(self, name, age, breed=""):
        super().__init__(name,age)
        self.breed = breed
    def sleep(self):
        print(self.name.title() + " is now sleeping.")
    def roll_over(self):
        print(self.name.title() + " rolled over!")

my_cat=  Cat("Kitty", 9, "Russian")
print('My cat name:', my_cat.get_name())
print('my cat age:', my_cat.get_age())
print('my cat breed:', my_cat.breed)
#slide 31
class Alpaca(Animal):
	def roll_over(self):
		print(self.name.title() + " don’t roll over!")

my_hamster= Animal ("Star", 5)
my_alp= Alpaca("Mimi", 9)
my_cat= Cat("kitty", 3)

my_alp.roll_over()
my_cat.roll_over()
my_hamster.roll_over()

