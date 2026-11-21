
#Take a variable and ask for 1 or 2 i.e Two-Wheeler and Four-Wheeler
vehicle_type = int(input("Enter 1 for Two-Wheeler or 2 for Four-Wheeler: "))

#If Two-Wheeler selected ask for scooty in option 1 and Mountain bike in option 2.

if vehicle_type == 1 :

    two_wheeler_type = int(input("Enter 1 for Scooty or 2 for Mountain Bike: "))

    if two_wheeler_type == 1 :
        print("You picked  : Scooty")
        print("Top speed   : 80 km/h")
        print("Best for    : City roads")
    else: 
        print("you picked : Mountain Bike")
        print("Top speed   : 60 km/h")
        print("Best for    : Off-road trails")

elif vehicle_type == 2 :
    
    # 1- Five seater Sedan , 2- 7 seater SUV 
    car_type = int(input("Enter 1 for 5-Seater Sedan and 2 for 7-Seater SUV: "))

    if car_type == 1 :
        print("You picked  : Sedan")
        print("Seats       : 5 passengers")
        print("Best for    : Family trips")
    else:
        print("You picked  : SUV")
        print("Seats       : 7 passengers")
        print("Best for    : Off-road adventures")

else:
    print("Please enter a valid option")        

print()
print("====================================")
print("   Your custom ride is ready!       ")
print("   Enjoy the journey!               ")
print("====================================")


