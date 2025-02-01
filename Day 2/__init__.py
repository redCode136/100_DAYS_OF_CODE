def tbill(bill, percentage):
    totbill = 0
    totbill = round(bill + (bill * percentage / 100),2)
    print(f"The totalBill is {totbill}")
    return totbill


print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?"))
percentage = float(input("What percentage of tip would you like to give?"))
totalbill=tbill(bill, percentage)
numPeople = int(input("How many people to split the bill?"))
bill_p_person=round(totalbill/numPeople,2)
print(f"Each person should pay :{bill_p_person}")