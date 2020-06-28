# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import pandas as pd


class SpidersPipeline:
    '''
    需要在settings中打开pipelines的配置
    '''
    #    def process_item(self, item, spider):
    #        return item
    def process_item(self, item, spider):
        # 每一个item管道组件都会调用该方法，并且必须返回一个item对象实例或raise DropItem异常
        name = ['电影名称:',item['movie_name']]
        types = ['电影类型:',item['movie_type']]
        times = ['上映时间:',item['movie_time']]
        movie_info = [[name, types, times]]
        #使用pandas处理爬取到的信息并转存为cvs文件
        maoyan_info = pd.DataFrame(data=movie_info)
        maoyan_info.to_csv('./movies_maoyan.csv',mode='a',encoding='utf8',index=False,header=False)

        return item
