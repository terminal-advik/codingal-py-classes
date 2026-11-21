"""
*      i = 0 , j = 0
**     i = 1 , j = 0 to 1
***    i = 2 , j = 0 to 2
****   i = 3 , j = 0 to 3
*****  i = 4 , j = 0 to 4
"""

n = int(input("How many rows of pattern do you want: "))

for i in range(1, n + 1):
    for j in range(0, i + 1):
        print("*", end="")

    print(" ")

    
