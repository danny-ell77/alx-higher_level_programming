from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super(Rectangle, self).__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        return self.height * self.width

    def display(self):
        print("\n" * self.y, end='')
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args, **kwargs):
        if args is not None and len(args) > 0:
            self._update_with_args(args)
        else:
            self._update_with_kwargs(kwargs)

    def _update_with_args(self, args):
        props = ["id", "width", "height", "x", "y"]
        for prop, value in zip(props, args):
            setattr(self, prop, value)

    def _update_with_kwargs(self, kwargs):
        for key, value in kwargs.items():
            if key == "id" and value is None:
                self.__init__(self.width, self.height, self.x, self.y)
            if hasattr(self, key):
                setattr(self, key, value)

    def to_dictionary(self):
        return {'id': self.id, 'x': self.x, 'y': self.y, 'width': self.width, 'height': self.height}

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
