import random

class MathWhiz:
    def __init__(self):
        # Initialize attributes for the user's name, proficiency levels, and counters for questions asked and correct answers.
        self.user_name = ""
        self.proficiency_levels = ['Beginner', 'Intermediate', 'Advanced']
        self.questions_asked = 0
        self.questions_correct = 0

        # Define the games for each proficiency level.
        self.games = {
            'Beginner': ['Number Operations (Arithmetic)', 'Addition', 'Subtraction', 'Multiplication', 'Division'],
            'Intermediate': ['Square Root of Numbers', 'Cubic Root of Numbers', 'Fractions', 'Probabilities', 'Decimals'],
            'Advanced': ['Algebraic Problem Solving', 'Equations', 'Inequalities', 'Simplification', 'Factoring']
        }

    def display_intro(self):
        title = "** The Math Whiz **"
        print("*" * len(title))
        print(title)
        print("*" * len(title))


    def welcome_user(self):
        # Ask for the user's name and provide instructions for the game.
        self.name = input("Enter your name: ")
        print(f"Hello {self.name}. Welcome to Math Whiz. Let's help you become a Math Whiz")
        print("Instructions: I will ask you a math question with four possible answers.")
        print("Enter the letter of your answer. You can quit at any time by typing 'quit'.")
        input("Press enter when you're ready to start.")

    def get_user_proficiency_level(self):
        # Ask the user to select a proficiency level and display available games for that level.
        print("What proficiency level would you like to learn today?")
        for i, level in enumerate(self.proficiency_levels, 1):
            print(f"{i}. {level}")

        # Validate user's choice.
        choice = input("Enter the number of your proficiency level choice: ")
        while not choice.isdigit() or int(choice) not in range(1, len(self.proficiency_levels) + 1):
            print("Invalid choice. Please enter a valid number.")
            choice = input("Enter the number of your proficiency level choice: ")

        proficiency_choice = int(choice)
        selected_level = self.proficiency_levels[proficiency_choice - 1]
        print(f'You selected "{selected_level}" proficiency level. Here are the available games:')
        
        # Display the games available for the selected proficiency level.
        for i, game in enumerate(self.games[selected_level], 1):
            print(f"{i}. {game}")

        return selected_level

    def generate_question(self, level):
        # Generate a random math question based on the user's selected proficiency level.
        if level == 'Beginner':
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            operation = random.choice(['+', '-'])
            correct_answer = num1 + num2 if operation == '+' else num1 - num2
        elif level == 'Intermediate':
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            operation = random.choice(['*', '/'])
            correct_answer = num1 * num2 if operation == '*' else round(num1 / num2, 2)
        else:  # Advanced
            num1 = random.randint(1, 10)
            operation = random.choice(['sqrt', 'cbrt'])
            if operation == 'sqrt':
                correct_answer = round(num1 ** 0.5, 2)
            else:
                correct_answer = round(num1 ** (1. / 3.), 2)

        # Generate three incorrect answers.
        incorrect_answers = random.sample([i for i in range(0, 21) if i != correct_answer], 3)

        # Combine correct and incorrect answers and shuffle them.
        answers = [correct_answer] + incorrect_answers
        random.shuffle(answers)

        return num1, operation, correct_answer, answers

    def ask_question(self, level):
        # Generate a question and ask it to the user.
        num1, operation, correct_answer, answers = self.generate_question(level)
        print(f"Problem: {num1} {operation} = ?")
        options = ['A', 'B', 'C', 'D']
        for i in range(4):
            print(f"{options[i]}. {answers[i]}")

        # Get the user's answer and validate it.
        user_answer = input("Enter the letter of your answer: ")
        if user_answer.lower() == 'quit':
            return 'quit'
        correct_option = options[answers.index(correct_answer)]

        # Provide feedback based on whether the user's answer was correct.
        if user_answer.upper() == correct_option:
            self.questions_correct += 1
            print(f"Correct answer, {self.user_name}. Keep it up!")
        else:
            print(f"Sorry, {self.user_name}. The correct answer was {correct_option}. Try again next time.")

        # Increment the count of questions asked.
        self.questions_asked += 1

    def report(self):
        # Report the user's score.
        print(f"You answered {self.questions_correct} out of {self.questions_asked} questions correctly.")

    def run(self):
        # The main game loop.
        self.display_intro()
        self.welcome_user()
        level = self.get_user_proficiency_level()
        while True:
            if self.ask_question(level) == 'quit':
                break
            if self.questions_asked % 10 == 0:
                self.report()
                continue_game = input("Do you want to continue? (yes/no): ")
                if continue_game.lower() != 'yes':
                    print("Thank you for playing Math Whiz. Goodbye!")
                    break

if __name__ == "__main__":
    # Start the game if the script is run directly.
    math_whiz = MathWhiz()
    math_whiz.run()

