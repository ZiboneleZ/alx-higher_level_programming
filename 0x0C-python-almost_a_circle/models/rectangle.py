from models.base import Base

class Rectangle(Base):
    ''' This is the claass of - 2.First Rectangle'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''This is aa constructor'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y


