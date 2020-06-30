#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : dataModel.py
# @Author: Small-orange
# @Date  : 2020-6-21
# @Desc  : 构造测试json数据模型

import json

class Clumns(object):
    def __init__(self,field,width,title,sort):
        self.field = field
        self.width = width
        self.title = title
        self.sort = sort

# 给表的字段和Clumns对应
def setField(tb_name):
    list = []
    if tb_name == 'student':
        stu1 = Clumns('id',80,'ID',True)
        stu2 = Clumns('name', 80, '姓名', False)
        stu3 = Clumns('sex', 80, '性别', False)
        stu4 = Clumns('age', 80, '年龄', False)
        list.append(stu1.__dict__)
        list.append(stu2.__dict__)
        list.append(stu3.__dict__)
        list.append(stu4.__dict__)
    elif tb_name == 'RESSAGAMMA_1':
        wel_1 = Clumns('WID',80,'井号',True)
        wel_2 = Clumns('DATETIME', 80, '时间',False)
        wel_2 = Clumns('TEMP', 80, '温度', False)
        wel_3 = Clumns('RESNINC', 120, '电阻率近井斜',False)
        wel_4 = Clumns('GMCount', 120, '自然伽马计数',False)
        wel_5 = Clumns('GMAPI', 120, '自然伽马API',False)
        wel_6 = Clumns('R12PHF', 120, '2M远天线相位差',False)
        wel_7 = Clumns('R12PLF', 120, '400K远天线相位差',False)
        wel_8 = Clumns('R12AHF', 120, '2M远天线幅度比',False)
        wel_9 = Clumns('R12ALF', 120, '400K远天线幅度比',False)
        wel_10 = Clumns('R34PHF', 120, '2M近天线相位差',False)
        wel_11 = Clumns('R34PLF', 120, '400K近天线相位差',False)
        wel_12 = Clumns('R34AHF', 120, '2M近天线幅度比',False)
        wel_13 = Clumns('R34ALF', 120, '400K近天线幅度比',False)
        wel_14 = Clumns('RGMCount', 120, '电阻率自然伽马计数',False)
        wel_15 = Clumns('RGMAPI', 120, '电阻率自然伽马API',False)
        wel_16 = Clumns('UPGMCount', 120, '电阻率上伽马计数',False)
        wel_17 = Clumns('UPGMAPI', 120, '电阻率上伽马API',False)
        wel_18 = Clumns('DOWNGMCount', 120, '电阻率下伽马计数',False)
        wel_19 = Clumns('DOWNGMAPI', 120, '电阻率下伽马API',False)
        list.append(wel_1.__dict__)
        list.append(wel_2.__dict__)
        list.append(wel_3.__dict__)
        list.append(wel_4.__dict__)
        list.append(wel_6.__dict__)
        list.append(wel_7.__dict__)
        list.append(wel_8.__dict__)
        list.append(wel_9.__dict__)
        list.append(wel_10.__dict__)
        list.append(wel_11.__dict__)
        list.append(wel_12.__dict__)
        list.append(wel_13.__dict__)
        list.append(wel_14.__dict__)
        list.append(wel_15.__dict__)
        list.append(wel_16.__dict__)
        list.append(wel_17.__dict__)
        list.append(wel_18.__dict__)
        list.append(wel_19.__dict__)
    print('----',json.dumps(list,ensure_ascii=False) )
    return list

#测试
# setField('student')






#字典
# base1 = {}
# base2 = {}
# base3 = {}
# base4 = {}
# dict1 = {}
# dict1['title'] = 'class'
# dict1['id'] = 1
# base1['title'] = 'stu1'
# base1['id'] = 1
# base2['title'] = 'stu2'
# base2['id'] = 1
# child_list = []
# child_list.append(base1)
# child_list.append(base2)
# dict1['children'] = child_list
# dict2 = {}
# dict2['title'] = 'class'
# dict2['id'] = 2
# base3['title'] = 'stu3'
# base3['id'] = 3
# base4['title'] = 'stu4'
# base4['id'] = 4
# child_list1 = []
# child_list1.append(base3)
# child_list1.append(base4)
# dict2['children'] = child_list1
# list = []
# list.append(dict1)
# list.append(dict2)
#
# jstr = json.dumps(list)
# print('-----',jstr)


