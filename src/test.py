
class Base(object):
    def __init__(self, x):
        self.x = x

    def format(self, x):
        return x

    def execute(self):
        y = self.format(self.x)
        print(y)

class Derived(Base):
    def __init__(self, x):
        super().__init__(x)

    def format(self, x):
        return x * 10

d = Derived(10)
d.execute()
