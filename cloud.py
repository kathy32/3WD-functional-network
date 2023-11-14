# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 19:06:24 2019

@author: Administrator
"""

import numpy as np
import csv
import sys
import math
import random

def Cloud_positive(Ex,En,He,court): 
    '''一维正向高斯云算法P50'''
    Cloud_x = []
    Cloud_u = []
    i = 0
    while i<court:
        y = random.gauss(En,He)
        x = random.gauss(Ex,y)
        u = math.e**(-pow((x - Ex),2) / (2 * pow(y,2)))
        
        Cloud_x.append(x)
        Cloud_u.append(u)
        i += 1

    return Cloud_x,Cloud_u

def t_gaosi_g(y,miu,seita):
    result = np.ones_like(y) * math.e
    #print(1,result.shape)
    temp = np.power((y - miu),2) * -1 / (2*seita**2)
    #print(2,temp.shape)
    result = np.power(result,temp)
    #print(3,result.shape)
    return result / (np.sqrt(2*math.pi)*seita)

def t_L_k(x,miu,seita,aerfa,k):
    fenzi = t_gaosi_g(x,miu[k],seita[k]) * aerfa[k]
    fenmu = np.zeros_like(fenzi)
    for n in range(len(miu)):
        fenmu += aerfa[n] * t_gaosi_g(x,miu[n],seita[n])
    return fenzi / fenmu

def t_cal_J(y,y_count,aerfa,miu,seita,k):
    #目标函数P101-3
    J = 0
    y_count = np.array(y_count)
    J_ln = np.zeros_like(y_count)
    for i in range(k):
        #print(1,t_gaosi_g(y,miu[i],seita[i]))
        J_ln += aerfa[i] * t_gaosi_g(y,miu[i],seita[i])        
    #print(1,J_ln)
    J_ln = np.log(J_ln)
    #print(2,J_ln)
    J = y_count * J_ln
    #print(3,J)
    #sys.exit()
    return np.sum(J)

def t_update_can(data,aerfa,miu,seita,k):
    for k_ in range(k):            
        miu[k_] = np.sum(t_L_k(data,miu,seita,aerfa,k_) * data) / np.sum(t_L_k(data,miu,seita,aerfa,k_))
        seita[k_] = math.sqrt(np.sum(t_L_k(data,miu,seita,aerfa,k_) * np.power((data-miu[k_]),2)) / np.sum(t_L_k(data,miu,seita,aerfa,k_)))
        aerfa[k_] = np.sum(t_L_k(data,miu,seita,aerfa,k_)) / len(data)
        
    return aerfa,miu,seita

def t_gaosi_tran(data,k,target):

    miu = []
    seita = []
    aerfa = []
    y = []
    y_count = []
    
    #统计频度分布P100-1
    for d in data:
        if d in y:
            y_count[y.index(d)] += 1
        else:
            y.append(d)
            y_count.append(1)
    y_count = np.array(y_count)/data.shape[0]
    y = np.array(y)
    #print(y_count)
    
    
    from PIL import Image
    import matplotlib.pyplot as plt    
    
    # plt.figure("lena")
    # n, bins, patches = plt.hist(data, bins=256, normed=1, facecolor='green', alpha=0.75)
    # plt.show()
    
    #sys.exit()
    
    
    
    #初始化P101-2
    for i in range(k):
        miu.append((i+1)*data.max()/(k+1))
        seita.append(data.max())
        aerfa.append(1/k)
    #print(miu,seita,aerfa) 
    #print(data.shape,y.shape,y_count.shape)
    count = 1    
    while True:
        print('gaosi times:',count)
        #目标函数P101-3
        J = t_cal_J(y,y_count,aerfa,miu,seita,k)
        
        #更新参数P101-4
        aerfa,miu,seita = t_update_can(data,aerfa,miu,seita,k)
        #计算目标估计值P101-5
        J_update = t_cal_J(y,y_count,aerfa,miu,seita,k)
        count += 1
        #print(J_update,J)
        if abs(J_update - J)<target:
            break
    return aerfa,miu,seita

def t_cloud_tran(data,k,target):
    
    aerfa,miu,seita = t_gaosi_tran(data,k,target)
    Ex = []
    En = []
    He = []
    CD = []
    for i in range(len(aerfa)):
        Ex.append(miu[i])
        En.append((1+aerfa[i])*seita[i]/2)
        He.append((1-aerfa[i])*seita[i]/6)
        CD.append((1-aerfa[i])/(1+aerfa[i]))
    return Ex,En,He,CD

def t_calculate_certain(Ex,En,He,x):
    '''计算输入数据的确定度，Ex,En,He均为列表
    返回确定度列表，最大确定度索引'''
    cer = []
    for i in range(len(Ex)):
        y = En[i]#random.gauss(En[i],He[i])
        cer.append(math.e**(-pow((x - Ex[i]),2) / (2 * pow(y,2))))
    return cer, cer.index(max(cer))

def t_cal_muti_all(Ex,En,He,data,k):
    '''计算图像的完整多粒度信息'''
    multi_sharp = np.zeros((k,data.shape[0],data.shape[1]))
    muti_count = np.zeros(k)
    
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            _, t = t_calculate_certain(Ex,En,He,data[i][j])
            multi_sharp[t][i][j] = 1
            muti_count[t] += 1
            
    return multi_sharp, muti_count

def t_cal_muti_par(Ex,En,He,data,k):
    '''计算图像的多粒度骨干P55信息'''
    print(data.shape)
    multi_sharp = np.zeros((k,data.shape[0],data.shape[1]))
    muti_count = np.zeros(k)
    
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            for t in range(k):
                if data[i][j] >= Ex[t] - En[t] and data[i][j] <= Ex[t] + En[t]:
                    multi_sharp[t][i][j] = 1
                    muti_count[t] += 1
            
    return multi_sharp, muti_count