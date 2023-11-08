# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 14:37:27 2020
Script for session 1B- SDPA
MSc data science
University of Bristol
@author: Zahraa Abdallah
"""
#Slide 6 
print("Hello World!")

# slide 7
print("First line")
print("Second line")
print("This looks like a script")

# Slide 16
type(5)
type(5.3)
type(None)

#Slide 17 
#try it yourself!

#slide 19
x= 12.5
print(x)

#slide 20
length= 12
width= 4
area= length*width


#Slide 22
x=1
print(type(x))
x='alpaca'
print(type(x))




#slide 26
x= 31
y= 6
print(x+y)
print(x/y)
print(x-y)
print(x*y)
print (x%y)

#try again with floats
print(x//y)


# Slide 28
minutes= 105
hours= minutes//60
remainder= minutes%60

#odd or even, try yourself!


#slide 32
surfing= True
work= False
print(surfing and work)
print(surfing or work)

#slide 33

pi = 3
radius = 11
# area of circle equation <- this is a comment
area = pi*(radius**2)
print(area)

#slide 34
# change values of radius <- another comment
# use comments to help others understand what you are doing in code
radius = radius + 3
print(area)     # area doesn't change
area = pi*(radius**2)
print(area)

#slide 40
x= 10
x_str= str(x)
print ("x is a number",x,".")
print ("x is a string"+ x_str+".")


#slide 41
animal= input("What is your favourite animal?")
print("Do you really like "+ animal +"?")


#slide 42

num= int(input("Type a number... "))
print(5*num) 

#############################
#### AUTOCOMPLETE #######
#############################
# Spyder can autocomplete names for you
# start typing a variable name defined in your program and hit tab 
# before you finish typing -- try it below
# notice that Spyder also automatically adds the closed parentheses for you!

