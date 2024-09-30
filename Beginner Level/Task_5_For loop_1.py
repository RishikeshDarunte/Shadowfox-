# 1. Simulating Rolling a Six-Sided Die
import random

def roll_die_simulation(rolls=20):
    roll_count_6 = 0
    roll_count_1 = 0
    consecutive_6 = 0
    previous_roll = 0

    for _ in range(rolls):
        roll = random.randint(1, 6)
        print(f"Rolled: {roll}")  # Display each roll
        
        if roll == 6:
            roll_count_6 += 1
            # Check for two consecutive 6s
            if previous_roll == 6:
                consecutive_6 += 1
        elif roll == 1:
            roll_count_1 += 1

        # Update the previous roll
        previous_roll = roll
    
    # Print the results
    print(f"\nTotal rolls of 6: {roll_count_6}")
    print(f"Total rolls of 1: {roll_count_1}")
    print(f"Consecutive rolls of two 6s: {consecutive_6}")

# Call the function for 20 rolls
roll_die_simulation(rolls=20)
