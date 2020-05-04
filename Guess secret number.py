secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

num=int(input("So, what is your guess, muggle? "))
while num != secret_number:
    print("Ha ha! You're stuck in my loop!")
    num=int(input("So, what is your next guess, muggle? "))
print("Well done, muggle! You are free now.")