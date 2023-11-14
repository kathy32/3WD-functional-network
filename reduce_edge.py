# -*- coding: utf-8 -*-
"""
Created on Fri May  1 16:40:31 2020

@author: Administrator
"""

import networkx as nx
import csv
import numpy as np
import sys

def read_data(path):
    result = []
    with open(path,"r") as csvfile:        
        reader = csv.reader(csvfile)
        for line in reader:
            if len(line) > 0:
                #print(list(map(str,line)))
                result.append(list(map(str,line)))
    #print(type(result[0][0]))
    result = np.array(result)
    #print(result.shape)
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
        
data = read_data('./data//before//Wikivote//Wikivote.csv')  
r_data = data[:,:3]           


G_asymmetric = nx.DiGraph()
for rd in r_data:
    G_asymmetric.add_edge(rd[0],rd[1])
    
    
    
    
    
    
    
    
    
    
    
    
    
    