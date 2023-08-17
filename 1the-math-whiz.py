import random
import time

class MathWhiz:
    """
    A class to play the Math Whiz game at different proficiency levels.

    Attributes:
        proficiency_levels (list): List of available proficiency levels.
        questions_asked (int): Number of questions asked during the game.
        questions_correct (int): Number of correct answers provided by the user.

    Methods:
        display_intro(): Display the title of the game.
        welcome_user(): Welcome the user and provide game instructions.
        get_user_proficiency_level(): Get the user's chosen proficiency level.
        generate_question(level): Generate a question based on the user's proficiency level.
        generate_beginner_question(): Generate a beginner-level math question.
        generate_intermediate_question(): Generate an intermediate-level math question.
        generate_advanced_question(): Generate an advanced-level math question.
        ask_question(level): Ask a generated question to the user and validate the answer.
        report(): Provide a report on the user's performance.
        run(): Run the Math Whiz game.

    Usage:
        math_whiz = MathWhiz()
        math_whiz.run()
    """

    proficiency_levels = ['Beginner', 'Intermediate', 'Advanced']

    def __init__(self):
        """
        Initialize attributes for the MathWhiz object.
        """
        self.questions_asked = 0
        self.questions_correct = 0

    @staticmethod
    def display_intro():
        """
        Display the title of the game.
        """
        title = "** The Math Whiz **"
        print("*" * len(title))
        print(title)
        print("*" * len(title))

    def welcome_user(self):
        """
        Welcome the user and provide game instructions.
        """
        self.name = input("Enter your name: ")
        print(f"Hello {self.name}. Welcome to Math Whiz. Let's help you become a Math Whiz")
        print("Instructions: I will ask you a math question with four possible answers.")
        print("Enter the letter of your answer. You can quit at any time by typing 'quit'.")
        input("Press enter when you're ready to start.")

    def get_user_proficiency_level(self):
        """
        Get the user's chosen proficiency level.

        Returns:
            str: The selected proficiency level.
        """
        print("What proficiency level would you like to learn today?")
        for i, level in enumerate(self.proficiency_levels, 1):
            print(f"{i}. {level}")

        choice = input("Enter the number of your proficiency level choice: ")
        while not choice.isdigit() or int(choice) not in range(1, len(self.proficiency_levels) + 1):
            print("Invalid choice. Please enter a valid number.")
            choice = input("Enter the number of your proficiency level choice: ")

        proficiency_choice = int(choice)
        selected_level = self.proficiency_levels[proficiency_choice - 1]
        print(f'You selected "{selected_level}" proficiency level. Here are the available questions:')

        return selected_level

    @staticmethod
    def generate_question(level):
        """
        Generate a question based on the user's proficiency level.

        Args:
            level (str): The proficiency level.

        Returns:
            tuple: A tuple containing num1, operation, num2, correct_answer, and shuffled answers.
        """
        if level == 'Beginner':
            return MathWhiz.generate_beginner_question()
        elif level == 'Intermediate':
            return MathWhiz.generate_intermediate_question()
        else:  # Advanced
            return MathWhiz.generate_advanced_question()

    @staticmethod
    def generate_beginner_question():
        """
        Generate a beginner-level math question.

        Returns:
            tuple: A tuple containing num1, operation, num2, correct_answer, and shuffled answers.
        """
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operation = random.choice(['+', '-', '*', '/'])

        if operation == '+':
            correct_answer = num1 + num2
        elif operation == '-':
            correct_answer = num1 - num2
        elif operation == '*':
            correct_answer = num1 * num2
        else:  # Division
            correct_answer = num1 // num2

        incorrect_answers = [correct_answer + random.randint(1, 5) for _ in range(3)]

        answers = [correct_answer] + incorrect_answers
        random.shuffle(answers)

        return num1, operation, num2, correct_answer, answers

    @staticmethod
    def generate_intermediate_question():
        """
        Generate an intermediate-level math question.

        Returns:
            tuple: A tuple containing num1, operation, num2, correct_answer, and shuffled answers.
        """
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        operation = random.choice(['+', '-', '*', '/'])

        if operation == '+':
            correct_answer = num1 + num2
        elif operation == '-':
            correct_answer = num1 - num2
        elif operation == '*':
            correct_answer = num1 * num2
        else:  # Division
            correct_answer = num1 // num2

        incorrect_answers = [correct_answer + random.randint(1, 10) for _ in range(3)]

        answers = [correct_answer] + incorrect_answers
        random.shuffle(answers)

        return num1, operation, num2, correct_answer, answers

    @staticmethod
    def generate_advanced_question():
        """
        Generate an advanced-level math question.

        Returns:
            tuple: A tuple containing num1, operation, num2, correct_answer, and shuffled answers.
        """
        num1 = random.randint(1, 20)
        operation = random.choice(['+', '-', '*', '/'])

        if operation == '+':
            num2 = random.randint(1, 20)
            correct_answer = num1 + num2
        elif operation == '-':
            num2 = random.randint(1, 20)
            correct_answer = num1 - num2
        elif operation == '*':
            num2 = random.randint(1, 10)
            correct_answer = num1 * num2
        else:  # Division
            num2 = random.randint(1, 10)
            correct_answer = num1 // num2

        incorrect_answers = [correct_answer + random.randint(1, 10) for _ in range(3)]

        answers = [correct_answer] + incorrect_answers
        random.shuffle(answers)

        return num1, operation, num2, correct_answer, answers

    def ask_question(self, level):
        """
        Ask a generated question to the user and validate the answer.

        Args:
            level (str): The proficiency level.

        Returns:
            str: 'quit' if user wants to quit, None otherwise.
        """
        num1, operation, num2, correct_answer, answers = self.generate_question(level)
        print(f"Problem: {num1} {operation} {num2} = ?")
        options = ['A', 'B', 'C', 'D']
        for i in range(4):
            print(f"{options[i]}. {answers[i]}")

        if level == 'Intermediate' or level == 'Advanced':
            time_limit = 15 if level == 'Intermediate' else 10
            start_time = time.time()

        user_answer = input("Enter the letter of your answer: ")
        if user_answer.lower() == 'quit':
            return 'quit'
        correct_option = options[answers.index(correct_answer)]

        if user_answer.upper() == correct_option:
            self.questions_correct += 1
            print(f"Correct answer, {self.name}. Keep it up!")
        else:
            print(f"Sorry, {self.name}. The correct answer was {correct_option}. Try again next time.")

        self.questions_asked += 1

        if level == 'Intermediate' or level == 'Advanced':
            end_time = time.time()
            elapsed_time = end_time - start_time
            if elapsed_time > time_limit:
                print("Time's up! You took too long to answer this question.")

    def report(self):
        """
        Provide a report on the user's performance.
        """
        print(f"You answered {self.questions_correct} out of {self.questions_asked} questions correctly.")

    def run(self):
        """
        Run the Math Whiz game.
        """
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
    math_whiz = MathWhiz()
    math_whiz.run()
