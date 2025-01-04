from itertools import combinations

drone_list = []
for drone in range(int(input())):
    new_drone = [int(i) for i in input().split()]
    drone_list.append({"number": new_drone[0], "coordinate": new_drone[1:]})

distance = lambda a, b: (
    (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2
) ** (1 / 2)

drone_distance = []
for drone_a, drone_b in combinations(drone_list, 2):
    distance_info = [
        drone_a,
        drone_b,
        distance(drone_a["coordinate"], drone_b["coordinate"]),
    ]
    drone_distance.append(distance_info)

drone_distance = sorted(drone_distance, key=lambda x: x[2])
for drone_a, drone_b, d in drone_distance[:3]:
    print(
        drone_a["number"],
        drone_b["number"],
        drone_a["coordinate"][0],
        drone_a["coordinate"][1],
        drone_a["coordinate"][2],
        drone_b["coordinate"][0],
        drone_b["coordinate"][1],
        drone_b["coordinate"][2],
    )
