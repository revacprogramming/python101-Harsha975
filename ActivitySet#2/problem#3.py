

def get_cs():
    cs=input("enter the string")
    return cs


def cs_to_lot(cs):
    list=[]
    c=(cs.split(";"))
    for r in c:
      list.append(tuple(r.split('=')))
    return list


def main():
    
    cs = get_cs()
    lot = cs_to_lot(cs)
    print(lot)


if __name__ == '__main__':
    main().
