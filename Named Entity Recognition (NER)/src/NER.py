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
        # string = re.findall('[A-Za-z0-9\x80-\xff]+', lines[i])
        line = re.sub('[【】？。，、《》]+', '', lines[i])
        strlist = re.findall(u"[\u2E80-\u9FFF]+", line)
        result.append(' '.join(strlist))	
        Rs2.append(result)#将该行分词写入列表形式的总分词列表
    #写入CSV
    file=open('cleaned.csv', 'w', encoding="utf-8", newline='')
    writer = csv.writer(file)#定义写入格式
    writer.writerows(Rs2)#按行写入
    file.close()

def stopwordslist(filepath):  
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]  
    return stopwords

def segment2(filename):
    lines = open(filename, encoding="utf-8").read().split('\n')  # Read line-by-line
    Rs2 = []  # 总分词列表
    for i in range(len(lines)):
        # Rs2.append(lines[i])
        tmpline = lines[i].split(',')  # 读取每一行分词
        tmpline.pop(0)
        tmpline.pop(0) ## 弹出前两个元素
        sentence_seged = jieba.cut(tmpline[0]) 
        stopwords = stopwordslist('./stopwords.txt')  # 这里加载停用词的路径 
        outstr = ''
        for word in sentence_seged:  
            if word not in stopwords:  
                if word != '\t' and re.findall(u"[\u2E80-\u9FFF]+", word)!=[]:  
                    outstr += word 
        #            outstr += " " 
        result=[]
        result.append(' '.join(jieba.cut(outstr)))
        Rs2.append(result)#将该行分词写入列表形式的总分词列表
        # print(Rs2)
    #写入CSV
    file=open('AfterSegmentation2.csv', 'w', encoding="utf-8", newline='')
    writer = csv.writer(file)#定义写入格式
    writer.writerows(Rs2)#按行写入
    file.close()

def tag(filename):
    lines = open(filename, encoding="utf-8").read().split('\n')  # Read line-by-line
    dictionary = open('data/highlight.csv', 'r', encoding="utf-8").read().split('\n')
    Rs2 = []  # 总Tag列表
    for i in range(len(lines)):
        # Rs2.append(lines[i])
        tmpline = lines[i].split(',')  # 读取每一行分词
        tmpline.pop(0)
        tmpline.pop(0) ## 弹出前两个元素
        result=[]
        p1=r"(\d{4}[年//-])?(\d{1,2}[月//-])?\d{1,2}[日:：](\d{1,2}[时h：:])?(\d{1,2}[分m:：])?(\d{1,2}[秒s])?"
        # if re.search(r"^\d{4}年\d{2}月\d{2}日", tmpline)
        if re.search(p1, str(tmpline)):
            match = re.search(p1, str(tmpline))
            # print(match.group()) 
            result.append(match.group()+'<time>')

        for j in range(len(dictionary)):
            sep_dictionary = dictionary[j].split(',')
            # print(sep_dictionary)
            # print(sep_dictionary[0])
            if re.search(sep_dictionary[0],str(tmpline)):
                result.append(dictionary[j])
        Rs2.append(result)#将该行分词写入列表形式的总分词列表
        # print(Rs2)
    #写入CSV
    file=open('Tag.csv', 'w', encoding="utf-8", newline='')
    writer = csv.writer(file)#定义写入格式
    writer.writerows(Rs2)#按行写入
    file.close()

if __name__ == '__main__':
#    preprocess('example.csv')
#    segment('AfterPreprocessed.csv')
    # clean('AfterSegmentation_space0.1.txt')
    # segment2('AfterPreprocessed.csv')
    tag('AfterPreprocessed.csv')

