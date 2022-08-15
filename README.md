# Scrapy_tencentSpider
腾讯招聘信息爬虫

## 1. 创建项目
  scrapy startproject tencentSpider
## 2. 创建一个基础爬虫模板
  cd tencentSpider
  scrapy genspider example example.com
  example:模板名称
  example.com:模板目标域名/地址
## 3. 修改爬虫逻辑,完成定制工作
  A,修改settings.py
    1.注释掉Rbotos协议
    2.打开anders选项,添加UA
    3.关闭cookies
    4.打开了PIPELINES,准备保存数据
  B,修改items.py
    以下示例爬取腾讯招聘网站数据,设定获取后数据的格式
	positionName = scrapy.Field() # 职位名称
	positionLink = scrapy.Field() # 职位链接
	positionType = scrapy.Field() # 职位类型
  C,修改piplines.py
	可以写入json格式文件,或保存到数据库
  D,修改爬虫主体逻辑,tencent.py
	主要制定需要爬取的具体信息
## 4. 运行爬虫
  scrapy crawl tencent
