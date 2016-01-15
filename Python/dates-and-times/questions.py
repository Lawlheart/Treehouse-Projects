class Question:
    answer = None
    text = None

    def __str__(self):
        return self.text


class Add(Question):
    def __init__(self, num1, num2):
        self.text = "{} + {}".format(num1, num2)
        self.answer = num1 + num2


class Multiply(Question):
    def __init__(self, num1, num2):
        self.text = "{} * {}".format(num1, num2)
        self.answer = num1 * num2


class Subtract(Question):
    def __init__(self, num1, num2):
        self.text = "{} - {}".format(num1, num2)
        self.answer = num1 - num2


class Divide(Question):
    def __init__(self, num1, num2):
        self.text = "{} / {}".format(num1, num2)
        self.answer = num1 / num2
