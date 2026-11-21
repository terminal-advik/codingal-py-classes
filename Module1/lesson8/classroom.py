#Operator Precedence: 
#1. ()
#2. ** (Exponent)
#3. *,/,//,%
#4. + ,-
#5. Comparision operators: (> , < , >= , <= , == , !=)
#6. not
#7. and
#8. or

# v, w, x, y = 4, 5, 8, 2
# z = (v + w) * x / y  #36 #This line is a sentence
# #     9 * 8 / 3 -----> normal division Float (expression)
# #     72/2
# #     36.0
# print(z)   # 36.0
# name = "Alex"
# age = 0
# print(name == "Alex" or name == "John" and age >= 2)
# # True - and is checked before or

#checking divisibility using modulus operator(%)

x = 10
y = 6

if(x % y == 0):
    print(y,"divides",x)
else:
    print(y,"does not divide",x)




