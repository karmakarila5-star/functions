def calculate_item_cost(price, quantity):
  return price * quantity


def calculate_tax(subtotal, tax_rate=0.05):
  return subtotal * tax_rate


def print_bill(item_name, price, quantity, subtotal, tax, total):
  print("\n--- ART SUPPLIES RECEIPT ---")
  print(f"Item: {item_name}")
  print(f"Price per unit: ${price:.2f}")
  print(f"Quantity: {quantity}")
  print("----------------------------")
  print(f"Subtotal: ${subtotal:.2f}")
  print(f"Tax (5%): ${tax:.2f}")
  print(f"Total Due: ${total:.2f}")
  print("----------------------------")
  print("Thank you for shopping!")


def main():
  item_name = "Sketchbook"
  unit_price = 12.50
  quantity = 3

  subtotal = calculate_item_cost(unit_price, quantity)
  tax = calculate_tax(subtotal)
  total = subtotal + tax

  print_bill(item_name, unit_price, quantity, subtotal, tax, total)


main()