
"""

     *         i = 1 , j = 1 to 2
   * * *       i = 2 , j = 1 to 1
 * * * * *
 for n = 3

"""
n = int(input("How many rows of pattern do you want: "))
for i in range(1, n + 1):
    
    #code for space
    for j in range(1 , n - i + 1):
        print(" ",end = "")

    #code for stars
    for k in range(1,2*i-1+1):
        print("*",end = "")

    print()