class QuizBrain:
    def __init__(self,q_list):
        self.question_number=0
        self.score=0
        self.question_list=q_list

    def check_answer(self,answer,ergebnis):
        if ergebnis==answer:
            self.score+=1
            print("You got it right!")
        else:
            print("You got it wrong.")
        print(f"The correct answer was: {answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
    def still_has_question(self):
        return self.question_number<len(self.question_list) #simplified return value


    def next_question(self):
        current_question=self.question_list[self.question_number].text
        current_answer = self.question_list[self.question_number].answer
        self.question_number+=1
        ergebnis=input((f"Q{self.question_number}: {current_question}. (True/False)"))
        self.check_answer(current_answer,ergebnis)



