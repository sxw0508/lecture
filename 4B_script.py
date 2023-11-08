# -*- coding: utf-8 -*-
"""
Software Development: progarmming and algorithms (SDPA) 
Session 4B
"""

#slide 8
def multi_iter(a,b):
	result = 0 
	while b >0:
		result += a
		b -= 1 
	return result 

def multi_rec(a,b):
	if b==1:
		#base case
		return a
	else:
		#recursive case
		return a+multi_rec(a,b-1)



#slide 9
def fact(n): 
	if n == 1:
		return 1 	
	else:
		return n*fact(n-1)

#slide 11
def isPal(s):
	if len(s) <= 1:
		return True
	else:
		if s[0] == s[-1]:
			return isPal(s[1:-1])
		else:  
			return False

