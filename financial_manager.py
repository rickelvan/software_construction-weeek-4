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


    # Main transaction input loop - continues until user types 'done'
    while True:
        transaction_count += 1
        
        # Ask user if they want to continue or finish
        user_input = input(f"\nEnter transaction {transaction_count}? (press Enter to continue, or 'done' to finish): ").strip().lower()
        
        # Check if user wants to finish entering transactions
        if user_input == 'done':
            # Ensure at least one transaction was entered
            if transaction_count < 2:  # transaction_count starts at 1, so < 2 means no transactions
                print("Please enter at least one transaction before finishing.")
                transaction_count -= 1  # Decrement to retry this iteration
                continue
            break  # Exit the loop if user is done
        
        # Get transaction details from user
        description, amount = log_transaction(transaction_count)
        
        # Store transaction in the list
        transactions.append((description, amount))
        
        # Update cumulative spending total
        cumulative_spending += amount
        
        # Provide feedback to user about the logged transaction
        print(f"Transaction logged: {description} - {amount:.2f}")
        print(f"Current cumulative spending: {cumulative_spending:.2f}")
        
        # ============================================================
        # STEP 3: Real-time Fiscal Oversight
        # ============================================================
        # Check immediately after each transaction if budget is breached
        check_budget_breach(cumulative_spending, budget)
    
    # Reminder about minimum transaction requirement for testing
    if len(transactions) < 5:
        print(f"\nNote: Only {len(transactions)} transaction(s) entered. For testing purposes, at least 5 transactions are recommended.")
        print("Continuing with current transactions...\n")
    
    # ============================================================
    # STEP 4: Final Financial Summary
    # ============================================================
    # Generate and display comprehensive report
    generate_summary(budget, transactions)


# Entry point of the program
# This ensures main() only runs when the script is executed directly,
# not when imported as a module
if __name__ == "__main__":
    main()
