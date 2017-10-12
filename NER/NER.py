#usr/bin/python
# -*-coding=utf-8 -*-

# Requirements: Python 3.6
#               jieba

import jieba
import numpy as np
import pandas as pd
import csv

# file_object2=open('D:\A仲敏2015\python_code\\advice.csv').read().split('\n')  #一行行的读取内容
# Rs2=[] #建立存储分词的列表
# for i in range(len(file_object2)):
#     result=[]
#     seg_list = jieba.cut(file_object2[i])
#     for w in seg_list :#读取每一行分词
#         result.append(w)
#     Rs2.append(result)#将该行分词写入列表形式的总分词列表
# #写入CSV
# file=open('D:\Azhongmin2015\python_code\\result2.csv','w')
# writer = csv.writer(file)#定义写入格式
# writer.writerows(Rs2)#按行写入
# #file.write(str(Rs))
# file.close()

# Remove English commas in Chinese sentences
def preprocess(filename):
    lines = open(filename, encoding="utf-8").read().split('\n')   # Read line-by-line
    Table = [] #总分词列表

    for i in range(len(lines)):
        result=[]
        segment = lines[i].split(',')#读取每一行分词
        result.append(segment[0])
        segment.pop(0)

        result.append(segment[0])
        segment.pop(0)
        result.append('，'.join(segment))
        # 将该行分词写入列表形式的总分词列表
        Table.append(result)
    #write csv file
    file = open('AfterPreprocessed.csv', 'w', encoding="utf-8", newline='')
    writer = csv.writer(file)  #定义写入格式
    writer.writerows(Table)  #按行写入
    file.close()

def segment(filename):
    lines = open(filename, encoding="utf-8").read().split('\n')  # Read line-by-line
    Rs2 = []  # 总分词列表
    for i in range(len(lines)):
        result=[]
        # Rs2.append(lines[i])
        tmpline = lines[i].split(',')  # 读取每一行分词
        tmpline.pop(0)
        tmpline.pop(0) ## 弹出前两个元素
        # print(i)
        result.append('/'.join(jieba.cut(tmpline[0])))
        Rs2.append(result)#将该行分词写入列表形式的总分词列表
    #写入CSV
    file=open('AfterSegmentation.csv', 'w', encoding="utf-8", newline='')
    writer = csv.writer(file)#定义写入格式
    writer.writerows(Rs2)#按行写入
    file.close()

if __name__ == '__main__':
    segment('AfterPreprocessed.csv')

