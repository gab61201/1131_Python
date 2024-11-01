def getTriangle(s, m, l) -> str:
    if l >= m + s or s <= 0:
        return "not a triangle"
    elif s == m == l:
        return "equilateral triangle"
    elif s == m or m == l:
        return "isosceles triangle"
    elif l**2 > m**2 + s**2:
        return "obtuse triangle"
    elif l**2 < m**2 + s**2:
        return "acute triangle"
    elif l**2 == m**2 + s**2:
        return "right triangle"


def area(a, b, c) -> float:
    if c >= a + b or a <= 0:
        return None
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5


def output(triangles: list, areas: list, amount: int):
    for i in range(amount):
        print(triangles[i], f"{areas[i]:.2f}" if areas[i] else "")
    areas = [a for a in areas if a]
    if areas:
        print(f"{max(areas):.2f}\n{min(areas):.2f}")
    else:
        print("All inputs are not triangles!")


def main():
    triangles, areas, amount = list(), list(), int(input())
    for _ in range(amount):
        a, b, c = sorted(int(num) for num in input().split())
        triangles.append(getTriangle(a, b, c))
        areas.append(area(a, b, c))
    output(triangles, areas, amount)


if __name__ == "__main__":
    main()
