import subprocess
import inquirer
print("Welcome to QuizMyBalls! (CTRL + C to quit)")
#print("Select the quiz you want to do!")
#print("1. Am I Freaky?")
questions = [
  inquirer.List('quiz',
                message="Select the quiz you want to do! More quizzes coming soon.",
                choices=['1. Am I Freaky?', '2. Am I Gay?'],
            ),
]
answers = inquirer.prompt(questions)
if (answers['quiz'] == "1. Am I Freaky?"):
    subprocess.call(["python", "quizzes/1.py"], shell=True)
elif (answers['quiz'] == "2. Am I Gay?"):
    subprocess.call(["python", "quizzes/2.py"], shell=True)