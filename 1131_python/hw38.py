def recursive(all_cave:list, start:str, visited:list = [], gold:int = 0):
    for cave in all_cave:
        if cave["name"] == start and cave["name"] not in visited:
            yield from recursive(all_cave, cave["des"][0], visited+[start], gold+cave["value"])
            yield from recursive(all_cave, cave["des"][1], visited+[start], gold+cave["value"])    
            yield gold + cave["value"]

def main():
    amount, start = input().split()
    cave = []
    for _ in range(int(amount)):
        num, value, des_1, des_2 = input().split()
        cave.append({"name": num, "value": int(value), "des": [des_1, des_2]})
    print(max(recursive(cave, start)))

if __name__ == "__main__":
    main()
