# -*- coding: utf-8 -*-

# Scrapy settings for juzi_death_company project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'juzi_death_company'

SPIDER_MODULES = ['juzi_death_company.spiders']
NEWSPIDER_MODULE = 'juzi_death_company.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) \
                Chrome/71.0.3578.98 Safari/537.36"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.5
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Cookie": "gr_user_id=8b2a0647-ed6e-4da9-bd79-0927840738ba; _\
        ga=GA1.2.1065816449.1520818726; MEIQIA_EXTRA_TRACK_ID=11oNlg9W4BPRdVJbbc5Mg9covSB; \
        _gid=GA1.2.1051909062.1524629235; acw_tc=AQAAADMxgTrydgkAxrxRZa/yV6lXP/Tv; \
        Hm_lvt_1c587ad486cdb6b962e94fc2002edf89=1524629235,1524637618,1524702648; \
        gr_session_id_eee5a46c52000d401f969f4535bdaa78=5ac2fdfd-b747-46e3-84a3-573d49e8f0f0_true; \
        identity=1019197976%40qq.com; remember_code=N8cv8vX9xK; unique_token=498323; \
        acw_sc__=5ae1302fee977bcf1d5f28b7fe96b94d7b5de97c; session=e12ae81c38e8383dcaeaaff9ded967758bc5a01c; \
        Hm_lpvt_1c587ad486cdb6b962e94fc2002edf89=1524707391",
        "Host": "www.itjuzi.com",
        "Referer": "https://www.itjuzi.com/deathCompany",
        "If-Modified-Since": "Thu, 26 Apr 2018 01:49:47 GMT",
        "Upgrade-Insecure-Requests": "1"
    }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'juzi_death_company.middlewares.JuziDeathCompanySpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'juzi_death_company.middlewares.JuziDeathCompanyDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'juzi_death_company.pipelines.JuziDeathCompanyPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
