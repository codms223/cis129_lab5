# Lab 5 The Bottle Return Program
# Author: Chaeeun Lee
# Date: 2024-10-16
# Description: This program calculates the total number of bottles returned for a week and the total payout based on the number of bottles.

# Step 1: Declare variables below 
nbr_of_days = 7                 # Number of days to collect data
total_bottles = 0               # Total bottles collected
today_bottles = 0               # Bottles collected today
total_payout = 0.0              # Total payout calculated
keep_going = "y"                 # Variable to control loop

# Step 2: Loop to run program again
while keep_going.lower() == "y":  # Continue while user wants to run the program again
    total_bottles = 0              # Reset total bottles for the week

    for counter in range(1, nbr_of_days + 1):  # Loop through each day
        today_bottles = int(input(f"Enter number of bottles returned for day #{counter}: "))
        total_bottles += today_bottles  # Accumulate total bottles

    total_payout = total_bottles * 0.10  # Calculate total payout

    # Print the results
    print(f"The total number of bottles collected is {total_bottles}.")
    print(f"The total paid out is ${total_payout:.2f}.")

    print("Do you want to enter another week’s worth of data? (Enter y or n)")
    keep_going = input()  # Update the loop control variable