def R(m, times=0):
    if m == 0 or m == 1:
        return times
    times += 1
    if m % 2 == 0:
        return R(m / 2, times)
    elif m % 2 == 1:
        return R((m + 1) / 2, times)


def main():
    while True:
        user_input = input()
        if user_input == "-1":
            break
        code = int(user_input, 2)
        T = sum(R(n + 1) for n in range(code))
        print(f"{T:014b}")


if __name__ == "__main__":
    main()
