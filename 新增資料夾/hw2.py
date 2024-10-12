import math


def main():
    a = int(input())
    b = int(input())
    c = int(input())
    root1 = ((-b)+math.sqrt(b*b-4*a*c))/(2*a)
    root2 = ((-b)-math.sqrt(b*b-4*a*c))/(2*a)
    print('%.1f'%root1)
    print('%.1f'%root2)


if __name__ == '__main__':
    main()