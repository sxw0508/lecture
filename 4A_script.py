# -*- coding: utf-8 -*-
"""
Software Development: progarmming and algorithms (SDPA) 
Session 4A
"""

#slide 12
x = 25
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, x)
ans = (high + low)/2.0
while abs(ans**2 - x) >= epsilon:
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print ('numGuesses =', numGuesses)
print (ans, 'is close to square root of', x)

# slide 16: function components
def cel_far(celsius):
    """ 
    Input: celsius, temperature in Celsius unit
    Returns the equivalent degree in Fahrenheit
    """
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit

cel_far(45)

#slide 17: Function return 
def greet_user():
	"""Display a simple
	greeting."""
	print("Hello!")

def max_2numbers(x,y):
	"""Display the max of two numbers."""
	if x > y:
		return x
	else:
		return y

max_2numbers(4,20)
greet_user()

#slide 23
def printName(firstName, lastName, reverse= False):
	if reverse:
		print (lastName, firstName)
	else:
		print (firstName, lastName)
        
printName('Olga', 'Raheem', False)
printName('Olga', 'Raheem', reverse = False)
printName('Olga', lastName = 'Raheem', reverse = False)
printName(lastName='Raheem', firstName='Olga', reverse=False)

#slide 26
def make_pizza(size, *toppings):
	"""Summarize the pizza we are about to make."""
	print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
	for topping in toppings:
		print("- " + topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


#slide 28
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein', location='princeto', field='physics')

# slide 30
def f(x):
	y = 1
	x = x + y
	print ('x =', x)
	return x

x = 3
y = 2
z = f(x)
print (x,y,z)


# slide 32

def g(y):
    x+=1
    print(x)

x = 5
g(x)
print(x)

def h(y):
    print(x)
    print (x+1)

x = 5
h(x)
print(x)

def f(y):
	x = 1
	x += 1
	print(x)

x = 5
f(x)      #2
print(x)  #5
