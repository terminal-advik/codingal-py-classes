print("Enter the value of numerator")

num = int(input("Num: "))


print("Enter the value of denominator")

deno = int(input("Deno: "))

if(num % deno != 0):
    print(num,"is not divisible by",deno)
else:
    print(num,"is divisible by",deno)

#10 is not divisible by 4
#10 is divisible by 5