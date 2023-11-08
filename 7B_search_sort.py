# -*- coding: utf-8 -*-
"""
Software Development: programming and algorithms (SDPA) 2022/23
Session 7 Serching and Sorting examples
"""
import random
def makelist(n, lo, hi):
    # Create random list of numbers
    # list length will be n
    # numbers will in in range [lo,hi]
    testList = []
    i = 0
    while i < n:
        #testList.append(i)
        element = random.randint(lo,hi)
        testList.append(element)
        i = i + 1
    return testList

# Linear Search
def linearsearch(arr, x):
   for i in range(len(arr)):
      if arr[i] == x:
         return i
   return -1
arr = ['t','u','t','o','r','i','a','l']
x = 'a'
#print("element found at index "+str(linearsearch(arr,x)))


def binary_search( list, element ):
    lo = 0
    hi = len(list) - 1
    while lo <= hi:
        mid = lo + ( (hi - lo) // 2 ) # or (hi+lo)//2
        if element > list[mid]:
            # go to the right
            lo = mid+1
        elif element < list[mid]:
            # go to the left
            hi = mid-1
        else:
            # i.e. list[mid] == element
            return mid
    return -1

# Create sorted list of numbers
testList = []
for i in range(100):
    testList.append(i)

element = 76
found_at_index = binary_search(testList, element)
print(f"Found element {element} at index {found_at_index}")


#Insertion sort
def swap( list, a, b ):
    # Helper to swap two items in list
    # a and b are the index of the items
    item = list[a]
    list[a] = list[b]
    list[b] = item

def insertion_sort(list):
    # start with second element as first is trivially sorted
    i = 1
    while i < len(list):
        # items [0,i-1] are sorted
        # swap until item is in proper place
        j = i # i may already be in proper place
        while j > 0 and list[j] < list[j-1]:
            # swap
            swap(list, j, j-1)
            j = j-1
        # Increment to get next item to insert
        i = i + 1


# Verify it works
list = [9, 1, 15, 28, 6]
print("Unsorted")
print(list)
insertion_sort(list)
print("Sorted")
print(list)

list = makelist(100, 0, 10)
print("Unsorted")
print(list)
insertion_sort(list)
print("Sorted")
print(list)
