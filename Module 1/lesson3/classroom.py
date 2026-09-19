#Lesson 3 : 

#1--> Data Types [it tell python what kind of variable is stored] and type(x) [gives us the type of x]

# x  = 100
# print(type(x))

# x = 100.5
# print(type(x))

# x = 100.0
# print(x)
# print(type(x))

#2-------> TypeCasting [changes a value from 1 data type to another]:

# a = "1000"

# print(type(a))

# b = int(a)
# print(type(b))

# # case 2: Incorrect conversion 
# a = "Advik"
# b = type(a)
# print(b)

# c = int(b)

#3---------->Taking User Input
# input()-------> always takes input in form of a str.....

# name = input("What is your name \n")
# print("the students name is", name)

#4---> String indexing and slicing
#  python uses 0 - based indexing.
#  A D V I K
#  0 1 2 3 4
# -5 -4-3-2-1
# name = "Advik"
# print(name[0])

# print(name[3])

# print(name[-1])

#5--> Slicing

#[start : end : jump]

name = "Singhal"

print(name[2 : 6 : 2])

print(name[2:6])

#String Concatenation

s ="Advik"
t ="singhal"
name = s + t
print(name)
print(s + t)

print(s + " " + t)


