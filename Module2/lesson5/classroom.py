#Continue Statement
# i = 1
# while i < 6: 
# #i = 1, 2 ,3 , 4 , 5 , 6

#     if(i == 3) :
#         i = i + 1 #i = 4
#         continue # rest of the lines ignored and pointer moves to the next iteration
    
#     print(i , end = ", ")
#     i += 1

# #Output : 1 , 2 , 4 , 5 

# for i in range(1 , 12):

#     if i > 5 : #for i = 5 this statement is False
#         continue

#     print(i ,end = ", ")

#output : 1, 2, 3, 4 , 5

#Patterns : 
# n = 6
# *
# **
# ***
# ****
# *****
# ******

# print("*")
# print("**")
# print("***")
# print("****")
# print("*****")

#Q. Print the matrix of n X n

# n = int(input("How many lines of pattern do YOU want: \n"))
# for i in range(0, n):
#     for j in range(0, n):
#         print("*",end = ", ")

#     print()

n = int(input("How many lines of pattern do YOU want: \n"))


for i in range(1, n + 1):
    for j in range (1 , i + 1): #2
        print("*" , end="")

    print()

        