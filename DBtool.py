#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : DBtool.py
# @Author: Small-orange
# @Date  : 2020-6-26
# @Desc  : 数据库连接工具类

import requests
import json
import pyodbc
from sqlalchemy import create_engine,MetaData,Table,Column,Integer,String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#获取数据库连接
#root:数据库用户名
#123456：密码
#localhost:数据库主机地址
#3306：端口号
#demo01：数据库名称
def databaseCon():
    # 创建数据库连接
    engine = create_engine(r'mssql+pyodbc://DESKTOP-OTDORG6\cfc:orange@flask_server64',echo=True)
    return engine

#获取数据库名称
def getDBName(conn):
    sql = "SELECT name FROM  master..sysdatabases WHERE name NOT IN ( 'master', 'model', 'msdb', 'tempdb', 'northwind','pubs' )"
    # 获取所有数据库名
    result = conn.execute(sql)
    dbname_list = []
    for res in result:
        dbname_list.append(res[0])
        # print('----dbname:', res)
    return dbname_list

#根据数据库名获取表名
def getTBname(conn,db_name):
    sql = "SELECT Name FROM {}..SysObjects where XType='U' ORDER BY Name ".format(db_name)
    result = conn.execute(sql)
    index = 0
    tb_list = []
    for tb in result:
        tb_dict = {}
        index = index + 1
        tb_dict['parentId'] = db_name
        tb_dict['title'] = tb[0]
        tb_dict['id'] = index
        tb_list.append(tb_dict)
        # print('\t\t----',tb)
    return tb_list

#构造树形数据模型
def treeDataModel():
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

meta = MetaData()
users_table = Table('student', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('sex', String(10)),
    Column('age', Integer)
)

#根据选中的数据库中的表获取表中的数据
def getTableData(tb_name,db_name):
    # 获取数据库连接
    engine = databaseCon()
    # 连接到数据库
    conn = engine.connect()
    sql = 'select * from {}..{};'.format(db_name,tb_name)
    print('sql:',sql)
    rest = conn.execute(sql)
    print('----',rest)
    # dic = dict((zip(result.keys(), result)))
    # print(dic)
    list = []
    # for dt in rest.fetchall():
    #     print(dt)

    field_li = [k[0] for k in rest.cursor.description]

    # 所有数据
    data_all = rest.fetchall()  # 查询所有数据，fetchall()或fetchone()要放到description后面，否则会报错
    result_list = []
    for data in data_all:
        result = dict(zip(field_li, data))
        result_list.append(result)

    # [{字段1:字段1的值,字段2:字段2的值，...},{字段1:字段1的值,字段2:字段2的值，...}.....]
    print('--ret_list--',json.dumps(result_list,ensure_ascii=False) )
    return result_list
#创建orm映射类
#创建基类，返回定制的metaclass类
#自定义与表对应的类
Base = declarative_base()
class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    sex = Column(String(20))
    age = Column(Integer)
    def to_dict(self):
        '''
        将查询结果转化为字典
        :return:
        '''
        return {k: v for k, v in self.__dict__.items() if k != "_sa_instance_state"}

    #创建session用于数据库操作
    # DBsession = sessionmaker(bind=databaseCon())
    # session = DBsession()


def test():
    # 获取数据库连接
    engine = databaseCon()
    # 连接到数据库
    conn = engine.connect()
    # 获取数据库名
    db_list = getDBName(conn)
    print('数据库名：',db_list)

# test()

# treeDataModel()
# getTableData('student','demo01')