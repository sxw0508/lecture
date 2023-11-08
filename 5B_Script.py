# -*- coding: utf-8 -*-
"""
Software Development: progarmming and algorithms (SDPA) 
EMATM0048
Session 5B
@author: Zahraa Abdallah
"""

#slide 28
b= float(input ("enter b: "))
c= float(input ("enter c: "))
a= b/float(c)
print ("The ratuon is", a)

############################
#b= float(input ("enter b: "))
#c= float(input ("enter c: "))
#
#
#try:
#    a = b/float(c)
#    print ('The ratio is', a)
#except ZeroDivisionError:
#	print ("c is zero, hence ratio is undefined")
#print ('Now here')
#
#
##slide 29
#try:
#	a = float(input("Tell me one number: "))
#	b = float(input("Tell me another number: "))
#	print("a/b = ", a/b)
#	print("a+b= ", a+b)
#except ValueError:
#	print("Could not convert to a number.")
#except ZeroDivisionError:
#	print("Can't divide by zero")
#except:
#	print("Something went very wrong.") 
#
def avg(grades):
    assert len(grades) != 0, 'no grades data'
    return sum(grades)/len(grades)
grades= []
print (avg(grades))
print ("now here")

