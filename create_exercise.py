# Create_excercise.py
"""
Creates the initial structure for a Python excersice.
"""

# imports
import argparse

# constants
def parse_arguments() -> argparse.Namespace:
    """
    Parse command line arguments
    """

    parser = argparse.ArgumentParser(description="Create a new exercise structure")
    parser.add_argument("exercise_id", type=str, help="The ID of the exercise to create")
    parser.add_argument("exercise_name", type=str, help="The name of the exercise to create")

    return parser.parse_args()


# functions
def main() -> None:
    """
    Appication entry point
    """

    args = parse_arguments()

    print("Exercise Generator")
    print()
    print(f"Exercise ID: {args.exercise_id}")
    print(f"Exercise Name: {args.exercise_name}")


if __name__ == "__main__":
    main()
