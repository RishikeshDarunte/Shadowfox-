def calculate_bmi():
    # Step 1: Ask the user for input
    height = float(input("Enter height in meters: "))
    weight = float(input("Enter weight in kilograms: "))
    
    # Step 2: Calculate BMI using the formula
    bmi = weight / (height ** 2)
    
    # Step 3: Determine the BMI category
    if bmi >= 30:
        category = "Obesity"
    elif 25 <= bmi < 30:
        category = "Overweight"
    elif 18.5 <= bmi < 25:
        category = "Normal"
    else:
        category = "Underweight"
    
    # Step 4: Output the result
    print(f"Your BMI is {bmi:.2f}. You are in the '{category}' category.")

# Call the function
calculate_bmi()

def find_country_by_city():
    # Step 1: Define city lists by country
    australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
    uae = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
    india = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
    
    # Step 2: Ask the user to enter a city name
    city = input("Enter a city name: ").strip()
    
    # Step 3: Determine which country the city belongs to
    if city in australia:
        print(f"{city} is in Australia.")
    elif city in uae:
        print(f"{city} is in UAE.")
    elif city in india:
        print(f"{city} is in India.")
    else:
        print(f"{city} is not listed in our database.")
    
# Call the function
find_country_by_city()
