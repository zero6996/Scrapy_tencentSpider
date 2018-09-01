# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
from tencentSpider.MySQLHelp import DBHelper


class TencentspiderPipeline(object):
    def process_item(self, item, spider):
        '''
        保存数据到json文件中
        '''
        with open('tencent.json','ab') as f:
            text = json.dumps(dict(item),ensure_ascii=False)+'\n'
            f.write(text.encode('utf-8'))
        return item

class TencentspiderPipelineToMysql(object):
    def process_item(self,item,spider):
        '''
        保存数据到数据库中
        '''
        dbhelper = DBHelper()
        positionName = item['positionName']
        positionLink = item['positionLink']
        positionType = item['positionType']
        positionNum = item['positionNum']
        positionSite = item['positionSite']
        positionTime = item['positionTime']
        sql = 'INSERT INTO tencent.tencentdata(positionName,positionLink,positionType,positionNum,positionSite,positionTime) VALUES(%s,%s,%s,%s,%s,%s)'
        params = (positionName,positionLink,positionType,positionNum,positionSite,positionTime)
        result = dbhelper.execute(sql,params)
        if result == True:
            print('Insert done!')
        else:
            print('Insert Failed!')
        return item