# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class InfhousePipeline(object):
    def process_item(self, item, spider):
        return item
class MysqlPipline(object):
    def open_spider(self,spider):
        self.connect=pymysql.connect(host='localhost',user='root',password='zjy19970927',port=3306,charset='utf8',db='安居客')
        self.cursor=self.connect.cursor()
    def process_item(self, item, spider):
        data = dict(item)
        sql='INSERT INTO anjuke(name,localtion,price,housetype,starttime,opentime) VALUES (%s,%s,%s,%s,%s,%s)'
        self.cursor.execute(sql,(data['name'],data['localtion'],data['price'],data['housetype'],data['starttime'],data['opentime']))
        self.connect.commit()
    def close_spider(self,spider):
        self.cursor.close()
        self.connect.close()
        # return item
