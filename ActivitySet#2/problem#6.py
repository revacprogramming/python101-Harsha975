
class Menu:
    # def __init__(self):
      
    def add(self,food,price):
        self.food=food
        self.price=price
        self.list=list.append(self.food,self.price)
        print(list)
    # def show(self):
    #     # print(self.food, self.price)
    #   for i in globally(list):
    #     print(i)



m = Menu()
# food=input("")
# price=input("")
# m.add(food, price)
# m.show()
m.add("idly", 10)
m.add("vada", 20)
m.show()
