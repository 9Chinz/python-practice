from data import question_data
from question_model import Question
from quiz_game import QuizGame

question_list = []

for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(question_text, question_answer)
    question_list.append(new_question)

quiz = QuizGame(question_list)

while quiz.still_has_question():
    quiz.next_question()

print("You have completed the quiz")
print(f"You final score was: {quiz.score}")