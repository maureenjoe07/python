class QuizBrain:

    def __init__(self, question_list):
        self.question_num = 0
        self.my_score = 0
        self.question_list = question_list

    def still_has_questions(self):
        if self.question_num < len(self.question_list):
            return True
        else:
            print("You've completed the quiz!")
            print(f'Your final score is: {self.my_score}/{self.question_num}')
            return False
            
        
    def next_question(self):
        self.the_question = self.question_list[self.question_num]
        self.question_num += 1
        self.my_input = input(f'Q.{self.question_num}: {self.the_question.text} (True/False)?: ').title()

    def all_answers(self):
        the_answer= self.the_question.answer
        if self.my_input == the_answer:
            self.my_score += 1
            print(f'CORRECT!.....({self.my_score}/{self.question_num})')
            print('\n')
        else:
            print(f'INCORRECT!.....({self.my_score}/{self.question_num})')
            print('\n')