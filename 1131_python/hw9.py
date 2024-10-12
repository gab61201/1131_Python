def main():
    line_set = set()
    for _ in range(3):
        x1, x2 = int(input()), int(input())
        line_set |= {num for num in range(x1, x2)}
    print(len(line_set))

if __name__ == '__main__':
    main()
