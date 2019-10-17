# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class HebeispiderPipeline(object):#直接保存为csv文件
    def process_item(self, item, spider):
        content='\n标题：'+item['title']+'\n所属城市：'+item['city']+'  来源平台：'+item['inmfrom']+'  信息类型：'+item['inmtype']+'  行业：'+item['industry']+'\n项目详情：'+item['text']+'\n联系方式：'+item['phones']
        with open('河北省招标投标公共服务平台.csv','a+',encoding='utf-8')as f:
            f.write(content)
        return item
class MysqlPipline(object): #连接 Mysql数据库保存
    def open_spider(self,spider):
        self.connect=pymysql.connect(host='localhost',user='root',password='zjy19970929',port=3306,charset='utf8',db='河北招标')
        self.cursor=self.connect.cursor()

    def process_item(self, item, spider):
        data = dict(item)
        sql='INSERT INTO hbzb(title,city,inmfrom,inmtype,industry,text,phones) VALUES (%s,%s,%s,%s,%s,%s,%s)'
        self.cursor.execute(sql,(data['title'],data['city'],data['inmfrom'],data['inmtype'],data['industry'],data['text'],data['phones']))
        self.connect.commit()
    def close_spider(self,spider):
        self.connect.close()
        self.cursor.close()



