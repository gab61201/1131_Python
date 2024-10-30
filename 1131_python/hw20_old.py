def matrix(n:int)->list:
    matr = list()
    for row in range(0, n**2, n):
        matr.append([i+row+1 for i in range(n)])
    return matr

def turn_left(matr:list):
    output = list()
    for i in range(-1, -len(matr)-1, -1):
        output.append([m[i] for m in matr])
    return output

def turn_right(matr:list):
    output = list()
    for i in range(len(matr)):
        output.append([matr[m-1][i] for m in range(len(matr), 0, -1)])
    return output

def main():
    mat = matrix(int(input()))
    turns = input()
    for t in turns:
        if t == 'L':
            mat = turn_left(mat)
        elif t == 'R':
            mat = turn_right(mat)
    for row in mat:
        for i in row:
            print(i, end=' ')
        print()

if __name__ == '__main__':
    main()