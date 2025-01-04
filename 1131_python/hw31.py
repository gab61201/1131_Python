def gray_code(n: int, k: int) -> str:
    if n == 1:
        return str(k)
    elif k < 2 ** (n - 1):
        return "0" + gray_code(n - 1, k)
    elif k >= 2 ** (n - 1):
        return "1" + gray_code(n - 1, 2**n - 1 - k)


def main():
    while True:
        user_input = input()
        if user_input == "-1":
            break
        n, k = [int(s) for s in user_input.split()]
        print(gray_code(n, k))


if __name__ == "__main__":
    main()
