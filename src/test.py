import time
from selenium.webdriver.common.by import By
from selenium import webdriver
import ddddocr

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
    browser.implicitly_wait(10)


    # 用户名密码
    username = "wangjia"
    password = "1qaz!QAZ"

    page = browser.get(mainUrl)


    username_input = browser.find_element(By.NAME,"j_username")
    password_input = browser.find_element(By.NAME,"j_password")
    username_input.send_keys(username)
    password_input.send_keys(password)

    randCodeImg = browser.find_element(By.ID,"refreshCaptcha")
    randCodeImg.screenshot("./a.png")
    with open("./a.png",'rb') as f:
        image = f.read()
    ocr = ddddocr.DdddOcr()
    random_text = ocr.classification(image)
    print(random_text)
    captchat_input = browser.find_element(By.NAME,"j_captcha")
    captchat_input.send_keys(random_text)

    login_button = browser.find_element(By.CLASS_NAME,"btns")
    login_button.click()





    # ------------登录成功后------------------
    # 用户管理 进入iframe
    user_manage = browser.find_element(By.ID,"btn5")
    user_manage.click()



    # 机构管理
    frame = browser.find_element(By.ID,"iframe1")
    browser.switch_to.frame(frame)

    print("-----结束-------")
    # print(f"browser text = {browser.page_source}")
    stucture_manage = browser.find_element(By.ID,"s32")
    stucture_manage.click()

    lil_frame = browser.find_element(By.ID, "iframe2")
    browser.switch_to.frame(lil_frame)

    # 添加组织结构
    # increas_organization = browser.find_element(By.CSS_SELECTOR,"#rig > div.tab_div > input")
    # increas_organization.click()

    # 添加组织名称 groupNameAdd

    print(browser.page_source)
    force_waiting(1)
    browser.close()

    # #s32
