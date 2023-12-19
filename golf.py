name = input("Welcome to GC mini golf! What is you name? ")
holes = int(input(f"Hi, {name}! Would you like to play 3 or 6 holes "))
score = 0
strokes = 0
i = 0
hole = 1

"""
The if loops represents how many holes were selected at the start. the while loop uses i as a counter less than the 
number of holes. It adds one to the number of holes each time it loops so once it hits three it is terminated. 
The hole variable is used to display the hole you are on. It counts and adds the next hole number each time. 
I did this to prevent having to copy and paste explicit hole numbers. 
"""
if holes == int(3):
    while i < 3:
        par = 9
        strokes += int(input(f"How many putts for hole {hole}? "))
        i += 1
        hole += 1
        score = strokes - par
elif holes == int(6):
    while i < 6:
        par = 18
        strokes += int(input(f"How many putts for hole {hole}? "))
        i += 1
        hole += 1
        score = strokes - par
# Responds with a comment based on performance and shows total score.
if score < 0:
    print(f"Great Job {name}, your total score was {score}.")
elif score == 0:
    print(f"Good game {name}, your total score was {score}.")
elif score > 0:
    print(f"Nice try, {name} your total score was {score}")
else:
    print("That is not a valid option.")