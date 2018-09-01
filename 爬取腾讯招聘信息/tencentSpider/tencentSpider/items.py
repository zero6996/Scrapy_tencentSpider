# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    positionName = scrapy.Field() # 职位名称
    positionLink = scrapy.Field() # 链接
    positionType = scrapy.Field() # 类型
    positionNum = scrapy.Field() # 数量
    positionSite = scrapy.Field() # 地点
    positionTime = scrapy.Field() # 时间
