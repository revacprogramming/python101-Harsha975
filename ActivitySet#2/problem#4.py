

def get_cs():
    return input("enter string\n")

def cs_to_lot(cs):
  lst=[]
  r=cs.split(";")
  for w in r:
    lst.append(tuple(w.split("=")))
  return lst


def lot_to_cs(lot):
    r=''
    for a,b in lot:
      r=r+a+'='+b+';'
    return r[:-1]


def main():
    cs=get_cs()

    lot=cs_to_lot(cs)  
    print(lot)

    cs=lot_to_cs(lot)  # convert list of strings to connect string
    print(cs)


if __name__ == '__main__':
    main()
