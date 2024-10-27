def get_input_dict()->dict:
    height, weight = input().split()
    return {'h': float(height), 'w': float(weight)}

def bmi(h,w):
    bmi = w / h**2
    if int(bmi*100)%2 == 0 and int(bmi*1000)%10 == 5:
        return int(bmi*100)/100
    else:
        return round(bmi, 2)

def median(nums:list)->float:
    lst = sorted(nums)
    if len(lst)%2 == 0:
        med = (lst[len(lst)//2] + lst[len(lst)//2-1])/2
    else:
        med = lst[len(lst)//2]
    return int(med*100)/100

def mod(nums:list)->float:
    count = [nums.count(num) for num in nums]
    i = count.index(max(count))
    return nums[i] if max(count)>1 else min(nums)

def main():
    bmi_list = list()
    for _ in range(int(input())):
        data = get_input_dict()
        bmi_list.append(bmi(**data))
    for funtion in max, min, median, mod:
        print(f'{funtion(bmi_list):.2f}')

if __name__ == '__main__':
    main()