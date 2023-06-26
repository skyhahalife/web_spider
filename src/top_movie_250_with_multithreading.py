import threading
import time

import bs4
import requests
import re

link = "https://movie.douban.com/annual/2022?fullscreen=1&source=navigation"
link_01 = 'https://movie.douban.com/chart'
thread_list = []


class MovieThread(threading.Thread):
    def __init__(self, name, list_div):
        super().__init__()
        self.name = name
        self.list_div = list_div

    def run(self):
        print("Staring" + self.name)
        movies_detail(list_div)
        print("Exiting" + self.name)


def movies_detail(list_div):
    for j in list_div:
        check_string = str(j.a)

        titles_pattern = r'>(.*?)</span>'
        link_pattern = r'href="(.*?)"'

        titles = re.findall(titles_pattern, check_string)
        link = re.findall(link_pattern, check_string)

        print("------------------------------------")
        print(f'{"电影中文名":<10}' + titles[0])
        print(f'{"电影外文名":<10}' + titles[1].split('/')[-1].strip())

        # loop url to find more information
        print(f'{"电影豆瓣链接:":<10}' + link[0])
        response_movie_detail = requests.get(link[0], headers=headers)
        movie_soup = bs4.BeautifulSoup(response_movie_detail.text, "lxml")
        # detail_span = movie_soup.findAll('div', class_='indent')
        detail_span = movie_soup.find('span', property="v:summary")
        # detail_span = movie_soup.findAll('span', class_ = 'all hidden')
        text = detail_span.get_text().strip()
        print(f'{"电影简介:":<10}' + text.split("\n")[0])

        play_links_list = movie_soup.find("ul", class_='bs')
        if play_links_list:
            play_links = play_links_list.findAll('a')
            for play_link in play_links:
                print('{:<10}'.format(play_link.text.strip() + ":") + re.findall('href=\"(.*?)\"', str(play_link))[-1])


if __name__ == '__main__':

    start_time = time.time()
    loop_link = 'https://movie.douban.com/top250?start='
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate',
        'Accept': '*/*',
        'Connection': 'keep-alive',
        'Cookie': 'bid=7TH-UDiD_9M; ll="118120"; __utmc=30149280; __utmz=30149280.1686791735.4.4.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ap_v=0,6.0; __utma=30149280.204071560.1680594820.1686791735.1686812599.5; __utmb=30149280.0.10.1686812599; dbcl2="204088368:8roBp+bMw5Y"; ck=vDWa; frodotk_db="3aaabd79f0dcc447b000386dd2964cd5"; push_noty_num=0; push_doumail_num=0; __gads=ID=0beb1c9dcab41d78-22b0bf1882e1003b:T=1686732462:RT=1686814222:S=ALNI_MYVT-dUAJIlW-XMj5PiTgmYguuk8w; __gpi=UID=00000c4ec8f1b5b1:T=1686732462:RT=1686814222:S=ALNI_MYd5rhb7M_GaARqYL5JQPzwQ1jLSQ'
    }

    # There are 25 items in each page, so we should loop 10 times
    for i in range(0, 10):
        url = loop_link + str(i * 25)
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            print("访问成功")
        else:
            print("访问失败，状态码:", response.status_code)

        beautiful_soup = bs4.BeautifulSoup(response.text, "lxml")
        # print(response.request.headers)
        # print(response.request.url)
        list_div = beautiful_soup.findAll('div', class_='hd')
        # put movies_detail(list_div) in threading
        movie_thread = MovieThread("线程——" + str(i), list_div)
        movie_thread.start()
        thread_list.append(movie_thread)

    for thread in thread_list:
        thread.join()
    end_time = time.time()
    print("共用时间：", end_time - start_time, "秒")
