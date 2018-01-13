import jieba
import re
import csv

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
        if(i%10000 == 0): print(i)
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
        line = re.sub('[【】？。，、《》\d]+', '', lines[i])
        strlist = re.findall(u"[\u2E80-\u9FFF]+", line)
        if(len(strlist) == 0): continue
        result.append(' '.join(strlist))	
        Rs2.append(result)#将该行分词写入列表形式的总分词列表
    #写入CSV
    file=open('cleaned.csv', 'w', encoding="utf-8", newline='')
    writer = csv.writer(file)#定义写入格式
    writer.writerows(Rs2)#按行写入
    file.close()

def track_network(filename):
    lines = open(filename, encoding="utf-8").read().split('\n')
    dic = dict()
    for i in range(len(lines)):
        if(i%10000==0):print(i)
        text = lines[i].split(' ')
        if(len(text) < 4): continue
        j = 0
        while(j <= len(text) - 5):
            for k in range(1,5):
                if(text[j] == text[j+k]):continue
                edge = text[j] + ' ' + text[j+k]
                if(edge in dic): dic[edge] +=1
                else: dic[edge] = 1
                edge = text[j+k] + ' ' + text[j]
                if(edge in dic): dic[edge] +=1
                else: dic[edge] = 1
            j += 1
        for k in range(1,4):
            if(text[j] == text[j+k]):continue
            edge = text[j] + ' ' + text[j+k]
            if(edge in dic): dic[edge] +=1
            else: dic[edge] = 1
            edge = text[j+k] + ' ' + text[j]
            if(edge in dic): dic[edge] +=1
            else: dic[edge] = 1
        j += 1
        for k in range(1,3):
            if(text[j] == text[j+k]):continue
            edge = text[j] + ' ' + text[j+k]
            if(edge in dic): dic[edge] +=1
            else: dic[edge] = 1
            edge = text[j+k] + ' ' + text[j]
            if(edge in dic): dic[edge] +=1
            else: dic[edge] = 1
        j += 1
        for k in range(1,2):
            if(text[j] == text[j+k]):continue
            edge = text[j] + ' ' + text[j+k]
            if(edge in dic): dic[edge] +=1
            else: dic[edge] = 1
            edge = text[j+k] + ' ' + text[j]
            if(edge in dic): dic[edge] +=1
            else: dic[edge] = 1
    file=open('network.txt', 'w', encoding="utf-8")
    for i in dic:
        if(dic[i] < 2):continue
        file.write(i)
        file.write(" %d\n" % dic[i])
    file.close()

if __name__ == '__main__':
    jieba.load_userdict("5万公司简称.txt")
    #print("begin segment")
    #segment('AfterPreprocessed.csv')
    print("begin clean")
    clean('AfterSegmentation.csv')
    track_network('cleaned.csv')