def main():
    n, turn = int(input()), input()
    turn = turn.count('R')-turn.count('L')
    for i in range(n):
        row_type = [range(1+i*n, 1+i*n +n, 1),#右轉0次
                    range(n**2-(n-i-1), i, -n),#右轉1次
                    range((n-i)*n, (n-i)*n -n, -1),#右轉2次
                    range(n-i, n**2-i+1, n)]#右轉3次
        for element in row_type[turn % 4]:
            print(element, end=' ')
        print()
main()