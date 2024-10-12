def best_plan(used:list):
    plan_183 = [0.08, 0.139, 0.135, 1.128, 1.483, 1, 250, 183]
    plan_383 = [0.07, 0.130, 0.121, 1.128, 1.483, 3, 200, 383]
    plan_983 = [0.06, 0.108, 0.101, 1.128, 1.483, 5, 150, 983]
    plan_1283 = [0.05, 0.100, 0.090, 1.128, 1.483, float('inf'), 0, 1283]
    price_dict = dict()
    for plan in [plan_183, plan_383, plan_983, plan_1283]:
        price = 0
        plan_name = str(plan[-1])
        used_data = used[-1]
        for item in range(5):
            price += plan[item] * used[item]
        if used_data > plan[-3]:
            price += (used_data-plan[-3])*plan[-2]
        price_dict[plan_name] = plan[-1] if plan[-1]>price else price
    minPrice = min(price_dict.values())
    for name, fee in price_dict.items():
        if fee == minPrice: return int(fee), name
        
if __name__ == '__main__': 
    input_list = [int(input()) for _ in range(6)]
    price, plan = best_plan(input_list)
    print(f'{price}\n{plan}')