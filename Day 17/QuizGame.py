from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank=[]
for x in question_data:
    question_bank.append(Question(x["text"],x["answer"]))

quiz_brain=QuizBrain(question_bank)


while quiz_brain.still_has_question():
    quiz_brain.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz_brain.score}/{quiz_brain.question_number}")