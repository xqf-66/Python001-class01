# _*_ coding : UTF-8 _*_
# 开发人员：xieqiaofa
# 开发时间：2020年6月28日
# 项目需求：使用 Scrapy 框架和 XPath 抓取猫眼电影的前 10 个电影名称、电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中。


import scrapy
from scrapy.selector import Selector
from ..items import SpidersItem
from http.cookies import SimpleCookie


class MaoyanSpider(scrapy.Spider):
    # 定义爬虫名称
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    # 起始URL列表
    start_urls = ['http://maoyan.com/films?showType=3']



    # 注释掉默认的parse函数
    # def parse(self, response):
    #     pass

    # 爬虫启动时，引擎自动调用该方法，并且只会被调用一次，用于生成初始的请求对象（Request）。
    # start_requests()方法读取start_urls列表中的URL并生成Request对象，发送给引擎。
    # 引擎再指挥其他组件向网站服务器发送请求，下载网页
    def start_requests(self):
        cookie = '__mta=146044427.1593337411652.1593337411652.1593337411652.1;' ' uuid_n_v=v1; ' 'uuid=D2A2CCE0B92311EAA94453F28D7995DF136E9C239CE54B49884F5EDB075757A3; ' '_csrf=7191ff74d070b7024355dbc27a7aa6e4c93b975adf782870304f6f92dccba15c; ' 'Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1592986956,1593076672,1593096084,1593337394; ' '_lxsdk_cuid=172e56bef4dc8-08ad4c59b813bd-31607403-fa000-172e56bef4dc8; ' '_lxsdk=D2A2CCE0B92311EAA94453F28D7995DF136E9C239CE54B49884F5EDB075757A3; ' 'mojo-uuid=49838d8e729158513762de8e12e2af53; ' 'Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593337411;' ' _lxsdk_s=172fa4f5efd-99b-ea-43c%7C308984839%7C2'
        url = 'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url=url,cookies=cookie,callback=self.parse)

    # 解析函数
    def parse(self, response):
        """
        解析爬取到的内容
        """

        print(response.url)
        item = SpidersItem()
        movies = Selector(response=response).xpath('//div[@class="movie-item-hover"]')

        for m in movies[:10]:
            movies_name = m.xpath('./a/div/div[1]/span/text()').extract_first().strip()
            movies_type = m.xpath('./a/div/div[2]/text()[2]').extract_first().strip()
            movies_time = m.xpath('./a/div/div[4]/text()[2]').extract_first().strip()

            # 注释掉调试的代码
            # print(movies_name)
            # print(movies_type)
            # print(movies_time)

            item['movie_name'] = movies_name
            item['movie_type'] = movies_type
            item['movie_time'] = movies_time
            yield item


