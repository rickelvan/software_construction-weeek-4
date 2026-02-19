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
