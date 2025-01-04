population, days, new_confirmed = int(input()), int(input()), int(input())
infect, recoverDay, immuneRate = float(input()), int(input()), float(input())
confirmed = [0] * int(recoverDay)
get_infeted = 0
for day in range(days):
    confirmed.append(new_confirmed)
    get_infeted += new_confirmed
    recovered = confirmed.pop(0)
    print(
        day + 1,  # 第N天
        sum(confirmed),  # 當天總確診人數
        confirmed[-1],  # 新增確診人數
        recovered,  # 康復人數
    )
    # 計算明日新增確診人數
    immuneRate += recovered / population
    new_confirmed = int(sum(confirmed) * (1 - immuneRate) * infect / recoverDay)
    infectable = round(population*(1-immuneRate))
    # print(new_confirmed)
    if sum(confirmed) + new_confirmed > infectable:
        new_confirmed = infectable - sum(confirmed)
print(get_infeted)
