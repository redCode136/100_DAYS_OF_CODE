# Importiere die MENU-Daten und die Ressourcen aus dem Modul menu_data
from menu_data import MENU, resources

# Funktion zur Abwicklung der Bezahlung
def make_transaction(coffeprice, insertmoney):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if coffeprice <= insertmoney:
        # Berechne das Wechselgeld und runde es auf 2 Dezimalstellen
        change = round(insertmoney - coffeprice, 2)
        print(f"It costs {coffeprice}. You gave me {insertmoney}€. Here is ${change} in change.")
        # Füge den bezahlten Betrag zur Kasse hinzu
        resources["money"] += coffeprice
        return True
    else:
        # Wenn nicht genug Geld eingeworfen wurde, gib eine Fehlermeldung aus
        print("Sorry that's not enough money. Money refunded.")
        return False

# Funktion zur Zubereitung des Kaffees
def make_coffee(kaffee):
    # Hole die Zutaten für den gewählten Kaffee aus dem MENU
    choice = MENU[kaffee]["ingredients"]

    # Verringere die Ressourcen basierend auf den verbrauchten Zutaten
    for item in choice:
        resources[item] -= choice[item]
    print(f"Here is your {kaffee} ☕️. Enjoy!")

# Funktion zur Verarbeitung der Münzeinwürfe
def process_coins():
    total = 0
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    # Berechne den Gesamtbetrag basierend auf den eingeworfenen Münzen
    total += int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    # Addiere den bereits vorhandenen Geldbetrag in der Kasse
    total += resources["money"]
    print(total)
    return total

# Funktion zur Überprüfung, ob genügend Ressourcen vorhanden sind
def is_resource_sufficient(kaffee):
    # Hole die Zutaten für den gewählten Kaffee aus dem MENU
    choice = MENU["espresso"]["ingredients"]
    for item in choice:
        # Überprüfe, ob genügend Ressourcen vorhanden sind
        if resources[item] < choice[item]:
            print(f"Sorry there is not enough {item}.")
            return False

    return True

# Funktion zur Anzeige der aktuellen Ressourcen
def show_resource():
    for key, value in resources.items():
        print(f"{key}: {value}")
    print("\n")

# Hauptprogrammschleife
is_on = True
while is_on:
    # Frage den Benutzer nach seiner Auswahl
    eingabe = input("What would you like? espresso, latte, cappuccino):\n")
    if eingabe == "off":
        # Schalte die Maschine aus, wenn der Benutzer "off" eingibt
        is_on = False
        print("Thank you! Till next time. ")

    elif eingabe == "report":
        # Zeige den aktuellen Ressourcenstand an, wenn der Benutzer "report" eingibt
        show_resource()

    elif eingabe in MENU:
        if is_resource_sufficient(eingabe):
            # Verarbeite die Münzeinwürfe, wenn genügend Ressourcen vorhanden sind
            money_recieved = process_coins()

            # Führe die Transaktion durch und bereite den Kaffee zu, wenn die Bezahlung erfolgreich war
            if make_transaction(MENU[eingabe]["cost"], money_recieved):
                make_coffee(eingabe)
    else:
        print("Invalid choice. Please select from espresso, latte, or cappuccino.")