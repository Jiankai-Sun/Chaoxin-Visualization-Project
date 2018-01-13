#usr/bin/python
# encoding=utf-8

# Requirements: Python 3.6
#               jieba

import jieba

seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
print("Full Mode: " + "/" .join(seg_list))   #全模式

seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
print("Default Mode: " + "/" .join(seg_list))   #精确模式

seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
print(" ".join(seg_list))

print('/'.join(jieba.cut('如果放到post中将出错。', HMM=False)))
