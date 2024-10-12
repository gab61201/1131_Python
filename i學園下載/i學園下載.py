from playwright.sync_api import sync_playwright
import re

browser = sync_playwright().start().chromium.launch(channel='chrome', headless=False, args=["--start-maximized"])
context = browser.new_context(no_viewport=True)
context.add_init_script("delete Object.getPrototypeOf(navigator).webdriver")
page = context.new_page()
page.goto('https://nportal.ntut.edu.tw/')

with page.expect_popup(timeout=0) as page_info:
    i_school_page = page_info.value
print('彈出視窗')

url = re.compile(r'https://istudy.ntut.edu.tw/learn/path/getPDF.php\D+')
with i_school_page.expect_response(url, timeout=0) as pdf:
    response = pdf.value

content_type = response.headers.get('content-type', '')
if 'application/json' in content_type:
    # 嘗試解析為 JSON
    try:
        json_data = response.json()  # 解析為 JSON
        if 'dataUri' in json_data:
            data_uri = json_data['dataUri']
    except Exception as e:
        print(f"解析 JSON 時出錯: {e}")

elif 'application/pdf' in content_type:
    print("響應為 PDF 文件，無法提取 data URI。")
    # 可以選擇保存 PDF 或進行其他操作
    pdf_data = response.body()  # 獲取二進制數據
    with open("output.pdf", "wb") as f:
        f.write(pdf_data)  # 將 PDF 保存到文件
    print('存檔完成')
