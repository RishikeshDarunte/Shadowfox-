
def format_number(num, format_type):
    # Using the format function to format the number in octal
    formatted_str = format(num, format_type)
    return formatted_str

# Testing the function with 145 and 'o'
result = format_number(145, 'o')
print(f"Formatted result: {result}")

def calculate_pond_area_and_water(radius):
    pi = 3.14  # Approximate value of pi
    # Step 1: Calculate the area of the pond
    area = pi * (radius ** 2)
    
    # Step 2: Calculate the total amount of water
    water_per_sq_meter = 1.4
    total_water = area * water_per_sq_meter
    
    # Step 3: Return the total water amount without any decimal points
    return int(total_water)  # Using int() to remove decimal points

# Radius of the pond is 84 meters
radius = 84
total_water = calculate_pond_area_and_water(radius)
print(f"Total amount of water in the pond: {total_water} liters")

def calculate_speed(distance, time_minutes):
    # Step 1: Convert time from minutes to seconds
    time_seconds = time_minutes * 60  # 1 minute = 60 seconds
    
    # Step 2: Calculate the speed in meters per second
    speed = distance / time_seconds
    
    # Step 3: Return the speed without any decimal points
    return int(speed)  # Using int() to remove decimal points

# Distance is 490 meters, time is 7 minutes
distance = 490
time_minutes = 7
speed = calculate_speed(distance, time_minutes)
print(f"Speed: {speed} meters per second")
