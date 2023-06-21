import time
from selenium.webdriver.common.by import By
from selenium import webdriver


def force_waiting(seconds):
    time.sleep(seconds)

if __name__ == '__main__':
    # 浏览器设置
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("disable-gpu")
    chrome_options.add_argument('--user-data-dir=C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\User Data')
    # 启动浏览器获取源代码
    browser = webdriver.Chrome(chrome_options)
    mainUrl = ""

    # 用户名密码
    username = "wangjia"
    password = "wangjia"

    page = browser.get(mainUrl)
    print(f"browser text = {browser.page_source}")


    force_waiting(10)
    print("结束")
    browser.close()
