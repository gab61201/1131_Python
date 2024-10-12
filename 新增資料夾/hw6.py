from math import sqrt

def main():
    a, b, c = [int(input()) for _ in range(3)]
    Discriminant = b*b-4*a*c
    if Discriminant >= 0:
        x1 = (-b+sqrt(Discriminant))/(2*a)
        x2 = (-b-sqrt(Discriminant))/(2*a)
        print('%.1f'%(x1))
        print('%.1f'%(x2))
    else:
        real_num = -b/(2*a)
        imag_num = sqrt(-Discriminant)/(2*a)
        print("%.1f+%.1fi"%(real_num,imag_num))
        print("%.1f-%.1fi"%(real_num,imag_num))

if __name__ == "__main__":
    main()