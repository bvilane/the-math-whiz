class MathWhiz:
    def __init__(self):
        """Initialize MathWhiz class with user_name and proficiency_levels attributes."""
        self.user_name = ""
        self.proficiency_levels = ['Beginner', 'Intermediate', 'Advanced']
        self.games = {
            'Beginner': ['Number Operations (Arithmetic)', 'Addition', 'Subtraction', 'Multiplication', 'Division'],
            'Intermediate': ['Square Root of Numbers', 'Cubic Root of Numbers', 'Fractions', 'Probabilities', 'Decimals'],
            'Advanced': ['Algebraic Problem Solving', 'Equations', 'Inequalities', 'Simplification', 'Factoring']
        }

    def display_welcome_page(self):
        """Display the welcome page."""
        title = "** Welcome to The Math Quiz **"
        print("*" * len(title))
        print(title)
        print("*" * len(title))

    def get_user_name(self):
        """Prompt the user to input their name and display a welcome message."""
        self.user_name = input("Enter your name: ")
        print(f'Fantastic {self.user_name}! Learning is so much fun!')

    def get_user_proficiency_level(self):
        """Prompt the user to select a proficiency level and display available games."""
        print("What proficiency level would you like to learn today?")
        for i, level in enumerate(self.proficiency_levels, 1):
            print(f"{i}. {level}")

        choice = input("Enter the number of your proficiency level choice: ")
        while not choice.isdigit() or int(choice) not in range(1, len(self.proficiency_levels) + 1):
            print("Invalid choice. Please enter a valid number.")
            choice = input("Enter the number of your proficiency level choice: ")

        proficiency_choice = int(choice)
        selected_level = self.proficiency_levels[proficiency_choice - 1]
        print(f'You selected "{selected_level}" proficiency level. Here are the available games:')
        for i, game in enumerate(self.games[selected_level], 1):
            print(f"{i}. {game}")


if __name__ == "__main__":
    # Create an instance of MathWhiz class
    math_whiz = MathWhiz()

    # Display the welcome page
    math_whiz.display_welcome_page()

    # Prompt the user to input their name
    math_whiz.get_user_name()

    # Prompt the user to select a proficiency level and display available games
    math_whiz.get_user_proficiency_level()

