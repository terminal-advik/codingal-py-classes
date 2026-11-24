import random

# ================================
# NUMBER GUESSING GAME
# ================================

# ---------- SETTINGS (given to you) ----------
secret = 1
secret = random.randint(1, 50)
max_attempts = 5
count = 0
guess = 0

print("=" * 42)
print(" 🎮 NUMBER GUESSING GAME")
print("=" * 42)
print("I have a secret number between 1 and 50.")
print("You have 5 attempts to guess it.")
print("After each wrong guess I will give you a hint.")
print()

# ---------- PART 1: the loop and the guess ----------
# Write a while loop that runs while count is less than max_attempts
# AND guess is not equal to secret.
# Inside the loop (indented):
while count < max_attempts and guess != secret:
#   read the guess with int(input("Your guess: "))
    guess = int(input("Your guess: "))
#   add 1 to count
    count = count + 1

    # ---------- PART 2: win or not ----------
    if guess == secret:
    # If guess equals secret, print a win message.
        print("🎉 Correct!! You guessed it in ", count, "attempt(s)!!!")
        print("Well done - You are a number wizard!!🧙‍♂️" )
    # Otherwise (else), do Parts 3 and 4.
    else:
        # ---------- PART 3: distance and hint ----------
        # Work out diff, the distance between guess and secret.
        # Do not use abs(). Use if / else instead.
        if secret > guess:
            diff = secret - guess
        else:
            diff = guess - secret
        # Print a hint:  diff >= 20 Ice cold | diff >= 10 Cold | diff >= 5 Warm | else Hot
        if diff >= 20:
            print("🧊 Ice cold!! You are very far away.")
        elif diff >= 10:
            print("🥶 Cold. Still quite a distance to go.")
        elif diff >= 5:
            print("🔥 WARM!! Super close!!")
        else:
            print("🔥🥵🔥 HOT!!!! A step away!!")  

        # ---------- PART 4: lives left ----------
        remaining_attempts = max_attempts - count
        if remaining_attempts > 0:
            print("Lives left:", end = " ")
            for i in range(1, remaining_attempts + 1):
                print("❤️", end = " ")
            print("\n")
        # remaining = max_attempts - count
        # If remaining is more than 0, use a for loop to print a ❤️ for each life left.

# ---------- GAME OVER (after the loop) ----------
if guess != secret:
    print("=" * 42)
    print("☠️💀 GAME OVER!!!!!! You used all 5 attempts.")
    print("The secret number was:", secret)
    print("=" * 42)
# If guess is still not equal to secret, print "Game over"
# and show the secret number.
