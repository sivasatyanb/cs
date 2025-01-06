import random
import datetime

class Robot:
    def __init__(self, name):
        self.name = name
        self.phrase = ['Merry Christmas!', 'I\'m not a mug!', 'Homework!', 'Penguins!', 'Angry with hornsy!'][random.randint(0, 4)]
    
    def sayPhrase(self):
        return self.phrase
    
    def shoutPhrase(self):
        return (self.phrase).upper()
    
    def reversePhrase(self):
        return self.phrase[::-1]
    
class UberRobot(Robot):
    def _init__(self, name, phrase, car):
        super().__init__(name, phrase)
        self.car = car
    
    def sayPhrase(self):
        return chr(random.randint(97, 122)) + super().sayPhrase()
    
    def shoutPhrase(self):
        return chr(random.randint(65, 90)) + super().shoutPhrase()
    
    def reversePhrase(self):
        return chr(random.randint(33, 47)) + super().reversePhrase()
    
tesla = UberRobot('DaGoodLookingJuan')

print(tesla.reversePhrase())

print(datetime.date(2024, 12, 17))