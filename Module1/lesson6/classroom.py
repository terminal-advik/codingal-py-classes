# #if-elif-else statements 

# marks = int(input("Enter your marks:"))

# #grade A , B ,C or Fail

# if marks >= 90:
#     print("Grade A")
# elif marks >= 75:    
#     print("Grade B")
# elif marks >= 50:
#     print("Grade C")
# else:
#     print("Fail")


# #And Operator

# age = int(input("Enter your age:"))
# has_id = input("True or False:")   

# # print(type(age))    # <class 'int'>
# # print(type(has_id)) # <class 'str'>

# # has_id = "TRue"

# if has_id.lower() == "true" :   # "true" == "true"
#     has_id = True
# else:
#     has_id = False

# # print(type(has_id)) #boolean

# # print(has_id) #True

# #Question : if age is greater than or equal 18 and has_id then print "you can drive the car"

# if age >= 18 and has_id :        #In case of "and" operator all the conditions need to be true 
#     print("you can drive the car")

#3 OR ------operator

art_period = True
games_period = False

# if art_period or games_period:
#     print("Fun Day at school")
# else:
#     print("Boring day at school")

#4-----------NOT operator

art_period = not art_period
games_period = not games_period

# if art_period or games_period:
#     print("Fun Day at school")
# else:
#     print("Boring day at school")

print(art_period)  #false
print(games_period)#true


s = "monday"
print(s.capitalize())

# Practice Activity:

a = b = c = d  = True
e = False

if a and b and c and d and e :
    print("all are true")
elif a == False :
    print("a is false")
elif not b :
    print("b is false")
elif not c :
    print("c is false")
elif not d :
    print("d is false")
else :
    print("e is false")