################################
# Kuenzang Rabten
# SWE 
# 02230289
################################
# REFERENCES
# Links that you referred while solving 
# the problem
# https://www.quora.com/What-does-input-strip-split-for-in-range-n-mean-arrays-Python-3-x-numpy-development#:~:text=The%20strip()%20method%20removes,case%2C%20a%20space%20character).
# https://www.youtube.com/watch?v=qGAY-YGJr2U
# https://play.google.com/store/apps/details?id=com.kvassyu.coding.py&hl=en&gl=US
################################
# SOLUTION
# Your Solution Score:
# Task 1: There were 20000 people assigned and there are 23926 of overlapping space assiognments.
# Task 2: There were 4707 assignments that overlap completely.
################################

# Read input file
def read_input():
    # Open the input file in read mode
    with open('input_9_cap2.txt', 'r') as f:
        # Return a list of lines, each split into sections based on the comma and space separator
        return [line.strip().split(', ') for line in f.readlines()]

# Solution for Task 1
def task_1(assignments):
    # Initialize a variable to keep track of total overlaps
    total_overlaps = 0
    
    # Iterate through each line of assignments
    for line in assignments:
        # Update total_overlaps by adding the result of count_overlaps for the current line
        total_overlaps += count_overlaps(line)
    
    # Print the summary of Task 1, including the total number of people assigned and total overlaps
    print(f"There were {sum([len(line) for line in assignments])} people assigned and there are {total_overlaps} overlapping space assignments")

# Function to count overlaps within a line
def count_overlaps(space):
    # Convert each space section into a tuple of integers and sort the list of sections
    sections = [tuple(map(int, s.split('-'))) for s in space]
    sections.sort()
    
    # Initialize variables to track the current range, count of overlaps, and total overlaps
    current_range = sections[0]
    count = 0
    total_overlaps = 0
    
    # Iterate through the sorted sections
    for i in range(1, len(sections)):
        # Check for overlap with the current range
        if sections[i][0] <= current_range[1]:
            count += 1
            total_overlaps += min(current_range[1], sections[i][1]) - current_range[0] + 1
        else:
            # If no overlap, update the current_range and reset count
            current_range = sections[i]
            count = 1
    
    # Return the total number of overlaps for the given line
    return total_overlaps

# Solution for Task 2
def task_2(assignments):
    # Initialize a variable to keep track of total completely overlapping assignments
    total_complete_overlaps = 0
    
    # Iterate through each line of assignments
    for line in assignments:
        # Update total_complete_overlaps by adding the result of count_complete_overlaps for the current line
        total_complete_overlaps += count_complete_overlaps(line)
    
    # Print the summary of Task 2, including the total number of completely overlapping assignments
    print(f"There were {total_complete_overlaps} assignments that overlap completely")

# Function to count completely overlapping assignments within a line
def count_complete_overlaps(space):
    # Convert each space section into a tuple of integers
    sections = [tuple(map(int, s.split('-'))) for s in space]
    
    # Initialize a variable to count completely overlapping assignments
    complete_overlaps = 0
    
    # Iterate through each pair of sections
    for i in range(len(sections)):
        for j in range(i+1, len(sections)):
            # Check if one section completely overlaps with the other
            if sections[i][0] <= sections[j][0] and sections[i][1] >= sections[j][1]:
                complete_overlaps += 1
            elif sections[j][0] <= sections[i][0] and sections[j][1] >= sections[i][1]:
                complete_overlaps += 1
    
    # Return the total number of completely overlapping assignments for the given line
    return complete_overlaps

# Main execution block
if __name__ == "__main__":
    # Read input from the file
    tasks = read_input()
    
    # Perform Task 1 and Task 2 and print the results
    task_1(tasks)
    task_2(tasks)
