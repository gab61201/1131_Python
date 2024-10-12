import pyexcel
import pyexcel_xls
import re
from os import system
system("title " + '註區查詢')
# pyinstaller -F --hidden-import=pyexcel_io.writers search_0823.py


def standardize(string):
    string = string.replace(' ', '')
    string = string.replace('　', '')
    string = string.replace("－", "之")
    string = string.replace("-", "之")
    string = string.replace("f", "樓")
    string = string.replace("F", "樓")
    string = string.replace("Ｆ", "樓")
    string = string.replace("ｆ", "樓")
    string = string.replace("b", "-")
    string = string.replace("B", "-")
    string = string.replace("臺", "台")
    return string


def full_to_half_num(string):
    full = '０１２３４５６７８９'
    half = '0123456789'
    for num in range(10):
        string = string.replace(full[num], half[num])
    return string


def chi_to_half_num(string):
    full = '一二三四五六七八九'
    half = '123456789'
    for num in range(9):
        string = string.replace(full[num], half[num])
    return string


def assign(excel, address):
    address = standardize(address)
    address = chi_to_half_num(address)
    address = full_to_half_num(address)
    max_row = 0
    max_priority = 0
    for row in range(1, len(excel)):
        priority = 0
        # 找路段
        road = chi_to_half_num(full_to_half_num(excel[row][6] + excel[row][7]))
        if road not in address:
            continue
        # 找縣市、行政區
        city = str(excel[row][1])
        district = str(excel[row][2])
        if (city not in address) and (district not in address):
            continue
        # 若row有巷
        if excel[row][9] and excel[row][10]:
            if re.search(road + r'\d+巷', address):  # address中有巷
                find_ally = re.search(road + r'\d+巷', address)
                ally = int(find_ally.group().replace(road, '').replace('巷', ''))
            else:
                continue
            if int(excel[row][9]) <= ally <= int(excel[row][10]):  # 巷在row範圍內
                priority += 10
            else:
                continue
        # 若row有弄
        if excel[row][11] and excel[row][12]:
            if re.search(r'巷\d+弄', address):  # address中有弄
                find_lane = re.search(r'巷\d+弄', address)
                lane = int(find_lane.group().replace('巷', '').replace('弄', ''))
            else:
                continue
            if int(excel[row][11]) <= lane <= int(excel[row][12]):  # 弄在row範圍內
                priority += 1
            else:
                continue
        # 若有號
        if excel[row][13]:
            if re.search(road + r'\d+', address) and priority == 0:
                find_number = re.search(road + r'\d+', address)
                number = int(find_number.group().replace(road, ''))
            elif re.search(r'\d+之\d+號', address):
                find_number = re.search(r'\d+之\d+號', address)
                number = int(re.sub(r'之\d+號', '', find_number.group()))
            elif re.search(r'\d+號', address):
                find_number = re.search(r'\d+號', address)
                number = int(find_number.group().replace('號', ''))
            else:
                continue
            if number % 2 == int(excel[row][13]) and int(excel[row][14]) <= number <= int(excel[row][15]):
                priority += 1
            else:
                continue
        # 若有_之_號
        if excel[row][16] and excel[row][17]:
            if re.search(r'之\d+號', address):
                find_of = re.search(r'之\d+號', address)
                of = int(re.search(r'\d+', find_of.group()).group())
            else:
                continue
            if int(excel[row][16]) <= of <= int(excel[row][17]):
                priority += 1
            else:
                continue
        # 若有樓
        if excel[row][18] and excel[row][19]:
            if re.search(r'\d+樓', address):
                find_floor = re.search(r'\d+樓', address)
                floor = int(re.search(r'\d+', find_floor.group()).group())
            else:
                continue
            if int(excel[row][18]) <= floor <= int(excel[row][19]):
                priority += 1
            else:
                continue

        if priority >= max_priority:
            max_priority = priority
            max_row = row
        # 迴圈結束
    return max_row


def load_excel():
    sheet = pyexcel.get_sheet(file_name='7048_ADDRESS.xls')
    excel = list(sheet)
    return excel


table = load_excel()
while True:
    addr = input('\n\n　輸入地址：')
    system('cls')
    excel_row = assign(table, addr)
    print('\n　地址：' + addr)
    if excel_row == 0:
        print('\n　地址錯誤')
        continue
    print('\n　Excel第' + str(excel_row+1) + '列')
    print('\n　到著(W)：' + str(table[excel_row][22]))
    print('\n　發送(X)：' + str(table[excel_row][23]))
