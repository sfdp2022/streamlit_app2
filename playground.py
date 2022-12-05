# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 12:49:28 2022

@author: fellos
"""
#For loop practice
item_list =["item 1", "item 2", "item 3"]
for item_list in item_list:
    print("This is", item_list)
    
print("List Complete!")


#Finding the largest value using for loop
largest_so_far = -1  # Don't have list numbers yet so use -1
print("Before", largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)

print("After", largest_so_far)


# Counting in a loop
count = 0
print("Before", count)
for thing in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    print(count, thing)
    
print("After", count)  # How many times code ran


# Summing in a loop & finding average of final value
count = 0
sm = 0
print("Before", count, sm)
for value in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    sm = sm + value
    print(count, sm, value)
  
    
print("After", count, sm, sm / count)


# Filtering in a loop - looking for all values above 20
print("Before")
for value in [9, 41, 12, 3, 74, 15]:
    if value > 20:
        print("Large number", value)
      
print("After")


#Search using Boolean variable
found = False
print("Before", found)
for value in [9, 41, 12, 3, 74, 15]:
    if value == 3:
        found = True
    print(found, value)
    
print("After", found)
      
# Finding smallest value      
smallest = None 
print("Before")
for value in [9, 41, 12, 3, 74, 15]:
    if smallest is None:  # Is is stronger than "==". Use on Booleans or None.
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
     
print("After", smallest)      

# For each letter in fruit print letter    
fruit = "banana" 
for letter in fruit:
    print(letter)

# Slicing strings
s = "Monty Python"
print(s[0:4])
print(s[:5])

# Searching for characters in string
fruit = "banana"
"n" in fruit
"m" in fruit
"nan" in fruit
if "a" in fruit:
    print("Found it!")
else:
    print("Not there.")

# Create lower case copy of a string - does not change original string
greet = "Hello Bob"
zap = greet.lower()

print(greet)

print(zap)


# Replace characters in string
nstr = greet.replace("Bob", "Jane")
print(nstr)


# Strip whitespace
greet = "   Hello Bob   "
greet.lstrip()  # Strips whitespace at left of text
greet.rstrip()  # Strips whitespace at right of text
greet.strip()  # Strips whitespace on both sides of text
#