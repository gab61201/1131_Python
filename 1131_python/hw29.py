def C(m, times=0):
    if m == 0 or m == 1:
        return times
    times += 1
    if m % 2 == 0:
        return C(m / 2, times)
    elif m % 2 == 1:
        return C((m + 1) / 2, times)


def main():
    while True:
        a = int(input(), 2)
        print(f"{C(a):04b}")
        if input() == "-1":
            break


if __name__ == "__main__":
    main()
