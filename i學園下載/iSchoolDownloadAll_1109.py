from playwright.sync_api import sync_playwright
from pathlib import Path
import time
import re
import json


def login_portal():
    page.goto("https://nportal.ntut.edu.tw/")
    # page.locator("#muid").fill(student_id)
    # page.locator("#mpassword").fill(password)
    portal_url = re.compile(r"https://nportal.ntut.edu.tw/myPortal.do\D+")
    page.wait_for_url(portal_url, timeout=0)
    print("成功登入入口網站")


def get_ischool_course_list():
    page.goto("https://nportal.ntut.edu.tw/ssoIndex.do?apOu=ischool_plus_oauth")
    url_to_get_course = "https://istudy.ntut.edu.tw/learn/mooc_sysbar.php"
    with page.expect_response(url_to_get_course) as course_page_info:
        course_page_text = course_page_info.value.text()
    print("登入i學園")
    course_data = re.findall(
        r'<option value="\d{8}">\d{4}_\D+_\d{6}</option>', course_page_text
    )
    course_list = list()
    for course in course_data:
        course_name = re.findall(r"\d{4}_\D+_\d{6}", course)[0]
        course_id = re.findall(r"\d{8}", course)[0]
        course_list.append((course_name, course_id))
    print("獲取課程清單\n")
    return course_list  # (course_name, course_id)


def get_course_json(course_id) -> dict:
    get_json_url = (
        "https://istudy.ntut.edu.tw/xmlapi/index.php?action"
        "=my-course-path-info&onlyProgress=0&descendant=1&cid=" + course_id
    )
    with page.expect_response(get_json_url) as output:
        page.goto(get_json_url)
        return output.value.json()


def path(folder_path: str) -> str:
    folder = Path(folder_path)
    folder.mkdir(parents=True, exist_ok=True)
    return str(folder) + "/"


def download(url: str, save_path: str, f_name: str):
    print(f"下載中：{f_name}", end="")
    response = page.request.get(url)
    if response.ok:
        file_data = response.body()
        with open(path(save_path) + f_name, "wb") as file:
            file.write(file_data)
        print(f"\r已儲存：{f_name}")
    else:
        print("下載失敗")


def traversal_json(file_list: list) -> dict:
    for file in file_list:
        if file["item"]:
            yield from traversal_json(file["item"])
            continue
        if re.match(r"istream://", file["href"]):
            continue

        if re.match(r"https://istudy.ntut.edu.tw/base/10001/course/", file["href"]):
            file_type = file["href"].split(".")[-1]
        else:
            file_type = "html"

        file_info = {
            "file_name": f'{file["text"]}.{file_type}',
            "href": file["href"],
            "identifier": file["identifier"],
        }
        yield file_info


def download_course_file(course_name: str, course_id: int, ischool_files: list):
    try:
        with open(
            path("downloaded") + course_name + ".json", "r", encoding="UTF-8"
        ) as f:
            local_course_data = json.load(fp=f)
    except FileNotFoundError:
        local_course_data = {"course_id": course_id, "file": []}

    local_file_set = {file["identifier"] for file in local_course_data["file"]}
    for i_file in ischool_files:
        if i_file["identifier"] not in local_file_set:
            download(
                i_file["href"], path("course_file") + course_name, i_file["file_name"]
            )
            i_file["download_date"] = time.ctime(time.time())
            local_course_data["file"].append(i_file)
    with open(path("downloaded") + course_name + ".json", "w", encoding="UTF-8") as f:
        json.dump(local_course_data, fp=f, ensure_ascii=False, indent=4)


def main():
    login_portal()
    for course_name, course_id in get_ischool_course_list():
        course_raw_json = get_course_json(course_id)
        raw_file_list = course_raw_json["data"]["path"]["item"]
        ischool_files = [file for file in traversal_json(raw_file_list)]
        download_course_file(course_name, course_id, ischool_files)


if __name__ == "__main__":
    browser = (
        sync_playwright().start().chromium.launch(channel="chrome", headless=False)
    )
    context = browser.new_context()
    context.add_init_script("delete Object.getPrototypeOf(navigator).webdriver")
    page = context.new_page()
    main()
    browser.close()
    print("\n完成")
