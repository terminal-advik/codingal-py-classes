# ================================
# POWER CALCULATOR
# ================================

print("=== Power Calculator ===")

# ---------- PART 1: ask the two questions ----------
Base = int(input("Enter a base number: "))
Exponent = int(input("Enter the power(exponent): "))
# Ask for the base number and store it in  base
# Ask for the power and store it in  exponent
# Wrap both in int() — you cannot multiply text.


# ---------- PART 2: the running total ----------
Result = 1
# Create a variable called  result  and start it at 1.
# Think about why 1 and not 0 before you write it. The hint below explains.


# ---------- PART 3 + 4: the loop that multiplies ----------
for i in range(1, Exponent + 1):
    Result = Result * Base
    print("Step", i, ": Result =", Result)
# for i in range(1, exponent + 1):
#     multiply result by base and store it back in result
#     print which step you are on and what result is now


# ---------- PART 5: the answer ----------
print("\nAnswer:", Base, "to the power of", Exponent, "equals to", Result, "\n")
# After the loop, print the base, the exp