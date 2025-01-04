def check_point(mat: list, side: int):
    point = 0
    for i in range(side):
        if all(mat[i::side]):
            point += 1
        if all(mat[i * side : i * side + side]):
            point += 1
    if all(mat[i * side + i] for i in range(side)):
        point += 1
    if all(mat[i * side - i] for i in range(1, side+1)):
        point += 1
    return point


def main():
    mat_side = int(input())
    circles = int(input())
    mat_a = input().split()
    mat_b = input().split()
    circled = input().split()

    mat_a = [n in circled for n in mat_a]
    mat_b = [n in circled for n in mat_b]
    score_a = check_point(mat_a, mat_side)
    score_b = check_point(mat_b, mat_side)
    if score_a > score_b:
        print("A Win")
    elif score_a < score_b:
        print("B Win")
    else:
        print("Tie")


if __name__ == "__main__":
    main()
