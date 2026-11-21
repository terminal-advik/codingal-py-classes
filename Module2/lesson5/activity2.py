#Floyed's Triangle
#
# 1
# 1 2 
# 1 2 3
# 1 2 3 4


n = int(input("How many rows of pattern do you want: "))

num = 1

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(num, end="")
        num +=1

    print(" ")