# -*- coding: utf-8 -*-
"""
Software Development: progarmming and algorithms (SDPA) 
Session 4/ Bonus lecture
"""

#slide 8
def multiply(x, y): 
	return x * y 

r = lambda x, y: x * y
r(12, 3)

#slide 6
def square(x): 
	return x * x

numbers=[1, 2, 3, 4, 5]
sqrList=map(square, numbers)
#or
sqrList=map(lambda x:x*x, numbers)

#slide 8
def length_of_all_elements(arr):
	return list(map(len, arr))
length_of_all_elements(['alpaca', 'SDPA', 'data science'])

#slide 9 
first_it = [1, 2, 3] 
second_it = [4, 5, 6, 7] 

list(map(pow, first_it, second_it)) 


#slide 11
#original function with no filter
def starts_with_a(arr):
	ret_arr = []
	for elem in arr:
		if elem[0].lower() == 'a':
			ret_arr.append(elem)
	return ret_arr

starts_with_a(['Alpaca', 'SDPA'])


#slide 12
#original function with filter
def starts_with_a(arr):
	return list(filter(lambda word: word[0].lower()=='a',arr))

starts_with_a(['Alpaca', 'SDPA']) 

#slide 13
# Find the maximum in a list of pairs by value of the second element.
pairs = [(1, 2), (-2, 5), (6, 4)]
max(pairs, key=lambda tup: tup[1])

#slide 14
# Find the maximum in a list of pairs by value of the second element.
pairs = [(1, 2), (-2, 5), (6, 4)]
sorted(pairs, key=lambda tup: tup[1])

#slide 14
squares = [i * i for i in range(10)]

#slide 16
sentence= ["I" ,"lIKe","coDing"]
[word.lower() for word in sentence]

word= 'alpaca'
word_new=[ch for ch in word.lower() if ch not in 'aeiou']

seq= [3,4,8]
[(x, x**2, x**3) for x in seq]
[(i,j) for i in range(5) for j in range(i)]

#side 17
squares = {i: i * i for i in range(10)}

