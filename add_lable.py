# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 11:31:26 2019

@author: Administrator
"""
import numpy as np
import csv

def read_data(path):
    result = []
    with open(path,"r") as file:        
        lines = file.readlines()
        for line in lines:
            line = line.split()
            result.append(line)
    #result = np.array(result)
    return result 

def write_csv(path,data):
    with open(path,"w",newline='') as csvfile: 
        writer = csv.writer(csvfile)
        for i in range(len(data)):
            writer.writerow(data[i])
            

data_nol = read_data('./data//tang//epinion.edgelist')          
data_l = read_data('./data//tang//epinion.dat')
for i in range(len(data_nol)):
    data_nol[i].append(data_l[i][0][-1:])
    #data_nol[i].append(data_l[i][0][:1])
            
write_csv('./data//tang//epinion_all.csv',data_nol)  
            