
def add(a, b):
    add=a+b
    return add


def output(a, b, add):
    print('{} + {} is {}'.format(a,b,add))


def main():
    a=int(input('enter the number'))
    b=int(input('enter the number'))
    sum = add(a, b)

    output(a, b, sum)


if __name__ == '__main__':
    main()
