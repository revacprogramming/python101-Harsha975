

def get_cs():
  return input("enter string\n")


def cs_to_dict(cs):
  ditc={}
  r=cs.split(";")
  for d in r:
    lst=d.split("=")
    ditc[lst[0]]=lst[1]
  return ditc
    
def dict_to_cs(d):
  b=""
  for a in d:
    b+=a+'='+d[a]+';'
  return b[:-1]


def main():
    cs = get_cs()

    d = cs_to_dict(cs) # convert connect string to a dictionary
    print(d)

    cs = dict_to_cs(d)
    print(cs)


if __name__ == '__main__':
    main()
