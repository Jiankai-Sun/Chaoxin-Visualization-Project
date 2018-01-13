# Chaoxin Visualization Project
This is a Python project based on [jieba](https://github.com/fxsjy/jieba) to split sentences.
## File Structure
In folder `Named Entity Recognition (NER)`,
```
│  README.md
│
├─data
│      AfterPreprocessed.csv
│      AfterSegmentation_space0.1.txt
│      cleaned.csv
│      corpus.txt
│      highlight.csv
│      highlight.csv_bak
│      highlight.csv_bak2
│      stopwords.txt
│      Tag.csv
│
├─LINE
│      concatenate.cpp
│      distance.cpp
│      line.cpp
│      normalize.cpp
│      reconstruct.cpp
│      train.sh
│
├─src
│      LDA.py
│      NER.py
│      jieba_example.py
│      topic_model.ipynb
│      track_network.py
│
└─tf_model
        model-00010.param
        model-00010.tag
        model-00010.twords
        model-00010.wordmap
        model-00010.zvalue
```
* `data` folder: contains all the dataset
* `LINE` folder: the implementation of LINE Algorithm
* `src` folder: source code for LDA Algorithm (LDA.py), topic model in tensorflow (topic_model.ipynb), main function (track_network.py & NER.py) and an example file to use jieba library (jieba_example.py)
* `tf_model` folder: TensorFlow models.

## How to use
* Check the topic model visualization with `topic_model.ipynb`, you can open it with `jupyter notebook`.
* `NER.py` contains some main functions for preprocessing the dataset, segmentation, cleaning and tag.

## Acknowledgement
Topic Model

[如何用 Python 从海量文本抽取主题？](https://www.leiphone.com/news/201707/Pe5LRySEwvi6vKiA.html)
