from coffee_data import menu
from typing import Dict

def dispense_coffee(coffee, resources) -> Dict:
    """Function to check if coffee can be dispensed and return updated resources and money"""
    order = menu[coffee]
    money = resources.get("money")
    order_cost = order.get("cost")

    is_enough_resources = check_resources(coffee=coffee, resources=resources)

    if is_enough_resources:
        try:
            milk_left = resources["milk"] - order["milk"]
            coffee_left = resources["coffee"] - order["coffee"]
            water_left = resources["water"] - order["water"]
            current_money = money + order_cost
            return {
                "resources": {
                    "milk": milk_left,
                    "coffee": coffee_left,
                    "water": water_left,
                    "money": current_money,
                },
                "message": f"Here is your {coffee}...Enjoy",
            }
        except Exception as e:
            print(e)
    return {"resources": resources, "message": "Not enough resources."}


def check_resources(coffee, resources):
    """Function to check whether resources are enough or not in coffee machine"""
    order = menu.get(coffee)
    total_milk = resources.get("milk")
    total_coffee = resources.get("coffee")
    total_water = resources.get("water")
    order_milk = order.get("milk")
    order_coffee = order.get("coffee")
    order_water = order.get("water")

    is_enough_resources = (
        True
        if order_water < total_water
        and order_milk < total_milk
        and order_coffee < total_coffee
        else False
    )
    return is_enough_resources


def display_report(resources):
    """Function to display the resources left on machine"""
    water = resources.get("water")
    milk = resources.get("milk")
    coffee = resources.get("coffee")
    money = resources.get("money")

    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money}")
