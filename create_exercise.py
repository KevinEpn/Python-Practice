# Create_excercise.py
"""
Creates the initial structure for a Python excersice.
"""

# imports
import argparse
from pathlib import Path

# constants
TEMPLATE_DIR = Path("templates")


def parse_arguments() -> argparse.Namespace:
    """
    Parse command line arguments

    Returns:
        argparse.Namespace: The parsed command line arguments.
    """

    parser = argparse.ArgumentParser(description="Create a new exercise structure")
    parser.add_argument(
        "exercise_id", type=str, help="The ID of the exercise to create"
    )
    parser.add_argument(
        "exercise_name", type=str, help="The name of the exercise to create"
    )

    return parser.parse_args()


# functions
def create_exercise_directory(exercise_id: str, exercise_name: str) -> Path:
    """
    Create exercise directory.

    Args:
        exercise_id (str): The ID of the exercise to create.
        exercise_name (str): The name of the exercise to create.

    Returns:
        Path: Created exercise directory.
    """
    exercise_path = Path("exercises") / f"{exercise_id}_{exercise_name}"
    exercise_path.mkdir(parents=True, exist_ok=True)
    return exercise_path


def load_template(template_name: str) -> str:
    """
    Load template content

    Args:
        template_name: Name of the template file.

    Returns:
        str: The content of the template.
    """

    template = TEMPLATE_DIR / template_name

    return template.read_text(encoding="utf-8")


def render_template(template: str, variables: dict[str, str]) -> str:
    """
    Render template with variables

    Args:
        template: Template content.
        variables: Dictionary of variables to replace in the template.

    Returns:
        str: The rendered template content.
    """

    for key, value in variables.items():
        template = template.replace(f"{{{{{key}}}}}", value)

    return template


def main() -> None:
    """
    Application entry point
    """

    args = parse_arguments()

    exercise_path = create_exercise_directory(args.exercise_id, args.exercise_name)

    variables = {"EXERCISE_ID": args.exercise_id, "EXERCISE_NAME": args.exercise_name}

    print("Exercise Generator")
    print()
    print(f"Exercise ID: {args.exercise_id}")
    print(f"Exercise Name: {args.exercise_name}")
    print()
    print("Exercise created successfully!")
    print()
    print("Location:")
    print(exercise_path)

    # Temporary test for template loading
    template = load_template("metadata.json.tpl")
    content = render_template(template, variables)
    print(content)


if __name__ == "__main__":
    main()
