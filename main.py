from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


'''
question_bank=[]
for i in question_data:
    question_bank.append(Question(i['text'],i['answer']))
'''

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz=QuizBrain(question_bank)

while quiz.still_has_question():
    continued=quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was : {quiz.score} / {quiz.question_number}")
# 다 틀렸을경우 점수가 없어서 출력이 안되었던거였음...

