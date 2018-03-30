# -*- coding: utf-8 -*-

# Scrapy settings for Question project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Question'

SPIDER_MODULES = ['Question.spiders']
NEWSPIDER_MODULE = 'Question.spiders'

HTTPERROR_ALLOWED_CODES = [403]#上面报的是403，就把403加入。
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Question (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True
# DEFAULT_REQUEST_HEADERS = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.18 Safari/537.36',
#     'Accept':'application/json, text/javascript, */*; q=0.01',
#     'Accept-Encoding':'gzip, deflate',
#     'Accept-Language':'zh-CN,zh;q=0.9',
#     'Connection':'keep-alive',
#     'Cookie':'JYERN=0.13373971236816584; JYERN=0.29750417728463074; remind_check=1; QS_ED=13; QS_GD=3; QS_TM=1; j_math3_q_q_0=a7b3c3f4-60c7-4d77-8bbb-3ed17d240b0b~75608b62-b081-4862-8214-1b45b72cd0ec~; j_math3_q_ct=0; j_math3_q_dg=0; j_math3_q_fg=0; j_math3_q_so=0; j_math3_q_so2=0; j_math3_q_po=0; j_math3_q_pd=1; j_q_lbs=; jyean=aasgGf7K9YW29wGeDYWhnIB1FWJO17wbrrqbnf-4MLGgzeWK0FB33OVPM5bmQItR5jv85abvlczJ72rnNmoksI_2aafAKlTQcj6fSsjORHO1IzDI3vqR4VOKmtuFxG-U0; UM_distinctid=1626b9a9ce25d-0d93560c66728-681f1b7e-1fa400-1626b9a9ce3211; jy=4823353F9AADD97EA62E47C1920908E42CA7FA404DA00F46A9EDCC8F785B2097DE554B3D83E36B9257273D4FDD647E582B818EC4EDF7C193094D31B93AF4F01271F20D8BD417F502B0F745B391C5813655D8ECE32B8F09C006A2D69ACC80ECCE1ABF0FC8954A6B173A0C54C19A74F867CCC3DFAF4F959EAA86EB2176AA626B7CFA3BDC78A316157EAF6209383DEA10823C34B580567F4475C055B9E7EC2C419E643DC3388632806D65452C4EC21DB0FCD046C5B8EF0C5DCC25B0CD45763A21A6781D00CA2CC06BB31897E0BAED5DB16AE5EDC144C9491614910166ECBB95A6474318ED8615092212504412D625F5AACF5D6337C9706CB44F31551CDF48CCE32E224D0BF5D7A1CD49032FA8C6DCF2F14386E636FE7F0995070BA7699836BF0AAEF0C1F7E15E9F7F57A4F5BE1D70F86E76F1D243752611A6E76F28A4B032AEA25702AF9628570122B7485DE6A3DA8CDF49; CNZZDATA2018550=cnzz_eid%3D1427837169-1522218522-%26ntime%3D'+str(t.time()),
#     'Referer':'http://www.jyeoo.com/math3/ques/detail/510077aa-1529-4315-56f5-73ee1be255da',
#     'Host':'www.jyeoo.com',
# }

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
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
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'Question.middlewares.QuestionSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'Question.middlewares.QuestionDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'Question.pipelines.QuestionPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
