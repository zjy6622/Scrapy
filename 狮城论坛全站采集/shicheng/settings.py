# -*- coding: utf-8 -*-

# Scrapy settings for shicheng project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'shicheng'

SPIDER_MODULES = ['shicheng.spiders']
NEWSPIDER_MODULE = 'shicheng.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'shicheng (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    # 'Accept-Language': 'zh-CN,zh;q=0.9',
    # 'Cache-Control': 'max-age=0',
    # 'Connection': 'keep-alive',
    'Cookie': 'iZOJfd_c4f3_saltkey=VrC6RHEL; iZOJfd_c4f3_lastvisit=1569631703; _ga=GA1.2.2021789008.1569635304; _gid=GA1.2.1399047899.1569635305; PHPSESSID=7iam7q2ukvpr49uhj956bbteg3; iZOJfd_c4f3_visitedfid=220D1265D1279D253D65D243D140D215D212; UM_distinctid=16d75d03183336-05db3789d55da7-67e1b3f-1fa400-16d75d0318431a; CNZZDATA1252988760=1454382089-1569637213-%7C1569637213; iZOJfd_c4f3_home_diymode=1; iZOJfd_c4f3_st_t=0%7C1569673649%7C0d656c6c830d3d0b9afdc894d4fcff8f; iZOJfd_c4f3_forum_lastvisit=D_212_1569635477D_215_1569635492D_140_1569635590D_243_1569635597D_65_1569635604D_1265_1569638730D_220_1569673649; iZOJfd_c4f3_st_p=0%7C1569674422%7C70cb511fc15e0287bf0d68b5c01e18a1; iZOJfd_c4f3_viewid=tid_15817676; iZOJfd_c4f3_sendmail=1; _gat=1; iZOJfd_c4f3_lastact=1569674425%09connect.php%09check',
    'Host': 'bbs.sgcn.com',
    'Referer': 'https://bbs.sgcn.com/thread-15817676-1-1.html',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'shicheng.middlewares.ShichengSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'shicheng.middlewares.ShichengDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'shicheng.pipelines.ShichengPipeline': 300,
   'shicheng.pipelines.MySqlPipline': 301,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
