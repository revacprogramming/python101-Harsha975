def add(a, b):
  sum=a+b
  return sum


def main():
    a = int(input('enter the number'))
    b =  int(input('enter the number'))

    c = add(a, b)
    print  ("sum of {} + {}   is {}".format(a,b,c))
main()