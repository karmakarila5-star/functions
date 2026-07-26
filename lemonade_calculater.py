def greet_customer():
    print("welcome to the lemonade stand!")
    print("fresh lemonade, made just for you.")
greet_customer()
price_per_cup = float(input("enter the price per cup in dollars:"))
cups_sold = int(input("enter the number of cups sold:"))
def calculate_total(price, cups):
    total = price * cups
    return total
total_cost = calculate_total(price_per_cup, cups_sold)
round_total = round(total_cost, 2)
print("total cost:",round_total)
amount_paid = float(input("enter the amount paid by the customer:"))
def calculate_change(paid, total):
    change = paid - total
    return change
change_due = calculate_change(amount_paid,round_total)
rounded_change = round(change_due,2)
def thank_you_message(cups):
    if cups >= 5:
        return "wow, big order!thanks so much for your support!"
    else:
        return "thanks for stopping by the stand!"
closing_message =  thank_you_message(cups_sold)
print("")
print("===== lemonade stand receipt =====")
print("price per cup: ", price_per_cup)
print("cups sold:", cups_sold)
print("total cost:", round_total)
print("amount paid:", amount_paid)
print("change due:", rounded_change)
print(closing_message)
print("==============================================")
