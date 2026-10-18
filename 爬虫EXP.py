#https://www.themoviedb.org/movie
#//*[@id="626def6c8258fc00a8b6f018"]/div/div[1]/a

import csv
from bs4 import BeautifulSoup
import requests
from lxml import html
import re

URL = 'https://www.themoviedb.org/movie'
url2 = 'https://www.themoviedb.org/discover/movie/items'
XPATH = '//*[@class="media-card-list contents w-full"]/div/*//a/@href'


def clearfunc(list1):
    if list1:
        print(list1)
        l1st = []
        str = list1[0].strip()
        l1st.append(str)
        return l1st
    else:
        return -1

def clear2(data):
    return re.search(r'\d{4}-\d{2}-\d{2}', data[0]).group()

def movie_time(data):
    if data == -1:
        return -1
    else:

        # 2h46m/2h/46m
        h = re.search(r'(\d+)h', data)
        m = re.search(r'(\d+)m', data)
        if h:
            h_time = int(h.group(1))
        if m:
            m_time = int(m.group(1))
        return h_time * 60 + m_time

def movie_content(movie_url):
    def clearfunc(list1):
        if list1:
            print(list1)
            l1st = []
            str = list1[0].strip()
            l1st.append(str)
            return l1st
        else:
            return -1

    def clear2(data1):
        print(data1)
        data = data1[0]
        print(data)
        return re.search(r'\d{4}-\d{2}-\d{2}', data).group()

    def movie_time(data1):
        if data1 == -1:
            return -1
        else:
            print(type(data1))
            data = data1[0]
            print(type(data))
            # 2h46m/2h/46m
            h = re.search(r'(\d+)h', data)
            m = re.search(r'(\d+)m', data)
            h_time = int(h.group(1)) if h else 0
            m_time = int(m.group(1)) if m else 0
            return h_time * 60 + m_time


    movie_response = requests.get(movie_url,timeout=10)
    movie_doc = html.fromstring(movie_response.text)
    movie_name = movie_doc.xpath('//*[@id="original_header"]/div[2]/section/div[1]/h2/a/text()')
    movie_intruduce = movie_doc.xpath('//*[@id="original_header"]/div[2]/section/div[3]/div/p/text()')
    movie_years1 = clear2(clearfunc(movie_doc.xpath('//*[@id="original_header"]/div[2]/section/div[1]/div/span[2]/text()')))
    movie_time = movie_time(clearfunc(movie_doc.xpath('//*[@id="original_header"]/div[2]/section/div[1]/div/span[@class="runtime"]/text()')))
    movie_score = movie_doc.xpath('//*[@id="consensus_pill"]/div/div[1]/div/div/@data-percent')
    movie_maker = movie_doc.xpath('//*[@id="original_header"]/div[2]/section/div[3]/ol/li/p[1]/a/text()')
    movie_chart = movie_doc.xpath('//*[@id="cast_scroller"]/ol/li/p[1]/a/text()')
    movie_element = movie_doc.xpath('//*[@id="original_header"]/div[2]/section/div[1]/div/span[3]/a/text()')
    print('电影名：',movie_name[0])
    print('简介：',movie_intruduce[0])
    print('发行日期：',movie_years1)
    print('时长：',movie_time)
    print('评分：',movie_score[0])
    print('制作人：',movie_maker)
    print('演员',movie_chart[:-1:])
    print('元素',movie_element[:-1:])
    movie_info = {
        '电影名':movie_name[0],
        '简介':movie_intruduce[0],
        '发行日期':movie_years1,
        '时长':movie_time,
        '评分':movie_score[0],
        '制作人':','.join(movie_maker),
        '演员':','.join(movie_chart[:-1:])
    }
    return movie_info

def save_data(info):
    with open('D:/李空的下载/导出的数据/movie/movie_info.csv','w',encoding='utf-8') as f:
        writer = csv.DictWriter(f,fieldnames=info[1].keys())
        writer.writeheader()
        writer.writerows(info)


def clearfunc(list1):
    if list1:
        print(list1)
        l1st = []
        str = list1[0].strip()
        l1st.append(str)
        return l1st
    else:
        return -1

def main(url,xpath):
    movie_urls1 = []
    for num in range(1,12):
        if num == 1:
            response = requests.get(URL,timeout=10)
        else:
            response = requests.post(url2,
                                     'air_date.gte = & air_date.lte = & certification = & certification_country = CN & debug = & first_air_date.gte = & first_air_date.lte = & include_adult = false & include_softcore = false & latest_ceremony.gte = & latest_ceremony.lte = & page = {} & primary_release_date.gte = & primary_release_date.lte = & region = & release_date.gte = & release_date.lte = 2027 - 02 - 13 & show_me = everything & sort_by = popularity.desc & vote_average.gte = 0 & vote_average.lte = 10 & vote_count.gte = 0 & watch_region = CN & with_genres = & with_keywords = & with_networks = & with_origin_country = & with_original_language = & with_watch_monetization_types = & with_watch_providers = & with_release_type = & with_runtime.gte = 0 & with_runtime.lte = 400'.format(num),
                                     timeout=10)


        document = html.fromstring(response.text)
        movie_list = document.xpath(xpath)
        for i in movie_list:
            if i:
                movie_url = url[:-6:1] + i
                movie_urls1.append(movie_url)
    return movie_urls1


def xiuzheng(info):
    info['时长'] = '预告，暂未正式上映！'
    info['评分'] = ' '
    info['制作人'] = ' '
    info['演员'] = ' '
    return info


if __name__ == '__main__':
    l1st = []
    movie_urls1 = main(URL,XPATH)
    movie_urls = movie_urls1[::2]
    for i in movie_urls:
        print('================================')
        info = movie_content(i)
        if info['时长'] == -1:
            info = xiuzheng(info)
        else:
            info['时长'] = str(info['时长']) + 'min'
        l1st.append(info)
    print(l1st)
    save_data(l1st)




