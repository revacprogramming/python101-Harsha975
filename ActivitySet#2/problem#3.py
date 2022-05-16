

def get_cs():
    cs=input("enter the string")
    return cs


def cs_to_lot(cs):
    c=(cs.split("="))
    c=(c.split(";"))
    c=list(c)
    return c


def main():
    cs = get_cs()

    lot = cs_to_lot(cs)
    print(lot)


if __name__ == '__main__':
    main()
