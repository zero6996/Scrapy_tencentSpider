#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 10:10:49 2018

@author: zero
"""

import pymysql

class DBHelper:
    '''
    完成所有对mysql数据库的处理
    '''
    
    def __init__(self,host='127.0.0.1',port=3306,user='yourusername',pwd='yourpwd',db='tencent',charset='utf8'):
        self.host = host
        self.port = port
        self.user = user
        self.pwd = pwd
        self.db = db
        self.charset = charset
        self.conn = None # 连接
        self.cur = None # 游标
    def connectDataBase(self):
        '''
        连接数据库
        '''
        try:
            self.conn = pymysql.connect(host=self.host,port=self.port,user=self.user,
                                        password=self.pwd,db=self.db,charset=self.charset)
        except:
            print('连接错误')
            return False
        self.cur = self.conn.cursor() #创建一个游标对象
        return True
    
    def close(self):
        '''
        关闭数据库
        '''
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()
        return True
    
    def execute(self,sql,params=None):
        '''
        执行sql语句
        '''
        if self.connectDataBase() == False:
            return False
        try:
            if self.conn and self.cur:
                self.cur.execute(sql,params)#执行sql语句
                self.conn.commit()
        except:
            print('执行'+sql+'错误')
            return False
        return True

if __name__ == '__main__':
    dbhelper = DBHelper()
    print(dbhelper.connectDataBase())
    print(dbhelper.close())
