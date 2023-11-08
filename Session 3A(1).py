# -*- coding: utf-8 -*-
"""
Software Development: progarmming and algorithms (SDPA) 2022/23
Session 3A
"""
#slide 3
s1 = "SDPA is good"
s2 = "I like coding"
for char1 in s1:
	for char2 in s2:
		if char1 == char2:
			print(char1)
			break 

#slide 6
isinstance(4, object) 			#True
isinstance(4.5, object) 			#True
isinstance('alapaca', object) 	#True
isinstance(None, object) 		#True
isinstance(str, object) 			#True
isinstance(False, object) 		#True
isinstance(object, object) 		#True

#slide 12
1==1.0
type(1)== type(1.0)
1 is 1.0

#slide 13
x= 'happy coding!'
y= 'happy '
y+='coding!'
x==y     	#True
x is y	#False
id(x)
id (y)

#slide 17
t= (4,'EMAT',10.5)
t[0]
t[1:]
t[0]=10 #error tuples are immutable


#slide 18
t1= (1, 'two',3)
t2= (t1, 3.25)
print (t2)
print (t1+t2)
print ((t1+t2)[3])
print ((t1+t2)[2:5])


for t in t1:
	print (t)

#slide 19


# We can unpack these values!
colors= 'red', 'blue','green'
print(colors) 		# (‘red’,’blue’,’yellow’)
type(colors) 			# => tuple

x, y, z = colors
x # =>’red’
y # =>’blue’
z # =>’yellow’

#slide 23
L=[1,2,3]
total =0
for i in range (len(L)):
	total+=L[i]
print(total)


total =0
for i in L:
	total+=i
print(total)

#slide 25
L1= [1,2,3] 
L2=[4,5,6]
L3= L1+L2 #create a new object L3, L1 and L2 unchanged
L1.extend(L2) #extend L1
L1.append(L2)

#slide 26
L1.insert(0,'alpaca')
print (L1)
L1*2

#slide 28
L= [2,1,3,6,3,7,0]
L.remove(2)
L.remove(3)
del(L[1])
L.pop()

#slide 20
squares = []
for value in range(1,7):
	square = value**2
	squares.append(square)
print(squares)


Squares = [x**2 for x in range(1,7)]

#slide 32
my_food= ['pizza', 'falafel', 'carrot cake']
friend_food= my_food
my_food.append('churros')

friend_food= my_food[:]
my_food.append('fish')

#slide 36
starter= ['Garlic bread','Soup']
main_menu= ['Risotto','Shish Kebab']
dessert= ['Cake'] 
my_food= [starter,main_menu, dessert]
main_menu.append('Chips')

#slide 37
L1 = [1,2,3,4]
L2 = [1,2,5,6]
#Remove duplicated elements
for e1 in L1:
    if e1 in L2:
        L1.remove(e1)

L1 = [1,2,3,4]
L2 = [1,2,5,6]
#Remove duplicated elements
L1_copy= L1[:]
for e1 in L1_copy:
    if e1 in L2:
        L1.remove(e1)
