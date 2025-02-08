from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu=Menu()
coffeMaker=CoffeeMaker()
moneyMachine=MoneyMachine()

is_on= True

while is_on:
    options=menu.get_items()
    eingabe = input(f"What would you like? ({options})):\n")
    if eingabe == "off":
        # Schalte die Maschine aus, wenn der Benutzer "off" eingibt
        is_on = False
        print("Thank you! Till next time. ")
    elif eingabe == "report":
        coffeMaker.report()
        moneyMachine.report()
        # Zeige den aktuellen Ressourcenstand an, wenn der Benutzer "report" eingibt

    elif eingabe in menu.get_items():
        order=menu.find_drink(eingabe)
        if coffeMaker.is_resource_sufficient(order):
            if moneyMachine.make_payment(order.cost):
                coffeMaker.make_coffee(order)


