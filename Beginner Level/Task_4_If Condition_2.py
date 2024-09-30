def check_same_country():
    # Step 1: Define city lists by country
    australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
    uae = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
    india = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
    
    # Step 2: Ask the user to enter two city names
    city1 = input("Enter the first city: ").strip()
    city2 = input("Enter the second city: ").strip()
    
    # Step 3: Check if both cities belong to the same country
    if city1 in australia and city2 in australia:
        print(f"Both cities are in Australia.")
    elif city1 in uae and city2 in uae:
        print(f"Both cities are in UAE.")
    elif city1 in india and city2 in india:
        print(f"Both cities are in India.")
    else:
        print(f"They don't belong to the same country.")
    
# Call the function
check_same_country()

