# Initial list of Justice League members
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

# Step 1: Calculate and print the number of members
num_members = len(justice_league)
print(f"Number of members in the Justice League: {num_members}")

# Step 2: Add Batgirl and Nightwing to the list
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print(f"Updated Justice League: {justice_league}")

# Step 3: Move Wonder Woman to the beginning
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")

# Display the updated list
print(f"Wonder Woman as leader: {justice_league}")

# Step 4: Move Green Lantern between Aquaman and Flash
justice_league.remove("Green Lantern")
justice_league.insert(justice_league.index("Flash"), "Green Lantern")
print(f"Green Lantern between Aquaman and Flash: {justice_league}")

# Step 5: Replace the Justice League with a new team
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print(f"New Justice League: {justice_league}")

# Step 6: Sort the list alphabetically
justice_league.sort()
print(f"Alphabetically sorted Justice League: {justice_league}")
