# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 21:52:02 2019

@author: Administrator
"""

import csv
import numpy as np

def read_data(path):
    result = []
    with open(path,"r") as csvfile:        
        reader = csv.reader(csvfile)
        for line in reader:
            if len(line) > 0:
                line = line[:-1]
                result.append(list(map(int,line)))
    #result = np.array(result)
    return result 

def write_csv(path,data):
    with open(path,"w",newline='') as csvfile: 
        writer = csv.writer(csvfile)
        for i in range(len(data)):
            writer.writerow(data[i])

def cal_SH(data):
    node_id = []
    node_sort = []
    for d in data:
        if d[0] not in node_id:
            node_id.append(d[0])
            node_sort.append([d[0],d[7]])
        if d[1] not in node_id:
            node_id.append(d[1])
            node_sort.append([d[1],d[8]]) 
    
    node_sort = sorted(node_sort,key=lambda x:x[1])
    node_sort = np.array(node_sort)
    SHole = node_sort[:int(len(node_sort)/100)]
    node_id = []
    for sh in SHole:
        node_id.append(sh[0])
    for d in data:
        if d[0] not in node_id and d[1] not in node_id:
            d.append(0)
        else:
            d.append(1)
            
    return data

def read_dat(path):
    result = []
    with open(path,"r") as file:        
        reader = file.readlines()
        for line in reader:
            if len(line) > 0:
                result.append(line)
    return result 

def cal_SB(data, triangle_data):          
    for d in data:
        is_t = 0
        for td in triangle_data:
            if d[0] in td and d[1] in td:
                is_t = 1
                break
        d.append(d[9]*is_t)
        
    return data


#计算SH
data = read_data('./data//Epinions//Epinions.csv')
data = cal_SH(data)

triangle_data_r = read_dat('./data//Epinions//epinions.dat')
triangle_data_r = triangle_data_r[7686:]  # 
triangle_data = []
for td in triangle_data_r:
    td = td.split()[1:-1]
    td = list(map(int,td))
    triangle_data.append(td)
    
data = cal_SB(data, triangle_data)
write_csv('./data//Epinions//Epinions_sh_sb.csv',data)

















