def get_fee(used:dict, plan:dict)->int:
    fee = sum(plan[i]*used[i] for i in ['inCall', 'outCall', 'tel', 'inMes', 'outMes'])
    if used['data'] > plan['data']:
        fee += (used['data']-plan['data'])*plan['buyData']
    return int(fee) if fee > plan['price'] else plan['price']

def main():
    Inp = {'inCall':int(input()),'outCall':int(input()),'tel':int(input()),
            'inMes':int(input()),'outMes':int(input()),'data':int(input())}
    plan_183 = {'inCall':0.08,'outCall':0.139,'tel':0.135,'inMes':1.128,'outMes':1.483,'data':1,'buyData':250,'price':183}
    plan_383 = {'inCall':0.07,'outCall':0.130,'tel':0.121,'inMes':1.128,'outMes':1.483,'data':3,'buyData':200,'price':383}
    plan_983 = {'inCall':0.06,'outCall':0.108,'tel':0.101,'inMes':1.128,'outMes':1.483,'data':5,'buyData':150,'price':983}
    plan_1283 = {'inCall':0.05,'outCall':0.100,'tel':0.090,'inMes':1.128,'outMes':1.483,'data':float('inf'),'buyData':0,'price':1283}
    planList = [plan_183, plan_383, plan_983, plan_1283]
    bestPlan = min(planList, key=lambda plan:get_fee(Inp, plan))
    print(f'{get_fee(Inp, bestPlan)}\n{bestPlan["price"]}')

if __name__ == '__main__':
    main()
