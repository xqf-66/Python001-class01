# _*_ coding : UTF-8 _*_
# 开发人员：xieqiaofa
# 开发时间：2020年6月24日
# 项目需求：爬取猫眼电影的前 10 个电影名称、电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中。

import requests
from bs4 import BeautifulSoup as bs
import lxml.etree
import pandas as pd

#使用requests爬取猫眼电影的网页源代码
# user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'

header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        'Cookie':'__mta=208417709.1592895912492.1592902918645.1592903952867.7; uuid_n_v=v1; uuid=DF9CCBB0B51F11EA801551553EAD9849A9C6A4B3E2894835A13DFBE0903318F2; _csrf=b440c76ad9bd8b530488f522785e6cf7af43ac1e907b9196a84bc71857d4234e; _lxsdk_cuid=172dffeb93ec8-0d64910ea0f05a-143e6257-1fa400-172dffeb93ec8; mojo-uuid=6a2c8527c33ed9dd8462351a67bb364e; mojo-session-id={"id":"5fa649bfa4a5fb40547b9af2b7ae5a30","time":1592898021553}; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22172e0281287bdf-06e09e70bab7de-2076244f-546797-172e0281288c3f%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%22172e0281287bdf-06e09e70bab7de-2076244f-546797-172e0281288c3f%22%7D; _lxsdk=DF9CCBB0B51F11EA801551553EAD9849A9C6A4B3E2894835A13DFBE0903318F2; lt=sbcAoSSv2aNOkmQO1M30XtzxY4oAAAAA5woAAM42swSU-Amm1PnUAOMGoyjjYbuzAnq3nio6jK_ArkGALUH-whiVT6KsP7yiYWj32g; lt.sig=ytlNcmJAcMmZ5ZqM84NQiRBdoqM; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1592906608,1592906937,1592906948,1592906968; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1592906968; __mta=208417709.1592895912492.1592903952867.1592906969162.8; mojo-trace-id=50; _lxsdk_s=172e01ee84e-47c-6be-c2b%7C%7C99',

}

myurl = 'https://maoyan.com/films?showType=3'

response = requests.get(myurl, headers=header)


#使用BeautifulSoup解析爬取到的网页
bs_info = bs(response.text, 'html.parser')

movies_list = []
for tags in bs_info.find_all('div', attrs={'class': 'movie-item-hover'},limit=10):
    for atag in tags.find_all('a',):

        url = atag.get('href')
        movie_details = requests.get('https://maoyan.com'+url,headers = header)
        # 获取所有链接


        selector = lxml.etree.HTML(movie_details.text)
        bs_selector = bs(movie_details.text, 'html.parser')

        movie_name = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/h1/text()')
        movie_releasetime = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[3]/text()')

        type_list = []
        for types in bs_selector.find_all('div', attrs={'class': 'movie-brief-container'}):
            for atype in types.find_all('a', attrs={'class': 'text-link'}):
                type_list.append(atype.get_text().strip())


        mlist = [f'电影名称:{movie_name}', f'电影类型:{type_list}', f'上映时间:{movie_releasetime}']
        movies_list.append(mlist)

#使用pandas处理获取到到电影信息并转存为cvs文件
maoyan_movie = pd.DataFrame(data=movies_list)

maoyan_movie.to_csv('./movie1.csv', encoding='utf8', index=False, header=False)








