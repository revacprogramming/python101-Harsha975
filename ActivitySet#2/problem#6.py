
class Menu:
    def __init__(self):
      self.list=[]
    def add(self,food,price):
      self.list.append((food,price))
    def show(self):
      for a,b in self.list:
        print(a,b)


m = Menu()
m.add("idly", 10)
m.add("vada", 20)
m.show()
.