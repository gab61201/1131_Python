from playwright.sync_api import sync_playwright
from os.path import abspath
from pyexcel import get_sheet
import pyexcel_xls, re
# pyinstaller --noconsole --hidden-import=pyexcel_io.writers 集貨派遣.py


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


def load_excel():
    sheet = get_sheet(file_name='7048_ADDRESS.xls')
    table = list(sheet)
    return table


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


def assign_html(data, dz, row, address):
    bol_no = data.split('BOL_NO:')[1].split(',')[0]
    customer_id = data.split('CUSTOMER_ID:')[1].split(',')[0]
    pickup_notice_seq = data.split('PICKUP_NOTICE_SEQ:')[1].split(',')[0].split('.')[0]
    output = re.sub(r'<h3>．託運單號：\S*．客戶編號：\S*．大Ｂ序號：\S*．到著註區：\S*．表格：\S*．地址：\S*</h3>',
                    r'<h3>．託運單號：'+bol_no+r'．客戶編號：'+customer_id+r'．大Ｂ序號：'+pickup_notice_seq+r'．到著註區：'+dz+r'．表格：'+row+r'．地址：'+address+r'</h3>',
                    html_template)
    return output


browser = sync_playwright().start().chromium.launch(channel='msedge', headless=False, args=["--start-maximized"])
context = browser.new_context(no_viewport=True)
context.add_init_script("delete Object.getPrototypeOf(navigator).webdriver")
page = context.new_page()
page.goto('http://ktms.kerrytj.com:8088/Portal/')
info_path = abspath('./_internal/info.html')
template_path = abspath('./_internal/template.html')
with open('./_internal/template.html', encoding='utf-8') as template:
    html_template = template.read()

while page in context.pages:
    try:
        with page.expect_popup(timeout=0) as assign_tab_info:
            assign_tab = assign_tab_info.value
    except:
        break
    station = assign_tab.locator("#MainContent_txtDEPOT_ID").input_value()
    if station != "7048" or 'http://ktms.kerrytj.com/TMS/CS/CSM/CS02M0020' not in assign_tab.url:
        continue

    info_page = context.new_page()
    info_page.goto(template_path)
    excel = load_excel()
    frame = assign_tab.frame_locator("#fra_DivDialogCS02M0020_iframe")
    while assign_tab in context.pages:
        try:
            with assign_tab.expect_request("http://ktms.kerrytj.com/TMS/CS/CSM/CS02M0010.aspx"
                                           "/GetData_CS_PICKUP_DISPATCH", timeout=0) as request_info:
                request = request_info.value
        except:
            break
        addr = frame.locator("#txtCOLLECTION_ADDR").input_value()
        excel_row = assign(excel, addr)
        if excel_row != 0:
            car = str(excel[excel_row][23])
            frame.locator("#txtCOLLECTION_AREA").fill(car)
            frame.locator("#txtCOLLECTION_AREA").select_text()

        if info_page in context.pages:
            response = str(request.response().json()).replace('\"', '')
            with open('./_internal/info.html', 'w', encoding='utf-8') as info:
                info.write(assign_html(response, str(excel[excel_row][22]),str(excel_row+1), addr))
            info_page.goto(info_path)
