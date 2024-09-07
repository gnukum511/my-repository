import time
import sys

# Function to produce a beep sound
def beep():
    sys.stdout.write('\a')
    sys.stdout.flush()

# Get user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
ale = int(input("Enter average life expectancy (ALE): "))

# Determine and print the appropriate message based on age
if age < 18:
    print(f"{name}, you are a Student.")
    print(f"At least {18 - age} years to become a worker.")
elif 18 <= age < 65:
    print(f"{name}, you are a Worker.")
    print(f"{65 - age} years to retire.")
else:  # age >= 65
    if age < ale:
        print(f"{name}, you are Retired.")
        print(f"{ale - age} years to reach ALE.")
    else:
        for i in range(3):
            beep()
            print("!!! Life Expectancy Reached !!!")
            time.sleep(i + 1)  # Waits for 1, then 2 seconds in the following iterations
