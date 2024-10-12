def main():
    name = input()
    number = input()
    chinese = input()
    cs = input()
    programming = input()

    total = int(chinese) + int(cs) + int(programming)
    average = int(total / 3)

    print('Name:' + name)
    print('ID:' + number)
    print(f'Average:{average}')
    print('Total:' + str(total))


if __name__ == '__main__':
    main()