# CDNCheck
     该脚本可以进行CDN检测。主要原理是通过爬取站长之家的全球ping来识别CDN，一共选取了35个国内外节点，并且对全国各个省份的节点都进行了选择。同时支持单个域名和多个域名检测。

### 一、项目简介

#### 1.项目介绍
    该脚本可以进行CDN检测。主要原理是通过爬取站长之家的全球ping来识别CDN，一共选取了35个国内外节点，并且对全国各个省份的节点都进行了选择。该脚本使用python3编写，支持单个域名或文件方式检测，其中域名支持带http(https)，也可以支持不带http(https)。

#### 2.说明

(1):为了检测效果，一共选择了35个节点，如果觉得检测速度太慢，可自行删除部分节点，若觉得节点太少，准确率不高，也可自行增加节点。

(2):脚本执行完成之后，会在命令行打印出是否存在CDN，也会在当前目录下生成一个result.txt文件，将检测的结果写入，采用的是追加的方式写入到文件中，如果重新检测，可以删除result.txt文件

### 二、用法说明

#### 1.使用方法

(1):查看帮助

```
python3 cndcheck.py -h
python3 cndcheck.py --help
```
<img width="1137" alt="image" src="https://user-images.githubusercontent.com/53456907/155275419-7d506baa-d87a-46d5-8838-3ca49e218253.png">

<img width="1064" alt="image" src="https://user-images.githubusercontent.com/53456907/155275461-8d638cb2-3fb4-4f71-900f-83249513ff23.png">


(2):检测单个域名

```
python3 cndcheck.py -u domain
python3 cndcheck.py --url domain
```

(3):检测多个域名

```
python3 cndcheck.py -f url.txt
python3 cndcheck.py --filename url.txt
```


