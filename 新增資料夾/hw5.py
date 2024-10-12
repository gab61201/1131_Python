def getTriangle(a, b, c):
    s, m, l = sorted([a,b,c])
    if l>=m+s or s<=0:
        print('not a triangle')
    elif s==m==l:
        print('equilateral triangle')
    elif s==m or m==l:
        print('isosceles triangle')
    elif l**2>m**2+s**2:
        print('obtuse triangle')
    elif l**2<m**2+s**2:
        print('acute triangle')
    elif l**2==m**2+s**2:
        print('right triangle')

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    getTriangle(a, b, c)

if __name__ == '__main__':
    main()