#usr/bin/python
# -*-coding=utf-8 -*-

# Requirements: Python 3.5.2 (default, Nov 17 2016, 17:05:23) 
#               jieba 0.39

import jieba
import numpy as np
import csv
import re

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
        result.append(' '.join(jieba.cut(tmpline[0])))
        Rs2.append(result)#将该行分词写入列表形式的总分词列表
    #写入CSV
    file=open('AfterSegmentation.csv', 'w', encoding="utf-8", newline='')
    writer = csv.writer(file)#定义写入格式
    writer.writerows(Rs2)#按行写入
    file.close()


def clean(filename):
    lines = open(filename, encoding="utf-8").read().split('\n')  # Read line-by-line
    Rs2 = []  # 总分词列表
    for i in range(len(lines)):
        result=[]
        # Rs2.append(lines[i])
        string = re.findall(']A-Za-z0-9\x80-\xff]+', lines[i])
        Rs2.append(string)#将该行分词写入列表形式的总分词列表
    #写入CSV
    file=open('cleaned.csv', 'w', encoding="utf-8", newline='')
    writer = csv.writer(file)#定义写入格式
    writer.writerows(Rs2)#按行写入
    file.close()

if __name__ == '__main__':
    clean('AfterSegmentation_space0.1.txt')

