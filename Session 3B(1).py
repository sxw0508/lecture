# -*- coding: utf-8 -*-
"""
Software Development: progarmming and algorithms (SDPA) 2022/23
Session 3B
"""
#slide 9
empty_dict={}
eng2esp= {'one': 'uno','two': 'dos', 'three': 'tres'}


#slide 10: Define a dictionary
eng2esp= {'one': 'uno','two': 'dos', 'three': 'tres'}
eng2esp_2= dict(one='uno', two= 'dos',three='tres')
eng2esp_3= dict([('one','uno'), ('two','dos'),('three','tres')])

#slide 11: add and mutate
eng2esp['two']
eng2esp['ten']

eng2esp['two']=2
eng2esp['six']= 'cuatro'

#slide 12: Dictionary operations
'one' in eng2esp
'tres'in eng2esp.values()

del eng2esp['two']
eng2esp.pop('two')

eng2esp.keys()
eng2esp.values()


#slide 14: A dictionary with different values: 
person = {}
type(person)


person['fname'] = 'Joe'
person['lname'] = 'Fonebone'
person['age'] = 51
person['spouse'] = 'Edna'
person['children'] = ['Ralph', 'Betty', 'Joey']
person['pets'] = {'dog': 'Fido', 'cat': 'Sox'}

#slide 15

person['fname']

person['age']

person['children']
person['children'][-1]
person['pets']['cat']


#slide 16

foo = {42: 'aaa', 2.78: 'bbb', True: 'ccc'} 
foo= {42: 'aaa', 2.78: 'bbb', True: 'ccc'} 
foo[42]  
foo[2.78]
foo[True] 


#slide 17
eng2esp.items()

#slide 18: dictionary representation
favorite_languages = {'jen': 'python',
                      'sarah': 'c', 
                      'edward': 'ruby',
                      'phil': 'python'}

student= {
'fname': 'Anna',
'lname': 'William',
'course': 'SDPA',
'grade': 'A'
}


#slide 19: nesting in dectionaries
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens= [alien_0, alien_1, alien_2]

#slide 20: nesting in dictionaries
students = {
'ej2020': {
'first': 'Anna',
'last': 'William',
'course': 'SDPA'
},
'ms8040': {
'first': 'Marie',
'last': 'Adam',
'course': 'VISAN'
},}

#slide 21: a dictionary in a dictionary
for st_key, student_info in students.items():
	print("\nUsername: " + st_key)
	full_name = student_info['first'] + " " + 	student_info['last']
	course = student_info['course']
	print("\tFull name: " + full_name.title())
	print("\tcourse: " + course.title())
    

#Slide 23: packing and unpacking
a, b, c = '123' #Unpacking strings 
a, b, c = [1, 2, 3] # Unpacking lists 
my_dict = {'one': 1, 'two':2, 'three': 3} # Unpacking dictionaries (keys, values, and items)  
a, b, c = my_dict # Unpack keys 
a, b, c = my_dict.values() # Unpack values 
a, b, c = my_dict.items() # Unpacking key-value


#slide 25
numbers = {"one": 1, "two": 2, "three": 3} 
letters = {"a": "A", "b": "B", "c": "C"} 
combination = {**numbers, **letters} 

#slide 27: sets
fav_animals = {'Alpaca', 'Kangaroo', 'Koala'}

#slide 28: defining a set 
empty_set = set() 		# not {}?
set_from_list = set([1, 2, 1, 4, 3])
basket = {'orange', 'banana', 'pear', 'apple','apple'}
len(basket) 			# => 4
'orange' in basket 		# => True
'crabgrass' in basket 	# => False


#slide 29-32: set operations
a = set('abracadabra') 	# {'a', 'r', 'b', 'c', 'd’}
b = set('alacazam') # {'a', 'm', 'c', 'l', 'z’}

a - b # Set difference (letters in a but not in b)
a | b # Set union (letters in a or b or both)
a & b # Set intersection (letters in both a and b)
a ^ b # Symmetric difference (letters in a or b but not both)

# Slide 34 : looping
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

#slide 36
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

#slide 37

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)
 

for i, v in enumerate(['tic', 'tac', 'toe'],10):
    print(i, v)
