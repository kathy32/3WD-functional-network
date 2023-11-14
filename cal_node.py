# -*- coding: utf-8 -*-
"""
Created on Fri May  1 16:28:20 2020

@author: Administrator
"""
import csv

def read_data(path):
    result = []
    with open(path,"r") as csvfile:        
        reader = csv.reader(csvfile)
        for line in reader:
            if len(line) > 0:
                result.append(list(map(float,line)))
    return result

def cal_node(data_all):
    num = 0
    node = []
    for da in data_all:
        if da[0] not in node:
            node.append(da[0])
            num += 1
            
        if da[1] not in node:
            node.append(da[1])
            num += 1 
    print('node count:',num)
    print('edge count:',len(data_all))
    
    
    
#data_all = read_data('./data//before//Epinions//r_Epinions_15_in.csv')
#data_all = read_data('./data//before//Alpha//Alpha_15_2.csv')
#data_all = read_data('./data//before//DBLP//DBLP_15_2.csv')
#data_all = read_data('./data//before//Slashdot//Slashdot_15_2.csv')
data_all = read_data('./data//before//Wikivote_reduce//Wikivote_reduce_15_2.csv')
cal_node(data_all)

