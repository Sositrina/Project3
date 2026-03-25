class Mixin:
    def __repr__(self):
        """Выводит информацию о создаваемом объекте"""
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(repr(self))