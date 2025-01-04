def path(connection: set[frozenset], start: str, end: str, vector: list[str] = []):
    for way in connection:
        if start in way and start not in vector:
            yield from path(connection, set(way - {start}).pop(), end, vector + [start])
    if start == end:
        yield vector + [end]


def main():
    roads, start, end = input().split()
    middle = set(input().split())
    connection = set()
    for _ in range(int(roads)):
        way = frozenset(input().split())
        connection.add(way)

    possible_path = [p for p in path(connection, start, end) if middle & set(p)]
    if possible_path:
        min_path = min(possible_path, key=len)
        print((set(min_path) & middle).pop())
        print(" ".join(min_path))
    else:
        print("NO")


main()
