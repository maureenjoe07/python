#CREATING CLASSES.
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for quest in question_data:
    question_text = quest["text"]
    question_answer = quest["answer"]
    # print(question_answer)
    question_obj = Question(question_text, question_answer)
    # print(question_obj)
    question_bank.append(question_obj)

# print(question_bank)

quiz = QuizBrain(question_bank)


while quiz.still_has_questions() == True:
    quiz.next_question()
    quiz.all_answers()

       


