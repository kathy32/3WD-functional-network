# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 10:05:19 2020

@author: Administrator
"""

import networkx as nx
import csv
import numpy as np
import sys
import random

def read_data(path):
    result = []
    with open(path,"r") as csvfile:        
        reader = csv.reader(csvfile)
        for line in reader:
            if len(line) > 0:
                result.append(list(map(str,line)))
    result = np.array(result)
    return result

def write_csv(path,data):
    with open(path,'w',newline='') as csvfile:
        writer = csv.writer(csvfile)
        for i in range(len(data)):
            writer.writerow(data[i])
def cal_indegree(node,edges):
    indegree = 0
    for e in edges:
        if node == e[1]:
            indegree += 1
    return indegree-1
        
            
data = read_data('./data//before//Epinions//r_Epinions_15_in.csv') 
r_data = data[:,:3] 

fu = 0
dian = []

for rd in r_data:
    if rd[2] == '0.0':
        fu+=1
    if rd[0] not in dian:
        dian.append(rd[0])   
    if rd[1] not in dian:
        dian.append(rd[1])         

print(fu,len(dian))
 