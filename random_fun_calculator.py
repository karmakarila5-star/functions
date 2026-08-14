import math
import random


def show_menu():
    print("\n" + "=" * 40)
    print("      ✨ THE RANDOM FUN CALCULATOR ✨      ")
    print("=" * 40)
    print("1. Generate a Lucky Number (random)")
    print("2. Choose a Random Activity (random)")
    print("3. Play the Number Guessing Game (random)")
    print("4. Explore Math Functions (math)")
    print("5. Exit")
    print("=" * 40)


def fun_math_explorations():
    print("\n--- 🧮 Math Module Exploration ---")

    num = float(input("Enter a decimal number (e.g., 4.3 or -2.7): "))
    print(f"👉 math.ceil({num}): {math.ceil(num)} (Rounds UP to nearest integer)")
    print(
        f"👉 math.floor({num}): {math.floor(num)} (Rounds DOWN to nearest integer)"
    )

    print(
        f"👉 math.fabs({num}): {math.fabs(num)} (Absolute value as a float)"
    )

    print("\n--- Testing copysign ---")
    base = float(input("Enter a base number: "))
    sign_source = float(input("Enter a number to copy the sign from (+ or -): "))
    result_sign = math.copysign(base, sign_source)
    print(
        f"👉 math.copysign({base}, {sign_source}): {result_sign} (Gives {base} the sign of {sign_source})"
    )

    print("\n--- Testing Greatest Common Divisor (GCD) ---")
    int1 = int(input("Enter first integer: "))
    int2 = int(input("Enter second integer: "))
    print(
        f"👉 math.gcd({int1}, {int2}): {math.gcd(int1, int2)} (Highest common factor)"
    )


def guessing_game():
    print("\n--- 🎲 Number Guessing Game ---")
    secret_number = random.randint(1, 20)
    attempts = 0
    print("I am thinking of a number between 1 and 20.")

    while True:
        try:
            guess = int(input("Take a guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low!")
            elif guess > secret_number:
                print("Too high!")
            else:
                print(
                    f"🎉 Correct! You guessed it in {attempts} attempts!"
                )
                break
        except ValueError:
            print("Please enter a valid integer.")


def main():
    activities = [
        "Go for a 15-minute walk outside 🏃‍♂️",
        "Read a chapter of a book 📚",
        "Code a brand new feature 💻",
        "Drink a large glass of water 💧",
        "Do 10 jumping jacks 🤸‍♂️",
        "Listen to your favorite song 🎵",
    ]

    while True:
        show_menu()
        choice = input("Select an option (1-5): ").strip()

        if choice == "1":
            lucky_num = random.randint(1, 100)
            print(f"\n🔮 Your lucky number for today is: {lucky_num}")

        elif choice == "2":
            activity = random.choice(activities)
            print(f"\n🎯 Suggested Activity: {activity}")

        elif choice == "3":
            guessing_game()

        elif choice == "4":
            fun_math_explorations()

        elif choice == "5":
            print("\nThank you for using the Random Fun Calculator! Goodbye! 👋")
            break
        else:
            print("\n❌ Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()