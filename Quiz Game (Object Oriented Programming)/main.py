# Import Question class from question_model.py
from question_model import Question

# Import question list from data.py
from data import questions

# Import QuizBrain from quiz_brain.py
from quiz_brain import QuizBrain

# Import logo from logo.py
from logo import logo

# When you run the code first of all the logo will show
print(logo)

# Create an empty list to add questions
question_list = []

# The user should select a category to start
category = input("Please choose a category and type it down\n"
                 "History / Sports / Animals / Mythology / Geography\n").lower()

# Create questions by using Question class and add them to question_list
for question in questions:
    if question["category"].lower() == category:
        text = question["question"]
        answer = question["correct_answer"]
        new_question = Question(question=text, answer=answer)
        question_list.append(new_question)

# Create the quiz object by using QuizBrain class
quiz = QuizBrain(question_list)

# While loop will provide to continue the game
while quiz.still_has_questions():
    quiz.next_question()

# Warn to user and show them the final score
print("You've completed the quiz.")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")