from models.rectangle import Rectangle

class Square(Rectangle):
    # This is the square class
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        # The overloading __str__ method - [Square] (<id>) <x>/<y> - <size>
        return '[{}] ({}) {}/{} - {}'.format(type(self).__name__, self.id, self.x, self.y, self.width)


