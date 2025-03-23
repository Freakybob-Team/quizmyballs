import inquirer
import subprocess
print("----------------------")
print("QuizMyBalls - Am I Gay?")
questions = [
  inquirer.List('gay',
                message="Are you attracted to men?",
                choices=['Yes', 'No', 'Maybe'],
            ),
]
answers = inquirer.prompt(questions)
if (answers['gay'] == "Yes"):
    print("You may be gay! (99%)")
elif (answers['gay'] == "No"):
    print("You may not be gay! (0%)")
else:
    print("You may be bisexual/pansexual! (50%)")
print("----------------------")
subprocess.call(["python", "src/quizmyballs.py"], shell=True)