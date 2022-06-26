class Menu:
    def __init__(self):
        self.list = []

    def __add__(self, a):
        self.list.append((a[0], a[1]))
        return self

    def __str__(self):
        return '{self.list[0][0]} {self.list[0][1]} \n{self.list[1][0]} {self.list[1][1]} '.format(self=self)


m = Menu()
m = m + ("idly", 10) + ("vada", 20)  # Hint: operator overloading special methods (__add__, __sub__, etc.)

print(m)  # should print the menu properly
