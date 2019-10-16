# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import pymysql
# class ZihuPipeline(object):
#     # def __init__(self):
#     #     with open('知乎用户数据.csv', 'a', encoding='utf-8',newline="")as f:
#     #         writer = csv.writer(f)
#     #         writer.writerow(['用户名', '简介', '头像','爬取粉丝来源'])
#     def process_item(self, item, spider):
#         data=dict(item)
#         with open('知乎用户数据.csv','a',encoding='utf-8',newline="")as f:
#             writer=csv.writer(f)
#             writer.writerow([data['name'],data['content'],data['jpg'],data['froms']])
#         return item


class FristspiderPipeline(object):
    def __init__(self):
        self.connect =pymysql.Connect(host='localhost',user='root',password='zjy19970927',port=3306,database='zhihudata')
        self.cursor=self.connect.cursor()

    def process_item(self, item, spider):
        data=dict(item)
        print(data['froms'])
        sql='INSERT INTO zhihu(username,content,jpg,froms) VALUES ("%s","%s","%s","%s")ON DUPLICATE KEY UPDATE name=%s,content=%s,jpg=%s,froms=%s'
        self.cursor.execute(sql,(data['name'],data['content'],data['jpg'],data['froms'])*2)
        self.connect.commit()
        # print('yes')
        return item
    def close_spider(self,spider):
        self.cursor.close()
        self.connect.close()
        # print('ok')
