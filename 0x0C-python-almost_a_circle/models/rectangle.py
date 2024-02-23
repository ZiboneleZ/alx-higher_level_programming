from models.base import Base

class Rectangle(Base):
    # This is the claass of - 2.First Rectangle

    def __init__(self, width, height, x=0, y=0, id=None):
        #This is aa constructor
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    #This is the validation handling - 3.Validate attributes
    
    @property
    def width(self):
        # Width of a rectangle
        return self.__width

    @width.setter
    def width(self, value):
        self.validator("width", value, False)
        self.__width = value

    @property
    def height(self):
        # Height of the rectangle
        return self.__height

    @height.setter
    def height(self, value):
        self.validator("height", value, False)
        self.__height = value

    @property
    def x(self):
        # X of rectangle
        return self.__x

    @x.setter
    def x(self, value):
        self.validator("x", value)
        self.__x = value

    @property
    def y(self):
        # Y of rectangle
        return self.__y

    @y.setter
    def y(self, value):
        self.validator("y", value)
        self.__y = value


    #This is a validator
    def validator(self, name, value, eq=True):
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if not eq and value <= 0:
            raise ValueError(f"{name} must be > 0")
        elif eq and value < 0:
            raise ValueError(f"{name} must be >= 0")
    
    # This is the 4.Area First
    def area(self):
        # This will give the area of the rectangle
        return self.width * self.height

    # This is 5. Display #0
    def display(self):
        # This will print #
        hash_printer = '\n' * self.y + \
                (' ' * self.x + '#' * self.width + '\n') * self.height
        print(hash_printer, end='')

    def __str__(self):
        # Overriding the __str__
        return '[{}] ({}) {}/{} - {}/{}'.\
                format(type(self).__name__, self.id, self.x, self.y,self.width, self.height)

