"""Command-line entry point for the BMI Analyzer.

Handles user input/validation and orchestrates the calculation,
persistence, and visualization layers. Run with:

    python main.py [--db path/to/database.db]
"""
import argparse

from bmi_logic import calculate_bmi, classify_bmi, convert_imperial_to_metric
from database import create_connection, save_entry, load_user_history
from visualization import show_summary, plot_history


def get_valid_name() -> str:
    """Prompt until a non-empty name is entered."""
    while True:
        name = input("Enter your name: ").strip()
        if name:
            return name
        print("Name cannot be empty.\n")


def get_weight_and_height() -> tuple[float, float]:
    """Prompt for weight/height in the user's chosen unit system.

    Returns:
        (weight_kg, height_m)

    Raises:
        ValueError: on an invalid unit choice or non-positive values.
    """
    unit = input("Choose unit system: [M]etric (kg, m) or [I]mperial (lbs, inches): ").strip().lower()

    if unit == "i":
        weight = float(input("Enter your weight (lbs): "))
        height = float(input("Enter your height (inches): "))
        weight, height = convert_imperial_to_metric(weight, height)
    elif unit == "m":
        weight = float(input("Enter your weight (kg): "))
        height = float(input("Enter your height (m): "))
    else:
        raise ValueError("Invalid unit system. Please choose 'M' for Metric or 'I' for Imperial.")

    if weight <= 0 or height <= 0:
        raise ValueError("Height and weight must be greater than 0.")

    return weight, height


def parse_args() -> argparse.Namespace:
    """Parse CLI arguments (currently just the database path)."""
    parser = argparse.ArgumentParser(description="Track and visualize BMI over time.")
    parser.add_argument(
        "--db",
        default="bmi_data.db",
        help="Path to the SQLite database file (default: bmi_data.db)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    conn = create_connection(args.db)
    name = get_valid_name()

    try:
        while True:
            try:
                weight, height = get_weight_and_height()
            except ValueError as e:
                print(f"{e}\n")
                continue

            bmi = calculate_bmi(weight, height)
            category = classify_bmi(bmi)

            print(f"\nBMI: {bmi:.2f} kg/m²")
            print(f"Category: {category}\n")

            save_entry(conn, name, weight, height, bmi, category)
            print("Data saved to the database.")

            user_history = load_user_history(conn, name)
            print("\nHistory of results:")
            print(user_history.to_string(index=False), "\n")
            show_summary(user_history)

            choice = input("Press [R] to repeat, [G] to see graph, or [E] to exit: ").strip().lower()

            if choice == "e":
                print("Leaving application.")
                break
            elif choice == "g":
                plot_history(load_user_history(conn, name), name)
            elif choice != "r":
                print("Invalid input.\n")
    except KeyboardInterrupt:
        print("\nInterrupted - exiting gracefully.")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
