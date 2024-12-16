CURRENCY = {
    "PENNY": 0.01,
    "NICKEL": 0.05,
    "DIME": 0.10,
    "QUARTER": 0.25,
}


def insert_coins(cost) -> bool:
    """Function to ask for coins, make calculation and return change"""
    try:
        penny_count = int(input("enter the amount of pennies:"))
        nickel_count = int(input("enter the amount of nickels:"))
        dime_count = int(input("enter the amount of dimes:"))
        quarter_count = int(input("enter the amount of quarters:"))
    except Exception as e:
        return False, e

    total_amount = float(
        penny_count * CURRENCY["PENNY"] +
        nickel_count * CURRENCY["NICKEL"] +
        dime_count * CURRENCY["DIME"] +
        quarter_count * CURRENCY["QUARTER"]
    )
    is_transaction_successful = total_amount > cost
    return is_transaction_successful, f"Here is your change: ${round(total_amount-cost,3)}..." if is_transaction_successful else f"You fell short of ${abs(cost-total_amount)}..."
