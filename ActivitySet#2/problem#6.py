
class Menu:
    # def __init__(self,food,price):
    #     self.food=food
    #     self.price=price
    def add(self,food,price):
        self.food=food
        self.price=price
    def show(self):
        print(self.food, self.price)



m = Menu()
m.add("idly", 10)
m.show()
m.add("vada", 20)
m.show()
