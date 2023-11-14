# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 20:36:11 2020

@author: Administrator
"""

import numpy as np
import csv
import random

def read_data(path):
    result = []
    with open(path,"r") as file:        
        lines = file.readlines()
        for line in lines:
            line = line.split(',')
            result.append(line)
    result = np.array(result)
    return result 

def write_csv(path,data):
    with open(path,"w",newline='') as csvfile: 
        writer = csv.writer(csvfile,delimiter=' ')
        for i in range(len(data)):
            writer.writerow(data[i])
            
for n in range(10):
    test_data = read_data('./result//test_temp//update//Slashdot//test_temp_d_'+str(n)+'.csv')
    train_data = read_data('./result//test_temp//update//Slashdot//train_temp_d_'+str(n)+'.csv')
    
    for t in test_data:
        t[2] = '?' + str(int(float(t[2])))
    for t in train_data:
        t[2] = '+' + str(int(float(t[2])))       
    
    listt = np.concatenate((test_data,train_data),axis=0).tolist()
    
    random.shuffle(listt)
    listt = np.array(listt)
    
    edgelist = listt[:,:2]
    edgelist = np.float32(edgelist)
    edgelist = np.int32(edgelist)
    
    temp = []
    for e in edgelist:
        if e[0] in temp:
            e[0] = temp.index(e[0])
        else:
            temp.append(e[0])
            e[0] = temp.index(e[0])
        if e[1] in temp:
            e[1] = temp.index(e[1])
        else:
            temp.append(e[1])
            e[1] = temp.index(e[1])
    
    dat = listt[:,2:3]    
    
    write_csv('./data//after//Slashdot'+ str(n) +'.edgelist',edgelist) 
    write_csv('./data//after//Slashdot'+ str(n) +'.dat',dat) 
    






