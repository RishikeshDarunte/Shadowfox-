#  2. Jumping Jacks Workout Routine

def jumping_jacks_workout(total_jumping_jacks=100, per_set=10):
    completed_jacks = 0

    for i in range(0, total_jumping_jacks, per_set):
        # Ask the user to perform the set
        print(f"Perform {per_set} jumping jacks.")
        completed_jacks += per_set

        # Ask if the user is tired
        tired = input("Are you tired? (yes/y or no/n): ").strip().lower()

        # If tired, ask if they want to skip the remaining sets
        if tired in ['yes', 'y']:
            skip = input("Do you want to skip the remaining sets? (yes/y or no/n): ").strip().lower()
            if skip in ['yes', 'y']:
                print(f"You completed a total of {completed_jacks} jumping jacks.")
                break
        else:
            remaining_jacks = total_jumping_jacks - completed_jacks
            if remaining_jacks > 0:
                print(f"{remaining_jacks} jumping jacks remaining.")
            else:
                print("Congratulations! You completed the workout.")
                break

# Call the function to start the workout
jumping_jacks_workout()