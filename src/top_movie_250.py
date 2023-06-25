import bs4
import requests
import re

link = "https://movie.douban.com/annual/2022?fullscreen=1&source=navigation"
link_01 = 'https://movie.douban.com/chart'

if __name__ == '__main__':

    loop_link = 'https://movie.douban.com/top250?start='
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate',
        'Accept': '*/*',
        'Connection': 'keep-alive',
        'Cookie':'bid=SXQ8o148eE8; ll="118120"; __utmc=30149280; __utmz=30149280.1686791735.4.4.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ap_v=0,6.0; __utma=30149280.204071560.1680594820.1686791735.1686812599.5; __utmb=30149280.0.10.1686812599; dbcl2="204088368:8roBp+bMw5Y"; ck=vDWa; frodotk_db="3aaabd79f0dcc447b000386dd2964cd5"; push_noty_num=0; push_doumail_num=0; __gads=ID=0beb1c9dcab41d78-22b0bf1882e1003b:T=1686732462:RT=1686814222:S=ALNI_MYVT-dUAJIlW-XMj5PiTgmYguuk8w; __gpi=UID=00000c4ec8f1b5b1:T=1686732462:RT=1686814222:S=ALNI_MYd5rhb7M_GaARqYL5JQPzwQ1jLSQ'
    }

    # There are 25 items in each page, so we should loop 10 times
    for i in range(0,10):
        url = loop_link + str(i*25)
        response = requests.get(url, headers=headers, timeout= 10)
        if response.status_code == 200:
            print("访问成功")
        else:
            print("访问失败，状态码:", response.status_code)

        beautiful_soup = bs4.BeautifulSoup(response.text, "lxml")
    # print(response.request.headers)
    # print(response.request.url)
        list_div = beautiful_soup.findAll('div', class_='hd')

        for i in list_div:
            check_string = str(i.a)
            titles_pattern = r'>(.*?)</span>'
            link_pattern = r'href="(.*?)"'

            titles = re.findall(titles_pattern,check_string)
            link = re.findall(link_pattern,check_string)

            print("------------------------------------")
            print(f'{"电影中文名":<10}'+titles[0])
            print(f'{"电影外文名":<10}' + titles[1].split('/')[-1].strip())


            # loop url to find more information
            print(f'{"电影豆瓣链接:":<10}' + link[0])
            response_movie_detail = requests.get(link[0],headers=headers)
            movie_soup = bs4.BeautifulSoup(response_movie_detail.text, "lxml")
            # detail_span = movie_soup.findAll('div', class_='indent')
            detail_span = movie_soup.find('span', property="v:summary")
            # detail_span = movie_soup.findAll('span', class_ = 'all hidden')
            text = detail_span.get_text().strip()
            print(f'{"电影简介:":<10}' + text.split("\n")[0])

            play_links_list = movie_soup.find("ul", class_='bs')
            if play_links_list:
                play_links = play_links_list.findAll('a')
                for i in play_links:
                    print('{:<10}'.format(i.text.strip() + ":") + re.findall('href=\"(.*?)\"', str(i))[-1])

            #if len(play_links_list)

            # detail_pattern = re.compile(r'>(.*?)</span>')
            # print(str(detail_span),123)
            # detail = detail_pattern.findall(str(detail_span).strip())
            # print(len(detail))
            # detail_content = re.findall(detail_pattern,detail_span[0].text)
            # print("电影简介:  " + str(detail_span[0].text).strip('\t').strip('\r').strip('\n').s)
            # print(titles[0])


            # print("              ")
            # print("电影标题",i.a.span)
            # content > div > div.article > ol > li:nth-child(1) > div > div.info > div.hd > a > span:nth-child(2)
            # // *[ @ id = "content"] / div / div[1] / ol / li[1] / div / div[2] / div[1] / a / span[2]