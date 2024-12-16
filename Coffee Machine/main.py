from coffee_data import menu
from transactions import insert_coins
from resources import dispense_coffee, display_report, check_resources

INTIAL_MACHINE_RESOURCES = {"milk": 500, "water": 500, "coffee": 50, "money": 0.0}


def coffee_machine():
    """Function that runs the coffee machine"""
    resources = INTIAL_MACHINE_RESOURCES
    print("Coffee Machine has started...")

    def handle_report():
        display_report(resources)

    def handle_off():
        nonlocal is_running
        is_running = False

    def handle_coffee_choice(choice):
        if check_resources(coffee=choice, resources=resources):
            is_transaction_successful, message = insert_coins(menu[choice]["cost"])
            if is_transaction_successful:
                print(message)
                response = dispense_coffee(choice, resources)
                print(response.get("message"))
                resources.update(response.get("resources"))
            else:
                print(f"Transaction Not Successful due to {message}")
        else:
            print("Not enough resources.")

    command_handlers = {
        "report": handle_report,
        "off": handle_off,
    }

    is_running = True
    while is_running:
        user_input = input("What would you like? (espresso/latte/cappuccino):").lower()
        if user_input in command_handlers:
            command_handlers[user_input]()  # Call the corresponding function
        elif user_input.capitalize() in menu:
            handle_coffee_choice(user_input.capitalize())
        else:
            print("Invalid input. Please select a valid option.")

    print("Coffee Machine has shutdown...")

coffee_machine()
