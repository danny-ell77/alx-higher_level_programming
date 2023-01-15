from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super(Square, self).__init__(id=id, x=x, y=y, width=size, height=size)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value

    def to_dictionary(self):
        return {'size': self.size, 'x': self.x, 'y': self.y, 'id': self.id}

    def update(self, *args, **kwargs):
        if args is not None and len(args) > 0:
            props = ["id", "size", "x", "y"]
            for prop, value in zip(props, args):
                setattr(self, prop, value)
        else:
            for key, value in kwargs.items():
                if key == "id" and value is None:
                    self.__init__(self.width, self.height, self.x, self.y)
                if hasattr(self, key):
                    setattr(self, key, value)

