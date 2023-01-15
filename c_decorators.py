
class DecoratorReg:

    decorated_classes = []

    def __init__(self, cls):
        self.cls = cls

    def __call__(self, *args, **kwargs):
        if self.cls not in self.decorated_classes:
            self.decorated_classes.append(self.cls)
        return self.cls(*args, **kwargs)


def add_str(string):

    def decor_str(cls):

        def inner_str(*args, **kwargs):
            return f"{string}{str(cls(*args, **kwargs))}"

        return inner_str

    return decor_str


class Box:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def volume(self):
        return self.x * self.y * self.z

    @staticmethod
    def total_volume(box_1, box_2):
        return box_1.volume() + box_2.volume()

    def __str__(self):
        return f"{self.x}x{self.y}x{self.z}"
