# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

def calculate_dog_years():
    # Your control flow logic goes here
    dog_human_age = input("Input a dog's age: ")
    dog_age_num = int(dog_human_age)
    if dog_age_num > 2:
        dog_age = (dog_age_num - 2) * 7 + (10 * 2)
    elif dog_age_num == 1 or dog_age_num == 2:
        dog_age = (dog_age_num *10)
    else:
        print("Enter valid Age")




    print(f"The dogs age in dog years is {dog_age}")

# Call the function
calculate_dog_years()
