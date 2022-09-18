from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from ascii import art

question_bank = []
for question in question_data:
    question["text"] = question["question"]
    question["answer"] = question["correct_answer"]
    questions = Question(question["text"], question["answer"])
    question_bank.append(questions)

print(art)
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print("You've completed the Quiz!")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")