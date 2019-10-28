#-a自定义参数，local=查询的城市拼音首字母简写（合肥=hf，北京=bj）
from scrapy import cmdline
cmdline.execute('scrapy crawl anjuke -a local=hf'.split())
