import inquirer
import subprocess
print("----------------------")
print("QuizMyBalls - Am I Freaky?")
questions = [
  inquirer.List('freaky',
                message="Are you freaky?",
                choices=['Yes', 'No'],
            ),
]
answers = inquirer.prompt(questions)
if (answers['freaky'] == "Yes"):
    print("You are Freaky! (100%)")
else:
    print("You aren't Freaky! (0%)")
print("----------------------")
subprocess.call(["python", "src/quizmyballs.py"], shell=True)