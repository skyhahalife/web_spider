import datetime
import time
import requests
import re

# 实际放替换的东西
users = ["Jack", "David", "Tom", "Bill"]
# minutes 预计演示时长分钟, step 监听时间空隙 秒
def monitor(minutes, step, start_index):
    # 监听的url
    monitor_url = "http://www.baidu.com"
    # header
    # 请求中其他可能需要的内容
    for i in range(0, minutes*60, step):
        response = requests.get(monitor_url)
        # 监听条件 如status_code不是200时, 进行相应处理
        if response.status_code == 200:
            print("xxxx正常请求" + "------------" + str(i) )
        else:
            change_file_content(start_index)
            start_index += 1
            print("xxxx请求数量达到上线以更换"+ "------------" + str(i))
        time.sleep(step)
    print("监听结束")

def change_file_content(start_index):
    file_path = "C:\\Users\\Administrator\\Desktop\\test.txt"
    with open(file_path, 'r') as r:
        keyword = "num"
        content = r.read()
        temp = ""
        # 找到关键字 在文件中位置 以位置替换
        # keyword_places = [m for m in re.finditer(keyword,content)]
        # keyword_places_index = [m.start() for m in re.finditer(keyword, content)]
        # keyword_places_count = len(keyword_places)
        # print(*keyword_places)
        # print(keyword_places[1].)

        # # 替换每一处
        # for i in range(keyword_places_count):
        #     #替换操作
        #
        #     print("替换成功" + str(i))
        # 读取账户名称

        temp = content.replace("num",users[start_index])
        with open(file_path, 'w') as w:
            w.write(temp)
        w.close()
    r.close()

if __name__ == '__main__':
    # 实际中建议 参数 120，10
    monitor(2, 5, 1)

    # 测试更换文件内容
    #change_file_content(start_index)
