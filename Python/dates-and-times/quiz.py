import datetime
import os
import random

from questions import Add, Multiply, Subtract

OPERATIONS = [Add, Multiply, Subtract]


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


class Quiz():
    questions = []
    answers = []
    times = []

    def __init__(self):
        for _ in range(0, 10):
            num1, num2 = random.randint(1, 10), random.randint(1, 10)
            question = random.choice(OPERATIONS)(num1, num2)
            self.questions.append(question)
        self.take_quiz()

    def timer(self, delta):
        output = ""
        if delta.days:
            output += "{}:".format(delta.days)
        hours = round(delta.seconds / 3600)
        minutes = round(delta.seconds % 3600 / 60)
        seconds = round(delta.seconds % 3600 % 60)
        return "{}:{}:{}".format(hours, minutes, seconds)

    def take_quiz(self):
        self.start_quiz = datetime.datetime.now()
        for i in range(0, len(self.questions)):
            question = self.questions[i]
            status = self.ask(question)
            self.answers.append(status)
            if status:
                print("Correct!")
            else:
                print("incorrect")
        self.stop_quiz = datetime.datetime.now()
        self.summary()

    def ask(self, question):
        start = datetime.datetime.now()
        print("________\n\n {} \n________".format(question.text))
        answer = input("> ")
        try:
            answer = int(answer)
        except ValueError:
            return self.ask(question)
        stop_question = datetime.datetime.now()
        print(self.timer(stop_question - self.start_quiz))
        self.times.append(stop_question - start)
        return answer == question.answer

    def get_score(self):
        raw_score = 0
        for i in range(0, len(self.answers)):
            if self.answers[i]:
                raw_score += 1
        percent = raw_score/len(self.answers)*100
        return "You scored {}%".format(round(percent))

    def quiz_review(self):
        print("\nSummary:")
        print("time   question    correct")
        for i in range(0, 10):
            time = self.timer(self.times[i])
            question = self.questions[i]
            status = self.answers[i]
            print("{}  {}\t-  {}".format(time, question, status))
        print()

    def summary(self):
        timer = self.timer(self.stop_quiz - self.start_quiz)
        print("_"*20)
        print("\nTotal time: {}".format(timer))
        print(self.get_score())
        print("_"*20 + "\n")
        if input("Would you like to review your answers? y/n ").lower() == 'y':
            self.quiz_review()


Quiz()
