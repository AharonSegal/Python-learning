# {dict} the coffee type : {dict} ingredients to make , (int) the cost
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
#{dict} the amount of, ingredients , money, in the machine (value=int)
resources = {
    "water": 5000,
    "milk": 2000,
    "coffee": 1000,
    "money" : 0
}
#{dict} name of coin : (int) value
coins = {
    "quarters" : .025,
    "dimes" : 0.10,
    "nickles" : 0.05,
    "pennies" : 0.01
}
#_main function
def coffee_machine():
    """STAGE 1 : get first input out of 3 options
    a: chose coffee
    b: report
    c: off"""
    running = True
    while True:
        while True:
            print("What would you like? (espresso / latte / cappuccino")
            request = input("""
            press 1 for espresso
            press 2 for latte
            press 3 for cappuccino:
            """)
            if request in ["1","2","3"]:
                break
            elif request == "off":
                print("goodbye :)")
                running = False
                break
            elif request == "report":
                print(f"current resources status: \n {resources}")
            else:
                print("unidentified. please chose valid option. ")

        if not running:
            break

        choice = ""
        if request == "1":
            choice = "espresso"
        elif request == "2":
            choice = "latte"
        else:
            choice = "cappuccino"
        # STAGE 2: checks for sufficient ingredients
        #send the ingredients of choice to function
        check_ingredients(MENU[choice]["ingredients"])
        #STAGE 4: receive payment.
        # the input will be by coin name and not by value same as one would insert 1 coin a quarter "q" then a dime "d"
        # input ex: qddnqpp "quarter,dime,dime..."
        payment = input(f"Please insert {MENU[choice]["cost"]}$")
        # STAGE 5: process payment.
        # def coin_sum(payment) and the received coins to a total sum
        # def check_payment(sum,price) checks for enough payment for coffee
        # def change_to_coin(change) returns change in coins
        check_payment(coin_sum(payment),MENU[choice]["cost"])
        #add money to resources
        resources["money"] += MENU[choice]["cost"]
        # make coffee / decrease ingredients from recourses
        make_coffee(choice)
        # Give coffee
        print(f"Here is your {choice}. Enjoy!”")

def make_coffee(choice):
    """decrease ingredients from recourses
    :parameter """
    for ingredient, required_amount in MENU[choice]["ingredients"].items():
        resources[ingredient] -= required_amount
def check_ingredients(order_ingredients):
    """checks if the requested coffe can be made
    :parameter: the ingredients for the requested coffe/choice.
    if sufficient continues.
    else, end transaction and states missing ingredient
    :type: dict
    :return: NONE
    """
    for ingredient,value in order_ingredients.items():
        if value <= resources[ingredient]:
            continue
        else:
            print(f"Sorry there is not enough {ingredient}.")
def coin_sum(payment):
    """receives payment in coins and returns the total sum
    :parameter:"letter symbols coin"
    :type:  str
    :return : int "the sum value of inserted coins"
    """
    sum = 0
    for i in payment:
        if i == "q":
            sum += 0.25
        elif i == "d":
            sum += 0.10
        elif i == "n":
            sum += 0.05
        else:
            sum += 0.01
    return sum
def check_payment(sum,price):
    """checks for sufficient payment
    if enough payment, returns profit
    else, end transaction.
    :parameter: sum
    :type: int
    :parameter: price
    :type: int
    :returns " sends change sum to be converted to individual coins"
    :return int"""
    change = 0
    if sum >= price:
        change = sum - price
    else:
        print("Sorry that's not enough money")
        change = sum
    change_to_coin(change)
def change_to_coin(change):
    """converts change to individual coins
    :parameter : int
    :returns : str"""
    #cal quarters
    q = 0
    w = change
    while w >= 0:
        w -= 0.25
        q += 1
    # cal dimes
    d = 0
    x = (q * 0.25 - change)
    while x >= 0:
        while x >= 0:
            x -= 0.10
            d += 1
    # cal nickles
    n = 0
    y = (((q * 0.25) + (d * 0.10) - change))
    while y >= 0:
        y -= 0.10
        n += 1
    #cal pennies
    p = 0
    z = (((q * 0.25) + (d * 0.10) +(n * 0.5) - change))
    while z >= 0:
        z -= 0.10
        p += 1
    print(f"Your change is : {q} quarters , {d} dimes , {n} nickles , {p} pennies")

coffee_machine()