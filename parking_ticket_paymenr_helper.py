def process_ticket_payment():
    ticket_cost = float(input("Please enter the ticket price ($): "))
    total_paid = 0

    print(f"Ticket cost is ${ticket_cost:.2f}. Valid coins are 0.05, 0.10, 0.25, 1.00.")

    while True:
        coin_input = input("Please enter a coin: $")
        coin = float(coin_input)

        if coin not in [0.05, 0.10, 0.25, 1.00]:
            print("Invalid coin denomination. Skipping.")
            continue

        total_paid += coin
        print(f"Accepted ${coin:.2f}. Total paid so far: ${total_paid:.2f}")

        if total_paid >= ticket_cost:
            print("Ticket fully paid!")
            break

    change = total_paid - ticket_cost

    if change > 0:
        return change
    elif change == 0:
        pass
    else:
        return 0

    return 0


returned_change = process_ticket_payment()

if returned_change > 0:
    print(f"Please take your change: ${returned_change:.2f}")
else:
    print("Exact amount received. No change needed.")