# #Identity Operators:
# #Definition:
# # is / is not

# a = [1,2,3]
# b = [1 ,2 ,3]
# c = b
# d = [1 ,2 ,3 ,4]

# print(a == b) #true
# print(a is not b) #true
# print(b is c) #true

# print(b == c) #true
# print(b != a) #false

# print(b == a) #true


#Membership Operator
#Definition: check whether a value is present in a collection
#in / not in

fruits = ["apple","mango", "guava"]
print("apple" in fruits) #True

print("mangoo" in fruits) #False

Sentence = "Advik is a good student"
print("Advik" in Sentence)

#BitWise Operators
print(2 & 3)
print(3 | 4)

print(bin(22))
