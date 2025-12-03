"""
Full Name: Taiwo Ayeyemi
Class-Section: IS 250 01
Assignment Title: Calculate Average of Three Scores
Submission Date: 11/17/2025
"""

"""
Pseudocode:
1. Ask the user to enter the first exam score.
2. Ask the user to enter the second exam score.
3. Ask the user to enter the third exam score.
4. Convert the three scores to numbers (floats).
5. Send the three scores to a function that calculates the average.
6. Inside the function: add the three scores, divide by 3, and return the result.
7. After receiving the average, print each score on its own line.
8. Print the final average score on its own line.
"""

def calculate_average(score1, score2, score3):

    total = score1 + score2 + score3

    average = total / 3

    return average



first_score_input = input("Enter first score: ")

score1 = float(first_score_input)

second_score_input = input("Enter second score: ")

score2 = float(second_score_input)

third_score_input = input("Enter third score: ")

score3 = float(third_score_input)

average_score = calculate_average(score1, score2, score3)

print("First score:", score1)

print("Second score:", score2)

print("Third score:", score3)

print("Final average score is:", average_score)


