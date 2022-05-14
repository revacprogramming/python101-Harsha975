
def add(a, b):
    sum=a+b
    return sum


def output(a, b, sum):
    print('{} + {} is {}'.format(a,b,sum))


def main():
    a=int(input('enter the number'))
    b=int(input('enter the number'))
    sum = add(a, b)

    output(a, b, sum)


if __name__ == '__main__':
    main()
