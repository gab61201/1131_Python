def main():
    line_set = set()
    for _ in range(int(input())):
        x1, x2 = input().split()
        line_set.update(num for num in range(int(x1), int(x2)))
    print(len(line_set))

if __name__ == '__main__':
    main()
