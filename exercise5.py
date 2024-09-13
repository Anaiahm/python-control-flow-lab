# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.

def determine_season():
    # Your control flow logic goes here
    month = input("Enter the month (ex. NOV for November ): ").upper()
    day = int(input("Enter the day: "))

    
    if month == "DEC":
        season = "Winter" if day > 21 else "Fall"

    if month == "JAN":
        season = "Winter"

    elif month == "FEB":
        season = "Winter"

    elif month == "MAR":
        season = "Winter" if day < 20 else "Spring"

    elif month == "APR":
        season = "Spring"

    elif month == "MAY":
        season = "Spring"

    elif month == "JUN":
        season = "Spring" if day < 21 else "Summer"

    elif month == "JUL":
        season = "Summer"

    elif month == "AUG":
        season = "Summer"

    elif month == "SEP":
        season = "Summer" if day < 22 else "Fall"

    elif month == "OCT":
        season = "Fall"

    elif month == "NOV":
        season = "Fall"

    
    print(f"{month} {day} is in {season}.")
# Call the function
determine_season()
