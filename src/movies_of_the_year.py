import time
from selenium.webdriver.common.by import By
from selenium import webdriver
import ddddocr

def force_waiting(seconds):
    time.sleep(seconds)

if __name__ == '__main__':
    # 浏览器设置
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("disable-gpu")
    chrome_options.add_argument(r'--user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data')
    # 启动浏览器获取源代码
    browser = webdriver.Chrome(chrome_options)
    browser.implicitly_wait(3)

    # 2022 movies of the year url
    main_url = 'https://movie.douban.com/annual/2022?fullscreen=1&source=navigation'
    browser.get(main_url)


    # First three items include the subject wall which is different with the others

    sorts = {
        '评分最高华语电影': 'subjectList1479',
        '评分最高外语电影': 'subjectList1480',
        '年度冷门佳片': 'subjectList1610',
        '评分最高韩国电影': '//*[@id="app"]/div/div/div[6]/div[2]/div/div[2]/ul/li[1]/div/div',
        '评分最高日本电影': '//*[@id="app"]/div/div/div[6]/div[2]/div/div[2]/ul/li[2]/div/div' ,
        '评分最高喜剧片': '//*[@id="app"]/div/div/div[7]/div[2]/div/div[2]/ul/li[1]/div/div',
        '评分最高爱情片': '//*[@id="app"]/div/div/div[7]/div[2]/div/div[2]/ul/li[2]/div/div',
        '评分最高恐怖片': '//*[@id="app"]/div/div/div[7]/div[2]/div/div[2]/ul/li[3]/div/div',
        '评分最高动画片': '//*[@id="app"]/div/div/div[7]/div[2]/div/div[2]/ul/li[4]/div/div',
        '评分最高纪录片': '//*[@id="app"]/div/div/div[7]/div[2]/div/div[2]/ul/li[5]/div/div',
    }

    keys = [key for key in sorts]
    for i in range(0, 3):
        print(keys[i] + ':')
        container = browser.find_element(By.ID, sorts.get(keys[i]))
        links = container.find_elements(By.TAG_NAME, 'a')

        for j in range(2, len(links)):
            print(f"No.{j-1}" + links[j].get_attribute('title') + ":" + links[j].get_attribute('href'))



    for i in range(3, 10):
        print(keys[i] + ':')
        container = browser.find_element(By.XPATH, sorts.get(keys[i]))
        links = container.find_elements(By.TAG_NAME, 'a')
        for j in range(0, len(links)):
            print(f"No.{j+1}__" + links[j].get_attribute('title') + ":" + links[j].get_attribute('href'))




    browser.close()

    # #s32
