
#Nested Loops

# for i in range(1 ,3) :
#     #i = 1 , 2
#     for j in range(1,5):
#         #j = 1 , 2 , 3 ,4
#         print(i,j)
#     print("Iteration complete")

#output :
# 1 1
# 1 2
# 1 3
# 1 4
# Iteration complete
# 2 1
# 2 2
# 2 3
# 2 4
#Iteration complete

# i = 1 

# while i <= 2 : #i = 1 , 2  j = there is no j present here
#     j = 1      #j = 1
#     while j <= 4 : # j = 1 , 2 , 3 ,4 ,5
#         print(i, j)
#         j += 1

#     print("Iteration Complete")
#     i += 1

#Q. Write the multiplication table of one to 5 till 12 using one for loop and one while loop:
    
i = 1

while i <= 5: 
    print(f"Table for {i}")
    # print("Table for",i)
    
    for j in range(1, 13):
        print(f"{i} X {j} = {i*j}")

    # i += 1
    print()
    