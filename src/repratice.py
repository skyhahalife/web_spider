import bs4
import requests
import re

if __name__ == '__main__':


    string = r'2\7'
    m = re.match('(\d+)\\\\', string)
    print(m.group())
    print(m.group(1))  # 结果为：2
    n = re.match(r'(\d+)\\', string)
    print(n.group(1))  # 结果为：2