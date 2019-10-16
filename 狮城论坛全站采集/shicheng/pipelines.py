# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import pymysql

class ShichengPipeline(object):

    def process_item(self, item, spider):
        data=dict(item)
        with open('狮城广告.csv','a',encoding='utf-8')as f:
            w=csv.writer(f)
            w.writerow(['服务内容:'+data['content'],'联系人:'+data['name'],'电话:'+data['phone'],'微信:'+data['wechat'],'内容:'+data['contents'],'warning:'+data['warning']])
            return item

class MySqlPipline(object):
    def open_spider(self,spider):
        self.connect=pymysql.connect(host='localhost',user='root',password='zjy19970927',port=3306,charset='utf8',db='狮城')
        self.cursor=self.connect.cursor()

    def process_item(self, item, spider):
        data = dict(item)
        sql='INSERT INTO shi_cheng(content,name,phone,wechat,contents,warning) VALUES (%s,%s,%s,%s,%s,%s)'
        self.cursor.execute(sql,(data['content'],data['name'],data['phone'],data['wechat'],data['contents'],data['warning']))
        self.connect.commit()
        return item
    def close_spider(self,spider):
        self.connect.close()
        self.cursor.close()