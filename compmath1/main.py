import math


def display_menu():
    print("\n" + "=" * 50)
    print("   COMPUTATIONAL MATHEMATICS: ROOT-FINDING METHODS")
    print("=" * 50)
    print("1. Bisection Method")
    print("   Formula: c = (a + b) / 2")
    print("-" * 50)
    print("2. False Position Method (Regula Falsi)")
    print("   Formula: c = b - (f(b)*(b - a)) / (f(b) - f(a))")
    print("-" * 50)
    print("3. Fixed-Point Iteration")
    print("   Formula: x_{n+1} = g(x_n)")
    print("-" * 50)
    print("4. Newton-Raphson Method")
    print("   Formula: x_{n+1} = x_n - f(x_n) / f'(x_n)")
    print("-" * 50)
    print("5. Secant Method")
    print("   Formula: x_{n+1} = x_n - f(x_n)*(x_n - x_{n-1}) / (f(x_n) - f(x_{n-1}))")
    print("-" * 50)
    print("6. Muller's Method")
    print("   Formula: Quadratic interpolation through 3 points")
    print("=" * 50)


def main():
    while True:
        display_menu()
        choice = input("Select a method to run (1-6) or 'q' to quit: ").strip().lower()

        if choice == '1':
            print("\n>>> Running Bisection Method...")
            # import Bisection_Method (ensure filename matches)
        elif choice == '2':
            print("\n>>> Running False Position Method...")
        elif choice == '3':
            print("\n>>> Running Fixed-Point Method...")
        elif choice == '4':
            print("\n>>> Running Newton-Raphson Method...")
        elif choice == '5':
            print("\n>>> Running Secant Method...")
        elif choice == '6':
            print("\n>>> Running Muller's Method...")
        elif choice == 'q':
            print("Exiting. Good luck with your lab!")
            break
        else:
            print("Invalid selection. Please try again.")


if __name__ == '__main__':
    main()