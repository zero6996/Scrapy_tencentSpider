# -*- coding: utf-8 -*-
import scrapy
from tencentSpider.items import TencentspiderItem


class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']#设置域名范围
#    start_urls = ['http://hr.tencent.com/']
    start_urls = []
    for i in range(0,520,10):
        start_urls.append('https://hr.tencent.com/position.php?keywords=python&lid=0&tid=0&start='+str(i)+'#a')
    
    '''
    /html/body/div[3]/div[1]/table/tbody/tr[2]/td[1]/a # Name
    /html/body/div[3]/div[1]/table/tbody/tr[2]/td[1]/a # Link
    /html/body/div[3]/div[1]/table/tbody/tr[2]/td[2] # Type
    /html/body/div[3]/div[1]/table/tbody/tr[2]/td[3] # Num
    /html/body/div[3]/div[1]/table/tbody/tr[2]/td[4] # Site
    /html/body/div[3]/div[1]/table/tbody/tr[2]/td[5] # Time
    '''
    # 提取数据的逻辑,这里使用xpath,接受的是HTTP Response    
    def parse(self, response):
        for each in response.xpath("//tr[@class='even']|//tr[@class='odd']"):#这里的//tr表示选取所有的tr元素@class表示选取所有的class的属性
            item = TencentspiderItem()
            item['positionName'] = each.xpath('./td[1]/a/text()').extract()[0]
            item['positionLink'] = 'https://hr.tencent.com/'+each.xpath('./td[1]/a/@href').extract()[0]
            item['positionType'] = each.xpath('./td[2]/text()').extract()[0]
            item['positionNum'] = each.xpath('./td[3]/text()').extract()[0]
            item['positionSite'] = each.xpath('./td[4]/text()').extract()[0]
            item['positionTime'] = each.xpath('./td[5]/text()').extract()[0]
            yield item #返回数据给上层,并最终传递给piplines