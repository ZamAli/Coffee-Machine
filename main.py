Coffee_Menu = {
    "espresso": {
        "ingredients":{
            "water": 50,
            "milk": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients":{
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients":{
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }

}

resources ={
    "milk": 550,
    "water": 300,
    "coffee": 300,
    "money": 0,
}

def check_ingredients(user_input):
    for key in Coffee_Menu[user_input]["ingredients"].keys():
        if key in resources.keys():
            if resources[key] < Coffee_Menu[user_input]["ingredients"][key]:
                return f"sorry! not enough {key}"
    return f"continue"

def update_ingredients(user_input):
    for key in Coffee_Menu[user_input]["ingredients"].keys():
        if key in resources.keys():
            new_val = resources[key] - Coffee_Menu[user_input]["ingredients"][key]
            resources.update({key:new_val})
def insert_coins(user_input):
    pennies = int(input("how many pennies?: "))
    resources["money"] += pennies * 0.01
    nickles = int(input("how many nickles?: "))
    resources["money"] += nickles * 0.05
    dimes = int(input("how many dimes?: "))
    resources["money"] += dimes * 0.1
    quarters = int(input("how many quarters?: "))
    resources["money"] += quarters * 0.25
    total = pennies * 0.01 + nickles * 0.05 + dimes * 0.1 + quarters * 0.25
    if Coffee_Menu[user_input]["cost"] == total:
        update_ingredients(user_input)
        return f"here is your {user_input} ☕️, enjoy!"
    elif Coffee_Menu[user_input]["cost"] < total:
        update_ingredients(user_input)
        change = round(total - Coffee_Menu[user_input]["cost"],2)
        resources["money"] -= change
        print (f"here is your change of 🤑${change}")
        return f"here is your {user_input} ☕️, enjoy!"
    else:
        resources["money"] -= total
        return f"sorry! not enough money. Here is your refund of 💰${total}"

def user_choice(user_input):
    res = check_ingredients(user_input)
    if res == "continue":
        print(insert_coins(user_input))
    else:
        print(res)

turn_off = False
while not turn_off:
    user_pick = input ("What would you like? (espresso/latte/cappuccino): ")
    if user_pick == "latte" or user_pick == "cappuccino" or user_pick == "espresso":
        user_choice(user_pick)
    elif user_pick == "report":
        for k in resources:
            if k != "money":
                print (f"{k} : {resources[k]}ml")
            if k == "money":
                print(f"{k} : ${resources[k]}")
    elif user_pick == "off":
        turn_off = True
    else:
        print ("invalid option")
