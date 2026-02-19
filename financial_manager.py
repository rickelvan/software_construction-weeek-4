
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
