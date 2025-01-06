class Player:
    def __init__(self, first: str, last: str, rating: int):
        self.first = first
        self.last = last
        self.rating = rating
    
    def generateEmail(self):
        return '{}.{}@lichess.org'.format(self.first, self.last)
    
    def playerInfo(self):
        return '{} {} {}'.format(self.first, self.last, self.rating)