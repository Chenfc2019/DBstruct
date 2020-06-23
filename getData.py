#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : getData.py
# @Author: Small-orange
# @Date  : 2020-6-20
# @Desc  : 获取数据库信息

import requests
import json
from sqlalchemy import create_engine

#获取数据库连接
#root:数据库用户名
#123456：密码
#localhost:数据库主机地址
#3306：端口号
#demo01：数据库名称
def databaseCon():
    # 创建数据库连接
    engine = create_engine('mysql+pymysql://root:123456@localhost:3306/demo01')
    return engine

#根据数据库名获取表名
def getTableName(conn,db_name):
    #字符串拼接，有sql注入风险，需要优化
    sql = 'select table_name from information_schema.tables where table_schema=%s'
    tb_list = []
    result = conn.execute(sql,db_name)
    for tb in result:
        tb_list.append(tb[0])
        # print('\t\t----',tb)
    return tb_list

#获取数据库名
def getDBName(conn):
    sql = 'show DATABASES'
    # 获取所有数据库名
    result = conn.execute(sql)
    dbname_list = []
    for res in result:
        dbname_list.append(res[0])
        # print('----dbname:', res)
    return dbname_list

def getDbInfo():
    # 获取数据库连接
    engine = databaseCon()
    # 连接到数据库
    conn = engine.connect()
    #获取数据库名
    db_list = getDBName(conn)
    #构造map(数据库名，List表名)
    name_map = {}
    list = []
    #获取数据库下表的名称
    for db in db_list:
        tb_list = getTableName(conn, db)
        # print('--{}--'.format(db),tb_list)
        name_map[db] = tb_list

    print('----', json.dumps(name_map, ensure_ascii='false'))
    # print('name_map:',name_map)

    return db_list;

#根据数据库名获取表名
def getTBname(conn,db_name):
    sql = 'select table_name from information_schema.tables where table_schema=%s'
    result = conn.execute(sql,db_name)
    index = 0
    tb_list = []
    for tb in result:
        tb_dict = {}
        index = index + 1
        tb_dict['title'] = tb[0]
        tb_dict['id'] = index
        tb_list.append(tb_dict)
        # print('\t\t----',tb)
    return tb_list

#构造树形数据模型
def dataModel():
    # 获取数据库连接
    engine = databaseCon()
    # 连接到数据库
    conn = engine.connect()
    # 获取数据库名
    db_list = getDBName(conn)
    list = []
    # 获取数据库下表的名称
    index = 0
    for db in db_list:
        index = index + 1
        father = {}
        father['title'] = db
        father['id'] = index
        # tb_list = getTableName(conn, db)
        child = getTBname(conn,db)
        father['children'] = child
        list.append(father)

    jsonStr = json.dumps(list,ensure_ascii=False)
    print('--jsonStr--',jsonStr)
    return jsonStr

#根据表名获取表数据
def getTBdataFromDB(tb_name):
    # 获取数据库连接
    engine = databaseCon()
    # 连接到数据库
    conn = engine.connect()
    sql = 'select * from ' + tb_name
    result = conn.execute(sql)
    list = []

    for tb in result:
        print('----',tb)
        dict = {}
        dict['id'] = tb[0]
        dict['name'] = tb[1]
        dict['score'] = tb[2]
        list.append(dict)
    # print('----',list)
    return list
    # print('--表中数据--',json.dumps(list,ensure_ascii=False))

#测试构造的json数据格式
#dataModel()
#测试获取表数据
#getTBdataFromDB('student')

