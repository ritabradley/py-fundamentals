print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_names = name1 + name2
lowercase_names = combined_names.lower()

# Take both people's names and check for the number of times the letters in the word TRUE occurs.
t = lowercase_names.count("t")
r = lowercase_names.count("r")
u = lowercase_names.count("u")
e = lowercase_names.count("e")
# Check for the number of times the letters in the word LOVE occurs.
l = lowercase_names.count("l")
o = lowercase_names.count("o")
v = lowercase_names.count("v")
e2 = lowercase_names.count("e")
# Combine these numbers to make a 2-digit number.
true = t + r + u + e
love = l + o + v + e2

score = str(true) + str(love)

if int(score) < 10 or int(score) > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 <= int(score) <= 50:
    print(f"your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
