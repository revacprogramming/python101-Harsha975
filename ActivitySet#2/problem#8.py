

class Menu:
  def __setitem__(self,key,value):
    self.__dict__[key]=value
  def __str__(self):
    return  ('\n'.join([str(a+' '+str(b)) for a,b in self.__dict__.items()]))

m = Menu()
m["idly"] = 10
m["vada"] = 20

print(m)

