"""
Full Name: Taiwo Ayeyemi
Class-Section: IS 250 01
Assignment Title: Calculate Average of Three Scores
Submission Date: 12/03/2025
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
# Define a function that calculates the average of three scores
def calculate_average(score1, score2, score3):
    # Add the three scores together
    total = score1 + score2 + score3

    # Divide the total by 3 to get the average
    average = total / 3

    # Return the computed average
    return average

# Ask the user for the first score
first_score_input = input("Enter first score: ")

# Convert the first score to a float
score1 = float(first_score_input)

# Ask the user for the second score
second_score_input = input("Enter second score: ")

# Convert the second score to a float
score2 = float(second_score_input)

# Ask the user for the third score
third_score_input = input("Enter third score: ")

# Convert the third score to a float
score3 = float(third_score_input)

# Call the function to calculate the average of the three scores
average_score = calculate_average(score1, score2, score3)

# Print the first score
print("First score:", score1)

# Print the second score
print("Second score:", score2)

# Print the third score
print("Third score:", score3)

# Print the final average score
print("Final average score is:", average_score)



