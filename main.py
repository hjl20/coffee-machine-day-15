MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

COINS = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickels": 0.05,
    "pennies": 0.01
}

RESOURCES_UNITS = {
    "water": "ml",
    "milk": "ml",
    "coffee": "g"
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_enough_resources(coffee_ingredients):
    """
    Checks if there are enough resources of each ingredient in coffee_ingredients.
    Returns True if enough and False otherwise.
    :param coffee_ingredients: dict
    :return: bool
    """
    for ingredient in coffee_ingredients:
        # Not enough resources
        if resources[ingredient] < coffee_ingredients[ingredient]:
            print(f"Sorry, there is not enough {ingredient}")
            return False
        else:
            return True


def calculate_coins():
    """
    Asks user for coin amounts and returns the total.
    :return: float
    """
    total = 0
    for coin in COINS:
        # Formatting coin amounts to 2 decimal places
        num_coin = input(f"How many {coin} (${COINS[coin]:.2f})? ")
        # Input validation
        if num_coin.isnumeric():
            num_coin = int(num_coin)
            total += num_coin * COINS[coin]
        else:
            print(f"Invalid number of {coin}. Defaulting to 0.")
    return total


def make_coffee(coffee_ingredients):
    """
    Takes coffee_ingredients amounts and subtracts from resources.
    :param coffee_ingredients: dict
    :return:
    """
    for ingredient in coffee_ingredients:
        resources[ingredient] -= coffee_ingredients[ingredient]


def show_report(machine_money):
    """
    Prints amounts of each resource and machine_money
    :param machine_money:
    :return:
    """
    for resource in resources:
        print(f"{resource.title()}: {resources[resource]}{RESOURCES_UNITS[resource]}")
    print(f"Money: ${machine_money:.2f}")


def process_transaction(user_input):
    """
    Takes user_input to process coffee order.
    Returns money from coffee_cost if enough resources and money from user and 0 otherwise.
    :param user_input: str
    :return: float
    """
    coffee_type = MENU[user_input]
    coffee_ingredients = coffee_type["ingredients"]
    enough_resources = check_enough_resources(coffee_ingredients)

    if not enough_resources:
        return 0
    else:
        coffee_cost = coffee_type["cost"]
        user_money = calculate_coins()

        if user_money < coffee_cost:
            print(f"Sorry, that's not enough money. Money refunded (${user_money:.2f}).")
            return 0
        else:
            # Make coffee
            make_coffee(coffee_ingredients)
            user_money -= coffee_cost
            print(f"Here is ${user_money:.2f} dollars in change.")
            print(f"Here is your {user_input}. Enjoy!")
            return coffee_cost


def coffee_machine():
    machine_on = True
    machine_money = 0

    while machine_on:
        user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

        # Coffee selected
        if user_input in MENU:
            machine_money += process_transaction(user_input)
        # Non-coffee selected
        elif user_input == "report":
            show_report(machine_money)
        elif user_input == "off":
            return
        else:
            print("Please choose between espresso/latte/cappuccino.")
            continue


coffee_machine()
