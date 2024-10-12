def bmi(h,w):
    bmi = w / (h**2)
    bmi3 = format(bmi, '.3f')
    if bmi3[-1] == '5' and int(bmi3[-2]) % 2 == 1:
        bmi += 0.01
    return format(bmi, '.3f')[:-1]


def main():
    height = float(input())
    weight = int(input())
    print(bmi(height, weight))


if __name__ == '__main__':
    main()