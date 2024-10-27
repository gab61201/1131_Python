def num_str(chars):
    string = str()
    for i in range(chars):
        string += str(i+1)
    for i in range(chars-1, 0, -1):
        string += str(i)
    return string

def rightTri(rows:int):
    for i in range(rows):
        print(num_str(i+1))

def triangle(rows:int):
    for i in range(1, rows+1):
        print('_'*(rows-i), num_str(i), '_'*(rows-i), sep='')

def revTriangle(rows:int):
    for i in range(rows):
        print('_'*(i), num_str(rows-i), '_'*(i), sep='')

def main():
    graph, rows = int(input()), int(input())
    if graph == 1:
        rightTri(rows)
    elif graph == 2:
        triangle(rows)
    elif graph == 3:
            revTriangle(rows)

if __name__ == '__main__':
    main()