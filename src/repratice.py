import bs4
import requests
import re

if __name__ == '__main__':

    sorts = {
        '评分最高华语电影': 'subjectList1497',
        '评分最高外语电影': 'subjectList1480',
        '年度冷门佳片': 'subjectList1610',
        '评分最高韩国电影': '//*[@id="app"]/div/div/div[6]/div[2]/div/div[2]/ul/li[1]/div/div',
        '评分最高日本电影': '//*[@id="app"]/div/div/div[6]/div[2]/div/div[2]/ul/li[2]/div/div' ,
        '评分最高喜剧片': '//*[@id="app"]/div/div/div[7]/div[2]/div/div[2]/ul/li[1]/div/div',
        '评分最高爱情片': '//*[@id="app"]/div/div/div[7]/div[2]/div/div[2]/ul/li[2]/div/div',
        '评分最高恐怖片/惊悚片': '//*[@id="app"]/div/div/div[7]/div[2]/div/div[3]/ul/li[2]/div/div',
        '评分最高动画片': '//*[@id="app"]/div/div/div[7]/div[2]/div/div[4]/ul/li[2]/div/div',
        '评分最高纪录片': '//*[@id="app"]/div/div/div[7]/div[2]/div/div[2]/ul/li[5]/div/div',
    }

    keys = [key for key in sorts]
    print(keys)