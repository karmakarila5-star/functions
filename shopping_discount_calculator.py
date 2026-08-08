while True:
    try:
        raw_price = input("Enter the total bill amount: ")
        price = float(raw_price)
        if price < 0:
            raise ValueError("Price cannot be negative.")

        raw_discount = input("Enter the discount percentage (0-100): ")
        discount = float(raw_discount)
        if not (0 <= discount <= 100):
            raise ValueError("Discount must be between 0 and 100.")

    except ValueError as e:
        print(f"Invalid Numeric Value: {e}\n Please try again.\n")
    except TypeError as e:
        print(f"Data Type Error: {e}\n Please try again.\n")
    else:
        final_price = price - (price * (discount / 100))
        print(f"\n--- Bill Summary ---")
        print(f"Original Price: ${price:.2f}")
        print(f"Discount Applied: {discount}%")
        print(f"Final Total: ${final_price:.2f}\n")
        break
    finally:
        print("Input processing iteration completed.")

print("Thank you for using the shopping discount tool!")