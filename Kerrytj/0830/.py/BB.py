import pyexcel
import pyexcel_xls
import re
from glob import glob
from reportlab.pdfgen import canvas
import pikepdf
import pdfplumber
from os import remove, system
# pyinstaller -F --hidden-import=pyexcel_io.writers
system("title " + '大B轉檔')


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


def assign_row(excel, address):
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



'''0.讀取EXCEL'''
try:
    sheet = pyexcel.get_sheet(file_name='7048_ADDRESS.xls')
    excel = list(sheet)
except FileNotFoundError:
    input('未讀取到\"7048_ADDRESS.xls\"')


'''1.pikepdf合併所有pdf'''

print('-合併所有pdf-')
pdf = pikepdf.Pdf.new()

for file in glob('./大B轉檔/*.pdf'):
    src = pikepdf.Pdf.open(file)
    pdf.pages.extend(src.pages)
    src.close()
pdf.save('./大B轉檔/merged')
pdf.close()

'''2.PDFPlumber讀取pdf中的地址'''

print('-讀取PDF中的地址-\n')
pdf_b = pdfplumber.open('./大B轉檔/merged', )

all_address = list()
for page in pdf_b.pages:
    text = page.extract_text()    # 取出文字
    date = text.split('\n')[0]
    address1 = text.split(date+'\n'+date)[1].strip('\n').split('\n')[-6]
    print(address1)
    all_address.append(address1)
    try:
        address2 = text.split(date + '\n' + date)[2].strip('\n').split('\n')[-6]
        print(address2)
        all_address.append(address2)
    except IndexError:
        all_address.append('')

pdf_b.close()

'''3.將地址轉成派遣號碼'''

print('\n-轉換地址為派遣號碼-')
all_assign = list()
for addr in all_address:
    row = assign_row(excel, addr)
    if row == 0:
        all_assign.append('')
    else:
        try:
            all_assign.append(str(excel[row][23]))
        except:
            all_assign.append('')

'''4.Canvas生成派遣號碼的pdf'''

print('-生成派遣號碼的pdf-')
temp_pdf = canvas.Canvas("./大B轉檔/assign")

for no in range(len(all_assign)):
    if no % 2 == 0:
        temp_pdf.drawString(572, 510, all_assign[no])
    elif no % 2 == 1:
        temp_pdf.drawString(572, 70, all_assign[no])
        temp_pdf.showPage()

temp_pdf.save()

'''5.pikepdf將派遣號碼合成到原本的pdf上'''

print('-將派遣號碼合成到原本的pdf上-')
pdf1 = pikepdf.Pdf.open('./大B轉檔/merged', allow_overwriting_input=True)
pdf2 = pikepdf.Pdf.open('./大B轉檔/assign', allow_overwriting_input=True)
for pg in range(len(pdf1.pages)):
    destination_page = pikepdf.Page(pdf1.pages[pg])
    thumbnail = pikepdf.Page(pdf2.pages[pg])
    destination_page.add_overlay(thumbnail)

pdf1.save('大B派遣單.pdf')
pdf1.close()
pdf2.save()
pdf2.close()
remove('./大B轉檔/merged')
remove('./大B轉檔/assign')
print('\n完成')
