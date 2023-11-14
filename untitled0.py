# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 15:29:08 2020

@author: gangqZhang
"""

import re

def find_char(string,char):
    for i in range(len(string)):
        if string[i] == char:
            return i


data = []
with open('./fsolve.txt','r') as file:
    reader = file.readlines()
    for r in reader:
        if len(r)>4:
            data.append(r)

data_result = []
for d in range(len(data)-1):
    temp = data[d].replace('-', '+ -')
    temp = temp.replace('+ - (', '+ ( -')
    temp = temp.split('+')
    temp_result = ''
    for t in temp:
        if type(find_char(t,'*')) == type(1) and '/' in t:
            fenmu = t.split('/')[-1]
            fenzi = t.split('/')[0]
            fenzi_num = fenzi[:find_char(fenzi,'*')]
            xs = fenzi[find_char(fenzi,'*')+1:]
            temp_result += str(round(float(int(fenzi_num.strip()[1:]))/float(int(fenmu)),2)) + '*' + xs[:-1] + '+'
            # print(t,str(round(float(int(fenzi_num.strip()[1:]))/float(int(fenmu)),2)) + '*' + xs[:-1])
            # print(temp_result)
        else:
            if 'x' not in t:
                if '-' in t:
                    fu_temp = t.replace('-',' ')
                    fenmu = fu_temp.split('/')[-1]
                    fenzi = fu_temp.split('/')[0]
                    temp_result += str(-round(float(int(fenzi))/float(int(fenmu)),2)) + '+'
                else:
                    fenmu = fu_temp.split('/')[-1]
                    fenzi = fu_temp.split('/')[0]
                    temp_result += str(round(float(int(fenzi)) / float(int(fenmu)), 2)) + '+'
            else:
                temp_result += t

    data_result.append(temp_result[:-1])

data_result.append(data[-1])

with open('./1111.txt','w') as f:     #设置文件对象
    for d in data_result:
        f.write(d+'\n')
        f.write('\n')



