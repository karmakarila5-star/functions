def calculate_bill(subtotal, tax_rate, tip_percentage):
    tax_amount = subtotal * tax_rate
    tip_amount = subtotal * tip_percentage
    total_bill = subtotal + tax_amount + tip_amount
    return round(total_bill, 2)


def calculate_seating(n):
    """Calculates unique seating arrangements for n people using recursion."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * calculate_seating(n - 1)


final_bill = calculate_bill(100, 0.08, 0.15)
print(f"Total Restaurant Bill: ${final_bill}")

people = 5
arrangements = calculate_seating(people)
print(f"Seating arrangements for {people} people: {arrangements}")

print(calculate_seating.__doc__)