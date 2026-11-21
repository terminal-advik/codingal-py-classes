print("************************************************************************")
print("                    ->YOUR HOLIDAY ACTIVITY PLANNER<-                   ")
print("************************************************************************")
print("")

print("STEP 1: Pick your favorite holiday type")
print("1: A camping vacation")
print("2: A tropical vacation")
print("")

choice = int(input("Enter 1 or 2: "))
print("")

if choice==1:
    print("Step 2: pick your Camping Vacation Activity:)")
    print("1: Hunting")
    print("2: Campfire Storytime")
    print()

    camping_activity = int(input("Enter 1 or 2: "))
    print()

    if camping_activity == 1:
        print("You picked    : Hunting")
        print("Best time     : Afternoon - Evening ")
        print("Remember      : Stay safe & have fun!!!!!")
    else:
        print("You picked    : Campfire Storytime")
        print("Best time     : Evening - Midnight")
        print("Remember      : Gather sticks, marshmellows, gramham crackers, & chocolate to make smores!!!!! ")

elif choice == 2:
    print("Step 2: Pick your Tropical Vacation Activity")
    print("1: The Beach")
    print("2: Rainforest Tour")
    print()

    tropical_activity = int(input("Enter 1 or 2: "))
    print()

    if tropical_activity == 1:
        print("You picked    : The Beach   ")
        print("Best for      : Building sandcastles & swimming")
        print("Remember      : Wear sunscreen & bring Beach toys")
    else:
        print("You picked    : Rainforest tour")
        print("Best for      : Tourist & people who like exploring")
        print("Remember      : Put on bug repellent")

else:
    print("That wasn't a valid option")
    print("Please enter 1 for a Camping vacation or 2 for a tropical vacation")

print()
print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")
print("              YOUR HOLIDAY PLAN IS READY            ")
print("                   ENJOY YOUR TRIP                  ")
print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")