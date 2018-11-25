from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
def cleanInput(input):
    input=re.sub("\n+"," ",input)
    input=re.sub("\[[0-9]*\]","",input)
    input=re.sub(" +"," ",input)
    input=bytes(input,"UTF-8")
    input=input("ascii","ignore")
    cleanInput=[]
    input=input.split(' ')
    for item in input:
#这里用import string和string.punctuation来获取Python所有的标点符号
#对内容中的所有单词进行清洗,单词两端的任何标点符号都会被去掉,但带连字符的单词
#仍然会保留
        item=item.strip(string.punctuation)
        if len(item)>1 or(item.lower()=='a' or item.lower()=='i'):
            cleanInput.append(item)

        return cleanInput
def ngrams(input,n):
    input=cleanInput(input)
    output=[]
    for i in range(len(input)-n+1):
        output.append(input[i:i+n])
    return output
