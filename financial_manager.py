"""
Personal Financial Management Tool
A command-line utility for campus students to track expenses against a budget.

This program implements four core functionalities:
1. Budget initialization - Set a spending limit
2. Transaction logging - Record expenses with descriptions
3. Real-time fiscal oversight - Monitor spending and warn of budget breaches
4. Final financial summary - Generate comprehensive report
"""
def initialize_budget():
    
    # Use a while loop to keep asking until valid input is received
    while True:
        try:
            # Prompt user for budget input and convert to float
            budget = float(input("Enter your budget for this period (e.g., a week): "))
            
            # Validate that budget is non-negative (as per requirements)
            if budget < 0:
                print("Budget must be a non-negative value. Please try again.")
                continue  # Go back to the start of the loop
            
            # Return the valid budget value
            return budget
            
        except ValueError:
            # Handle case where user enters non-numeric input (e.g., text)
            print("Invalid input. Please enter a valid numerical value.")


   
