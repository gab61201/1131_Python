def tree_recursion(graph: list, start: str, end: str, visited: list = [], branch: list = [], total_value: int=0):
    for vector in graph:
        if vector["start"] == start and vector["end"] not in visited:
            yield from tree_recursion(graph, vector["end"], end, visited + [start], branch+[vector], total_value + vector["value"])
    if start == end:
        yield {"path": visited + [start], "value": total_value}

def main():
    graph = []
    nodes = input()
    while True:
        user_input = input()
        if user_input == "-1":
            break
        data = user_input.split()
        value = int(data[2])
        for g in graph:
            if g["start"] == data[1] and g["end"] == data[0]:
                value = min(value, g["value"])
                g["value"] = value
                break
        graph.append({"start": data[0], "end": data[1], "value": value})

    connections = list(tree_recursion(graph, "A", "B"))
    shortest_path = sorted(connections, key=lambda x: len(x["path"]))[0]
    max_familiarity = sorted(connections, key=lambda x: x["value"])[-1]
    print(len(shortest_path["path"]) - 1)
    print(" ".join(shortest_path["path"]))
    print(max_familiarity["value"])
    print(" ".join(max_familiarity["path"]))

if __name__ == "__main__":
    main()