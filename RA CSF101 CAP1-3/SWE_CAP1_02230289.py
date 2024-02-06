################################
# Kuenzang Rabten
# B.E software engineering
# 02230289
################################
# REFERENCES
# Links that you referred while solving 
# the problem
# https://www.codingal.com/coding-for-kids/blog/rock-paper-scissors-game-in-python/
# https://www.youtube.com/watch?v=1X2kGrryecE
# https://www.w3schools.com/python/python_dictionaries.asp#:~:text=Dictionaries%20are%20used%20to%20store,and%20earlier%2C%20dictionaries%20are%20unordered.
################################
# SOLUTION
# Your Solution Score:
# 50293
################################

# Read the input.txt file
def read_input(file_path):
    with open(file_path, 'r') as file:
        rounds = [line.strip().split() for line in file] 
    return rounds

input_file = "input_9_cap1.txt"
rounds = read_input(input_file)

# solution
def calculate_score(player_shape, opponent_shape, outcome):
    shape_scores = {'A': 1, 'B': 2, 'C': 3} #A for Rock, B for paper and C for scissors
    result_scores = {'X': 0, 'Y': 3, 'Z': 6} # Score fro outcomes: X=0, Y=3 and Z=6.

    # Scores for the player and the opponent
    player_score = shape_scores[player_shape] + result_scores[outcome]
    opponent_score = shape_scores[opponent_shape] + result_scores[outcome]

    return player_score, opponent_score
total_score = 0
for round_info in rounds:
    # Gets the opponent's choice and outcome
    opponent_choice, condition = round_info
    # Estimates the player's choice based on an outcome
    player_choice = 'A' if condition == 'Y' else ('B' if condition == 'X' else 'C')

    # Scores for current round and total score
    player_score, _ = calculate_score(player_choice, opponent_choice, condition)
    total_score += player_score

print("The total score is:", total_score)



