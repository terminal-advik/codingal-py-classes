#1-------->Indention<-----------------
#definition : adding spaces at the beginning of the line up code

#check if the student is an adult i.e >= 18 years old.
# if he is an adult check if he has a degree in Engineering.
#2--------------->Conditional Statements<------------


age = 26
hasDegree = True

if age >= 18:

    if hasDegree == True:
        print("Yes, he has an adult and has an Engineering Degree")

    else :
        print("yes, he is a adult and doesn't have a enginneering degree")

    
else:

    print("no, he is not an adult and doesn't have a engineering degree")


#practice 
# print(10 % 4) #2

# age < 12 -----> no ticket
# 12 >= age < 60 --------> Standard Ticket
# 60 <= age < 80----------> Senior
# age >= 80 -------> Veteran Ticket

if age < 12:
    print("no ticket")
elif age >= 12 and age < 60:
    print("standard ticket")
elif age >= 60 and age < 80:
    print ("senior ticket")
else:
    print("veteran ticket")

# age < 12 -----> no ticket
# 12 >= age < 60 --------> Standard Ticket
# 60 <= age < 80----------> Senior
# age >= 80 -------> no ticket

if age < 12 or age >= 80:
    print("no ticket")
elif age <= 12 and age < 60:
    print("standard ticket")
else:
    print ("senior ticket")
