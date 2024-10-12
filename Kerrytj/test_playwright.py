from playwright.sync_api import sync_playwright


def get_home_page():
    if 'http://ktms.kerrytj.com/TMS/Default.aspx' in page.url:  # 若已在主頁，找尋彈出視窗
        print("已在主頁"+page.url)
        get_tab()
    else:
        print('尋找主頁中')
        with page.expect_request("http://ktms.kerrytj.com/TMS/Default.aspx/GetAllMenuData", timeout=0) as login:
            login = login.value
        print("進入主頁")
        get_tab()  # 連接派遣頁面


def get_tab():
    print('尋找彈出視窗中')
    with page.expect_popup(timeout=0) as assign_tab:
        assign_tab = assign_tab.value

    if 'http://ktms.kerrytj.com/TMS/CS/CSM/CS02M0020.ASPX' in assign_tab.url:
        print('彈出派遣頁面')
        get_response(assign_tab)
    else:
        print('彈出非派遣頁面')
        get_home_page()


def get_response(pg):
    while pg.frame_locator("#fra_DivDialogCS02M0020_iframe"):
        frame = pg.frame_locator("#fra_DivDialogCS02M0020_iframe")
        print('尋找response中')
        try:
            with pg.expect_request("http://ktms.kerrytj.com/TMS/CS/CSM/CS02M0010.aspx/GetData_CS_PICKUP_DISPATCH", timeout=0) as response_info:
                print(frame.locator("#txtCOLLECTION_ADDR").input_value())
        except:
            break

    get_home_page()


browser_type = 'chrome'
browser = sync_playwright().start().chromium.launch(channel=browser_type, headless=False, args=["--start-maximized"])
context = browser.new_context(no_viewport=True)
page = context.new_page()
page.add_init_script("delete Object.getPrototypeOf(navigator).webdriver")
page.goto('http://ktms.kerrytj.com:8088/Portal/')
get_tab()