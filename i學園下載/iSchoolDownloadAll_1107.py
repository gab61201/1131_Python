from playwright.sync_api import sync_playwright
import re
import os


def browser_context():
    _browser = sync_playwright().start().chromium.launch(channel='chrome', headless=False, args=["--start-maximized"])
    context = _browser.new_context(no_viewport=True)
    context.add_init_script("delete Object.getPrototypeOf(navigator).webdriver")
    return context


def login_portal(page):
    page.goto('https://nportal.ntut.edu.tw/')
    page.locator('#muid').fill('')
    page.locator('#mpassword').fill('')
    portal_url = re.compile(r'https://nportal.ntut.edu.tw/myPortal.do\D+')
    with page.expect_request(portal_url, timeout=0):
        print('Login portal successfully')


def get_ischool_course_list(page):
    page.goto('https://nportal.ntut.edu.tw/ssoIndex.do?apOu=ischool_plus_oauth')
    url_to_get_course = 'https://istudy.ntut.edu.tw/learn/mooc_sysbar.php'
    with page.expect_response(url_to_get_course) as course_page_info:
        course_page_text = course_page_info.value.text()
    print('Login iSchool successfully')
    course_data = re.findall(r'<option value="\d{8}">\d{4}_\D+_\d{6}</option>', course_page_text)
    course_list = list()
    for course in course_data:
        course_name = re.findall(r'\d{4}_\D+_\d{6}', course)[0]
        course_id = re.findall(r'\d{8}', course)[0]
        course_list.append({'name': course_name, 'id': course_id})
    print('Get course list successfully')
    return course_list  # [{'name': course_name, 'id': course_id},]


def get_course_json(page, course: dict):
    get_json_url = ('https://istudy.ntut.edu.tw/xmlapi/index.php?action'
                    '=my-course-path-info&onlyProgress=0&descendant=1&cid='+course['id'])
    with page.expect_response(get_json_url) as output:
        page.goto(get_json_url)
        return output.value.json()


def path(folder_path: str):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    return folder_path+'/'


def download(page, url: str, save_path: str, f_name: str):
    response = page.request.get(url)
    if response.ok:
        file_data = response.body()
        with open(path(save_path)+f_name, 'wb') as file:
            file.write(file_data)
        print(f_name, 'saved')
    else:
        print('failed download')


def traversal_download(page, file_list: list, course_name: str):
    for file in file_list:
        if file["item"]:
            traversal_download(page, file["item"], course_name)

        if file["href"].find('/content/') != -1:
            print('downloading:', file["text"])
            download(page, file["href"], path('course/'+course_name), file["href"].split('/content/')[-1])
        elif file["href"].find('https://') != -1:
            print('pass downloading other:', file["text"])
        else:
            print('pass downloading:', file["text"])


def main():
    browser = browser_context()
    page_1 = browser.new_page()
    login_portal(page_1)
    course_list = get_ischool_course_list(page_1)
    page_2 = browser.new_page()
    for course in course_list:
        course_json = get_course_json(page_1, course)
        file_list = course_json["data"]["path"]["item"]
        traversal_download(page_2, file_list, course['name'])
    browser.close()


if __name__ == '__main__':
    main()
    input('Done')
