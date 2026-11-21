
# My Chore Checklist Countdown

# PART 1: Set today's total number of chores (no list needed)

total_chores = 4
original_count = total_chores
print("You have" ,original_count, "chores to finish today")

#You have originalCount chores to finish today.

# PART 2: Keep a counter for completed chores and the current chore number

completed_count = 0
chore_num = 1

# PART 3: Repeat while there are still chores left to check off

while chore_num <= total_chores :

#PART 4 : 
    if chore_num == 1 :
        next_chore = "Make your bed"
    elif chore_num == 2:
        next_chore = "feed the pet"
    elif chore_num == 3:
        next_chore = "wash the dishes"
    else:
        next_chore = "take out the trash"


    answer = input("Have you finished: ( yes/ no): ")   

    
# PART 5: Only move on to the next chore once it is marked done

    if answer == "yes":
    
        completed_count += 1
        chore_num += 1    
        print("yeeeeeess almost done")
    else:
        print("Ok , finish it and check again")

# PART 6: Print how many chores remain after each check
    print("Chores remaining:", total_chores - completed_count)
    print()

# PART 7: This only prints once every chore is marked done
print("===== ALL CHORES COMPLETE! =====")
print("Great work finishing your entire checklist today!\n")


# PART 9: Print the final chore checklist summary
print("\n===== CHORE CHECKLIST SUMMARY =====")
print("Chores Assigned Today:", original_count)
print("Chores Completed:", completed_count)
print("Chores Remaining:", total_chores - completed_count)
print("======================================")












    