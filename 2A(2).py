# -*- coding: utf-8 -*-
"""
Software Development: progarmming and algorithms (SDPA) 2020/21
Session 2A 
@author: Dr. Zahraa Abdallah
"""

# slide 3
s1 = 'SDPA is good'
s2 = 'I like coding'
for char1 in s1:
	for char2 in s2:
		if char1 == char2:
			print("letter",char1)
			break 

#slide 5
x= "Alpaca is cute"
print (x)
print("\N{winking face}")

#slide 6
x= 'Hello'
y= 'there'
print (x + y) 
print (x,y)

#slide 7
print (x + 3) #returns an error how to fix it 
print (x * 3)

#slide 9
var= 'PYTHON'
var[0]
var[5]
var[6]

#slide 10
var[:2]
var[3:]
var[::]


#slide 11
var[0:3]
var[4:]
var[:5:2]

# slide 12
var[-2]
var[-4:]

#slide 13
s= "hello"
s[0]='y'
s= 'y'+s[1:]

#slide 19
x = 5
if x < 10:
    print('Smaller')
if x > 20:
    print('Bigger')
print('Finish')

#slide 21
y= 8
if x == y:
	print('x and y are equal')
else:
	if x < y:
		print('x is less than y')
	else:
		print('x is greater than y')


#slide 24
x = float(input("Enter a number for x: "))
y = float(input("Enter a number for y: "))
if x == y:
	print("x and y are equal")
	if y != 0:
		print("therefore, x / y is", x/y)
elif x < y:
	print("x is smaller")
elif x > y:
	print("y is smaller")
print("done!")

#slide 27
n = 5
while n > 0 :
    print(n)
    n -=1
print('Blastoff!')

#slide 29
n = input("You're in the Lost Forest. Go left or right? ")
while n == "right":
	n = input("You're in the Lost Forest. Go left or 	right? ")
print("You got out of the Lost Forest!") 

#slide 30
for c in 'alpaca':
    print (c)
    
#slide 31
range(5,40,10)
range(40,5,10)
range(5)

#slide 33
x = 4
for i in range(0, x):
	print(i)
	x = 5
    
#slide 34
s = 'A random text' 
i=0
while i<len(s):
	char= s[i]
	if(char=='a'):
		 print('there is an a')
	i+=1 	

#####
i=0
for index in range(len(s)):	
	if(s[index]=='a'):
		 print('there is an a')
######
for ch in s:
	if ch=='a':
		print('there is an a')



#slide 35
x = 6
while x: 
	print(x) 
	x -= 1 
	if x == 3: 
		break

#slie 36
current_number = 0
while current_number < 10:
	current_number += 1
	if current_number % 2 == 0:
		continue
	print(current_number)

