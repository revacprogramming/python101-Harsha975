
class Menu():
  def __setitem__(self,key,value):
    self.__dict__[key]=value



class Order:
  def __setitem__(self):
    


class Bill:
    """fill in class definition here"""


m = Menu()
m["idly"] = 20
m["vada"] = 20


o = Order(m)
try:
    o["vada"] = 2
    o["pongal"] = 2

except KeyError as e:
    print(e)

# b = Bill(m, o)
# print(b)
