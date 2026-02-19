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


def log_transaction(transaction_number):
    """
    Log a single financial transaction.
    
    This function captures two pieces of information for each transaction:
    - A textual description (e.g., "Lunch at Bobics", "Transport to Bugujju")
    - A numerical value representing the expense amount
    
    Args:
        transaction_number (int): The sequence number of the transaction
        
    Returns:
        tuple: A tuple containing (description, amount) where:
            - description (str): Textual description of the transaction
            - amount (float): The expense amount
    """
    # Display transaction header for clarity
    print(f"\n--- Transaction {transaction_number} ---")
    
    # Get transaction description from user and remove leading/trailing whitespace
    description = input("Enter transaction description (e.g., 'Lunch at Bobics'): ").strip()
    
    # Validate and get transaction amount
    while True:
        try:
            # Convert user input to float (handles decimals)
            amount = float(input("Enter transaction amount: "))
            
            # Ensure amount is non-negative (expenses can't be negative)
            if amount < 0:
                print("Amount must be non-negative. Please try again.")
                continue  # Ask again for valid input
            
            # Return both description and amount as a tuple
            return (description, amount)
            
        except ValueError:
            # Handle non-numeric input gracefully
            print("Invalid input. Please enter a valid numerical value.")

def check_budget_breach(cumulative_spending, budget):
    """
    Check if cumulative spending exceeds the budget.
    
    This function implements real-time fiscal oversight by checking immediately
    after each transaction whether the cumulative spending has exceeded the budget.
    If breached, it issues a clear warning notification to the user.
    
    Args:
        cumulative_spending (float): The total of all expenses entered so far
        budget (float): The initial budget limit set by the user
    """
    # Check if spending has exceeded the budget
    if cumulative_spending > budget:
        # Calculate how much over budget the user is
        deficit = cumulative_spending - budget
        
        # Display warning message with detailed information
        print(f"\n⚠️  WARNING: Budget exceeded by {deficit:.2f}!")
        print(f"   Cumulative spending: {cumulative_spending:.2f}")
        print(f"   Budget: {budget:.2f}")
        print(f"   Deficit: {deficit:.2f}\n")

def generate_summary(budget, transactions):
    """
    Generate and display a comprehensive financial summary report.
    
    This function creates the final terminal report that includes:
    - The initial budget that was set
    - The total sum of all recorded expenses
    - The resulting financial position (remaining balance or deficit)
    - A consolidated textual log itemizing each transaction
    
    Args:
        budget (float): The initial budget set by the user
        transactions (list): List of tuples containing (description, amount) for each transaction
    """
    # Calculate total expenses by summing all transaction amounts
    # Using list comprehension: extract amount (second element) from each transaction tuple
    total_expenses = sum(amount for _, amount in transactions)
    
    # Calculate financial position: positive = remaining balance, negative = deficit
    financial_position = budget - total_expenses
    
    # Print report header with decorative separator
    print("\n" + "="*60)
    print("FINANCIAL SUMMARY REPORT")
    print("="*60)
    
    # Display key financial metrics
    print(f"\nInitial Budget: {budget:.2f}")
    print(f"Total Expenses: {total_expenses:.2f}")
    
    # Display remaining balance if under budget, or deficit if over budget
    if financial_position >= 0:
        print(f"Remaining Balance: {financial_position:.2f}")
    else:
        # Use abs() to show deficit as a positive number for clarity
        print(f"Deficit Amount: {abs(financial_position):.2f}")
    
    # Print transaction log section
    print("\n" + "-"*60)
    print("TRANSACTION LOG")
    print("-"*60)
    
    # Display each transaction with a numbered list
    if transactions:
        # enumerate() provides index (starting at 1) and transaction tuple
        for i, (description, amount) in enumerate(transactions, 1):
            print(f"{i}. {description}: {amount:.2f}")
    else:
        # Handle edge case where no transactions were entered
        print("No transactions recorded.")
    
    # Print footer separator
    print("="*60 + "\n")

def main():
    """
    Main function to run the financial management program.
    
    This function orchestrates the entire program flow:
    1. Initialize budget
    2. Log transactions (minimum 5 for testing)
    3. Provide real-time fiscal oversight
    4. Generate final summary report
    """
    # Display welcome message
    print("="*60)
    print("PERSONAL FINANCIAL MANAGEMENT TOOL")
    print("Track your spending and stay within your limits!")
    print("="*60)
    
    # ============================================================
    # STEP 1: Budget Initialization
    # ============================================================
    # Get budget from user (must be non-negative)
    budget = initialize_budget()
    print(f"\nBudget set to: {budget:.2f}")
    
    # ============================================================
    # STEP 2: Transaction Logging
    # ============================================================
    # Initialize list to store all transactions as tuples (description, amount)
    transactions = []
    
    # Track cumulative spending to check against budget in real-time
    cumulative_spending = 0.0
    
    # Display transaction logging section header
    print("\n" + "-"*60)
    print("TRANSACTION LOGGING")
    print("Enter at least 5 transactions (or type 'done' to finish)")
    print("-"*60)
    
    # Counter to track transaction sequence numbers
    transaction_count = 0

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
