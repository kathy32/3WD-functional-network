# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 19:03:27 2019

@author: Administrator
"""

import numpy as np
import copy
import operator
import csv
import random
import sys

way_con = 0

W = ['A_','B_','C_','D_','E_','F_','G_','H_']

concate = ['*','+']

'''
#Wikivote 0.19 约11,6
net_stru = [['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14'],
            ['1_5','12_13','3_12','5_12','9_12','3_13','2_4','2_7','2_9','3_5','4_7','4_9','7_9'],
            ['3,12_3,13_12,13','2,4_2,9_4,9','2,7_2,9_7,9','4,7_4,9_7,9'],
            ['3,12,13_2,4,9_2,7,9_4,7,9_1,5_5,12_9,12_3,5_0_8_10_14']
            ]
'''
'''
#Wikivote 0.23 约11,6
net_stru = [['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14'],
            ['12_13','3_12','9_12','3_13','2_9','4_9'],
            ['12,13_3,12_9,12_3,13_2,9_4,9_0_1_5_7_8_10_14']
            ]
''' 
'''
#Wikivote 0.315 
net_stru = [['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14'],
            ['3_12','6_12','6_13','3_6'],
            ['3,12_6,12_6,13_3,6_0_1_2_4_5_7_8_9_10_14']
            ]
'''

# #Slashdot 0.24
# net_stru = [['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14'],
#             ['1_5','1_9','9_10','6_12','2_7','2_9','3_6','3_9','6_9','7_9'],
#             ['1,5_1,9_9,10_6,12_2,7_2,9_3,6_3,9_6,9_7,9_0_4_8_13_14']
#             ]

#Slashdot 0.24
net_stru = [['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14'],
            ['0_9','1_5','1_9','3_10','9_10','3_12','6_12','2_7','2_9','3_6','3_7','3_9','5_9','6_7','6_9','7_9'],
            ['1,5_1,9_5,9','3,6_3,12_6,12','2,7_2,9_7,9','3,6_3,9_6,9'],
            ['1,5,9_3,6,12_2,7,9_3,6,9_7,9_6,9_6,7_5,9_3,9_3,7_3,6_2,9_2,7_6,12_3,12_9,10_3,10_1,9_1,5_0,9_4_8_13_14']
            ]

'''
#Slashdot 0.24约11,6
net_stru = [['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14'],
            ['1_5','1_9','9_10','2_7','2_9','3_9','7_9'],
            ['1,5_1,9_9,10_2,7_2,9_3,9_6,9_7,9_0_4_8_12_13_14']
            ]
'''
 
'''
#DBLP 0.37
net_stru = [['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14'],
            ['8_12','8_13','8_14','2_7','4_5'],
            ['8,12_8,13_8,14_2,7_4,5_0_1_2_3_6_9_10_14']
            ] 
'''
# #DBLP 0.33
# net_stru = [['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14'],
#             ['1_8','8_10','8_12','8_13','8_14','2_7','2_8','2_9','4_5','4_8','4_9','5_9','7_8','7_9','8_9'],
#             ['2,7_2,8_7.8','2,7_2,9_7.9','4,5_4,8_5,8','4,5_4,9_5,9'],
#             ['2,7,8_2,7,9_4,5,8_4,5,9_8,9_8,14_8,13_8,12_8,10_1,8_0_3_6_12']
#             ]

#alpha 0.28
net_stru = [['0','1','2','3','4','5','6','7','8','9','10','12'],
            ['0_10','0_9','1_10','1_5','10_8'],
            ['0,10_0,9_1,10_1,5_8,10_2_3_4_6_7_8_9_12']
            ] 

# #alpha 0.21
# net_stru = [['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14'],
#             ['0_10','0_2','0_4','0_9','1_10','1_3','1_5','2_10','4_10','5_10','7_10','8_10','9_10','6_12','2_4','2_9','3_5','4_9','0,4_0,10_4,10','0,9_0,10_9,10','0,2_0,9_2,9','0,4_0,9_4,9','1,5_1,10_5,10','1,3_1,5_3,5','4,9_4,10_9,10','2,4_2,9_4,9'],
#             ['0,4_0,10_4,10','0,9_0,10_9,10','0,2_0,9_2,9','0,4_0,9_4,9','1,5_1,10_5,10','1,3_1,5_3,5','4,9_4,10_9,10','2,4_2,9_4,9'],
#             ['2,4,9_4,9,10_1,3,5_1,5,10_0,4,9_0,2,9_0,9,10_0,4,10_4,9_3,5_2,9_2,4_6,12_9,10_8,10_7,10_5,10_4,10_2,10_1,5_1,3_1,10_0,9_0,4_0,2_0,10_13_14']
#             ]

'''
#Epinions 0.295
net_stru = [['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14'],
            ['0_13','0_4','1_5','10_13','6_10','6_12','4_13','6_13','2_4','3_5'],
            ['0,13_0,4_1,5_10,13_6,10_6,12_4,13_6,13_2,4_3,5_7_8_9_14']
            ] 
'''

# #0.25_934
# net_stru = [['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14'],
#             ['0_10','0_13','0_2','0_4','0_6','0_7','1_3','1_5','10_12','10_13','10_4','10_5','10_6','12_13','12_6','13_2','13_3','13_4','13_5','13_6','13_7','2_4','3_5','4_6','4_7','5_6','5_7','6_7'],
#             ['0,2_0,4_2,4','0,13_0,4_4,13','10,13_6,10_6,13','1,3_1,5_3,5'],
#             ['0,4,13_0,2,4_1,3,5_6,10,13_0,10_0,6_0,7_10,12_4,10_5,10_12,13_6,12_2,13_3,13_5,13_7,13_4,6_4,7_5,6_5,7_6,7_8_9_14']
#             ]

# #Epinions 0.20
# net_stru = [['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14'],
#             ['0_10','0_13','0_2','0_4','0_6','0_7','0_8','1_13','1_3','1_5','10_12','10_13','10_3','10_4','10_5','10_6','12_13','12_3','12_4','12_5','12_6','13_2','13_3','13_4','13_5','13_6','13_7','13_8','13_9','2_4','2_6','2_7','3_5','3_6','3_7','4_6','4_7','5_6','5_7','6_7'],
#             ['0,13_10,13_0,13','0,10_4,10_0,4','0,4_0,10_4,10','0,6_0,10_6,10','0,2_2,13_0,13','0,4_4,13_0,13','0,6_6,13_0,13','0,7_7,13_0,13','0,2_0,4_2,4','0,4_0,6_4,6','0,4_0,7_4,7','1,3_1,5_3,5','6,10_6,12_10,12','4,10_4,13_10,13','5,10_5,13_10,13','6,10_6,13_10,13','3,5_3,10_5,10','4,6_4,10_6,10','5,6_5,10_6,10','6,12_6,13_12,13','2,4_2,13_4,13','3,5_3,13_5,13','4,6_4,13_6,13','4,7_4,13_7,13','5,13_6,13_5,6','6,7_6,13_7,13','2,4_2,7_4,7','3,5_3,6_5,6','3,5_3,7_5,7'],
#             ['0,2,4_0,2,13_0,4,13_2,4,13','0,4,6_0,4,13_0,6,13_4,6,13'],
#             ['0,2,4,13_0,4,6,13_3,5,7_3,5,6_2,4,7_6,7,13_5,6,13_5,6,13_4,7,13_3,5,13_6,12,13_5,6,10_4,6,10_3,5,10_6,10,13_5,10,13_4,10,13_6,10,12_1,3,5_0,4,7_0,7,13_0,6,10_0,4,10_0,10,13_3,6_2,6_9,13_8,13_6,12_5,12_4,12_3,12_12,13_1,13_0,8_0,12_14']
#             ]
'''
net_stru = [['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14'],
            ['0_1','2_3','4_5','6_7','8_9','12_14'],
            ['0,1_2,3_4,5','12,14_13'],
            ['0,1,2,3,4,5_6,7_10','8,9_12,13,14'],
            ['0,1,2,3,4,5,6,7,10_8,9,12,13,14']]

'''
'''
#934节点减少
net_stru = [['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14'],
            ['0_4','0_9','1_10','1_5','3_10','5_10','2_4','2_7','2_9','3_5','4_7','4_9','7_9'],
            ['0,4_4,9_0,9','1,5_5,10_1,10','3,5_3,10_5,10','2,4_2,7_4,7','2,4_4,9_2,9','2,7_2,9_7,9','4,7_4,9_7,9'],
            ['2,4,7_2,4,9_2,7,9_4,7,9'],
            ['2,4,7,9_3,5,10_1,5,10_0,4,9_6_8_12_13_14']
            ]
'''
'''
#DBLP
net_stru = [['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14'],
            ['4_10','5_10','9_10','2_7','2_9','4_5','4_9','5_9','7_9'],
            ['4,5_4,10_5,10','4,9_4,10_9,10','5,9_5,10_9,10','2,7_2,9_7,9','4,5_4,9_5,9'],
            ['4,5,9_4,5,10_4,9,10_5,9,10'],
            ['4,5,9,10_2,7,9_0_1_3_6_12_13_14']
            ]
'''
'''
#Alpha
net_stru = [['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14'],
            ['0_10','0_2','0_4','0_9','1_10','1_5','4_10','5_10','7_10','8_10','9_10','6_12','2_4','2_9','3_5','4_9'],
            ['0,9_0,10_9,10','0,2_0,9_2,9','0,4_0,9_4,9','1,5_1,10_5,10','2,4_2,9_4,9'],
            ['0,9,10_0,2,9_0,4,9_1,5,10_2,4,9_4,10_7,10_8,10_6,12_3,5_13_14']
            ]
'''
'''
#tang_en
net_stru = [['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14'],
            ['0_4','0_9','1_10','1_12','1_5','3_10','5_10','4_12','5_12','6_12','7_12','3_5','6_7','4_9'],
            ['1,5_1,10_5,10','0,4_0,9_4,9','3,5_3,10_5,10','6,7_6,12_7,12'],
            ['1,5,10_0,4,9_6,7,12_3,5,10_1,12_4,12_5,12_2_8_13_14']
            ]
'''

'''
#S_before
net_stru = [['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14'],
            ['1_5','1_9','9_10','2_7','2_9','3_9','5_9','7_9'],
            ['2,7_2,9_7,9'],
            ['2,7,9_1,5_1,9_9,10_3,9_5,9_0_3_4_8_12_13_14']
            ]
'''
'''
#概念数934
net_stru = [['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14'],
            ['0_1','2_3','4_5','6_7','11_13','12_14','9_10'],
            ['0,1_2,3_4,5','11,13_12,14'],
            ['0,1,2,3,4,5_8_6,7','11,12,13,14_9,10'],
            ['0,1,2,3,4,5,6,7,8_9,10,11,12,13,14']
            ]
'''

# #OTC 0.315
# net_stru = [['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14'],
#             ['0_4','0_9','2_4','2_9','4_9'],
#             ['0,4_0,9_4,9','2,4_2,9_4,9'],
#             ['0,4,9_2,4,9_1_3_5_6_7_8_10_11_13_14']
#             ]


def standard_name(name):
    '''0,1_2,3_4  -->  0,1,2,3,4'''
    result = ''
    re_l = []
    temp = name.split('_')
    for t in temp:
        t_temp = t.split(',')
        for tt in t_temp:
            re_l.append(tt)
    re_l = sorted(re_l)
    for r in re_l:
        result += ',' + r
    
    return result[1:]

def cal_value(before,model,wc = way_con):
    '''查找上一层节点并返回value'''
    cal_va = ''
    temp_b = before.split('_')
    for tb in temp_b:
        t = tb.split(',')
        t = sorted(t)
        t_str = ''
        for tt in t:
            t_str += ','+tt
        t_str = t_str[1:]            
        
        for m in model:
            if t_str == m.name:
                cal_va += concate[wc] + m.formula
                
    cal_va = cal_va[1:]
    return cal_va

def str2list(strr):
    '''多项式字符串转列表'''
    result = []
    temp_st = strr.split('+')
    for tst in temp_st:
        t_re = []
        t_temp_st = tst.split('*')
        for t in t_temp_st:
            t_re.append(t)
        t_re = sorted(t_re)    
        result.append(t_re)
    return result

def mini_2(fomula):
    result = []
    fo = fomula.split('+')
    for i in range(len(fo)):
        for j in range(i,len(fo)):
            temp = fo[i] + '*' + fo[j]
            te = temp.split('*')
            te_re = []
            te_nu = 1
            for t in te:
                if t[:2] not in W:
                    te_nu *= float(t)
                else:
                    te_re.append(t)
            te_re.append(str(te_nu))
            te_re = sorted(te_re)
            te_re_fi = ''
            for tr in te_re:
                te_re_fi += '*' + tr
            
            result.append(te_re_fi[1:])
    result_re = ''        
    for r in result:
        result_re += '+' + r
    
    return result_re[1:]        

def merge_similar(ori_d,new_d):
    '''合并同类项'''
    result = ''
    or_list = ori_d.split('+')
    temp_or = new_d.split('+')
    for i in range(len(or_list)):
        ol = or_list[i].split('*')
        ol[0] = str(float(ol[0])+float(temp_or[i].split('*')[0]))
        t_result = ''
        for o in ol:
            t_result += '*' + o        
        result += '+'+ t_result[1:]  
    return result[1:]
    


class fun_neu:
    def __init__(self,value,weight,before,name):
        self.value = value        
        self.weight = weight
        #self.formula = '(' + self.value + ')' + '*' + self.weight
        self.before = before
        self.name = name
        self.isUse = False
        self.del_brackets()
        self.del_same_name()
    def show_data(self):
        print(self.value, self.weight, self.formula, self.before, self.name, self.isUse)
    def del_brackets(self):
        self.formula = ''
        temp_value = self.value.split('+')
        for tv in temp_value:
            self.formula += '+' + tv + '*' + self.weight
        self.formula = self.formula[1:]
    def del_same_name(self):
        temp = self.name.split(',')
        temp = list(set(temp))
        temp = sorted(temp)
        self.name = ''
        for t in temp:
            self.name += t + ','
        self.name = self.name[:-1]

def read_data(path):
    result = []
    with open(path,"r") as csvfile:        
        reader = csv.reader(csvfile)
        for line in reader:
            if len(line) > 0:
                result.append(list(map(float,line)))
    #result = np.array(result)
    return result

def write_csv(path,data):
    with open(path,'w',newline='') as csvfile:
        writer = csv.writer(csvfile)
        for i in range(len(data)):
            writer.writerow(data[i])
        
def deal_data(data,num):
    data = sorted(data,key=lambda s: s[2], reverse=True)
    data = np.array(data)
    
    index = 0
    for i in range(len(data)):
        if data[i][2] == 0:
            index = i
            break
    po_data = data[:index]
    random.shuffle(po_data)
    ne_data = data[index:]
    random.shuffle(ne_data)    
    
    po_ne = len(po_data) / len(ne_data)
    #po_data = po_data[:int(len(po_data)/5.0)]
    #print(len(po_data),len(ne_data))    
    
    test_d1 = po_data[int(len(po_data)/10)*num:int(len(po_data)/10)*(num+1),:]
    test_d2 = ne_data[int(len(ne_data)/10)*num:int(len(ne_data)/10)*(num+1),:]
    test_l1 = po_data[int(len(po_data)/10)*num:int(len(po_data)/10)*(num+1),:3]
    test_l2 = ne_data[int(len(ne_data)/10)*num:int(len(ne_data)/10)*(num+1),:3]    
    test_data = np.concatenate((test_d1,test_d2), axis=0)
    test_label = np.concatenate((test_l1,test_l2), axis=0)
    
    train_d1 = np.concatenate((po_data[:int(len(po_data)/10)*num,:],po_data[int(len(po_data)/10)*(num+1):,:]), axis=0)
    train_d2 = np.concatenate((ne_data[:int(len(ne_data)/10)*num,:],ne_data[int(len(ne_data)/10)*(num+1):,:]), axis=0)
    train_l1 = np.concatenate((po_data[:int(len(po_data)/10)*num,:3],po_data[int(len(po_data)/10)*(num+1):,:3]), axis=0)
    train_l2 = np.concatenate((ne_data[:int(len(ne_data)/10)*num,:3],ne_data[int(len(ne_data)/10)*(num+1):,:3]), axis=0)
    
    
    train_data = np.concatenate((train_d1,train_d2), axis=0)
    train_label = np.concatenate((train_l1,train_l2), axis=0)
    
    write_csv('./result//test_temp//test_temp_d_'+str(num)+'.csv',test_data)
    write_csv('./result//test_temp//test_temp_l_'+str(num)+'.csv',test_label)
    
    write_csv('./result//test_temp//train_temp_d_'+str(num)+'.csv',train_data)
    write_csv('./result//test_temp//train_temp_l_'+str(num)+'.csv',train_label)

    return train_data,train_label,test_data,test_label,po_ne

def deal_tang(data):
    def read_tang_data(path):
        result = []
        with open(path,"r") as file:        
            lines = file.readlines()
            for line in lines:
                line = line.split()
                result.append(line)
        #result = np.array(result)
        return result
    
    train_data = []
    train_label = []
    test_data = []
    test_label = []
    data_nol = read_tang_data('./data//tang//epinion.dat')
    for i in range(data.shape[0]):
        if data_nol[i][0][:1] == '?':
            test_data.append(data[i])
            test_label.append(data[i][:3])
        else:
            train_data.append(data[i])
            train_label.append(data[i][:3])
    
    train_data = np.array(train_data)
    train_label = np.array(train_label)
    test_data = np.array(test_data)
    test_label = np.array(test_label)
    
    write_csv('./result//test_temp//test_temp_d_'+str(0)+'.csv',test_data)
    write_csv('./result//test_temp//test_temp_l_'+str(0)+'.csv',test_label)
    
    write_csv('./result//test_temp//train_temp_d_'+str(0)+'.csv',train_data)
    write_csv('./result//test_temp//train_temp_l_'+str(0)+'.csv',train_label)
    return train_data,train_label,test_data,test_label

# data_all = read_data('./data//before//Epinions//Epinions_15_2.csv')
#data_all = read_data('./data//before//Epinions//r_Epinions_15_in.csv')
data_all = read_data('./data//before//Alpha//Alpha_15_2.csv')
# data_all = read_data('./data//before//DBLP//DBLP_15_2.csv')
# data_all = read_data('./data//before//Slashdot//Slashdot_15_2.csv')
#data_all = read_data('./data//before//Wikivote_reduce//Wikivote_reduce_15_2.csv')
# data_all = read_data('./data//before//OTC//OTC_15_2.csv')

#data_all = [[7,244,1,0.794981245,0.070150499,0.130821941,0.154867734,0.305721814,0.068457245,0.583827623,0.050744551,0,0,0,0,0,0,0,0],
#            [7,542,0,0.794981245,0.250037185,0.130821941,0.16107282,0.305721814,0.223244848,0.46714739,0.168432272,0,0,0,0,0,0,0,0]]

data_all = np.array(data_all)

group_num = 1
for g in range(group_num):

    train_data,train_label,test_data,test_lable,po_ne = deal_data(data_all,g)
    #train_data,train_label,test_data,test_lable = deal_tang(data_all)
    
    print('number:',g,train_data.shape,train_label.shape,test_data.shape,test_lable.shape)

           
    #train_data = [['a','b','1',1,2,3,4,5,6,7,8,9,10,11,0,13,14,15]]
    #train_data = [['a','b','1',1,1,1,1,1,1,1,1,1,1,1,0,1,1,1]]     
    
    loss_formula = ''
    num = 0
    for da in train_data:     
        model = []
        for i in range(len(net_stru)):
            for j in range(len(net_stru[i])):
                if i==0:
                    t_value = str(da[3+i+j])
                    #t_weight = str(1)
                    t_weight = W[i]+str(j+1)
                    t_before = ''
                    t_name = net_stru[i][j]
                elif i == len(net_stru)-1:
                    t_weight = str(1)
                    #t_weight = W[i]+str(j+1)
                    t_before = net_stru[i][j]
                    t_value = cal_value(t_before,model,1)
                    t_name = standard_name(net_stru[i][j])
                else:
                    t_weight = str(1)
                    #t_weight = W[i]+str(j+1)
                    t_before = net_stru[i][j]                    
                    t_value = cal_value(t_before,model)
                    t_name = standard_name(net_stru[i][j])

                new_fun_neu = fun_neu(t_value,t_weight,t_before,t_name)
                #new_fun_neu.show_data()
                model.append(new_fun_neu)    
           
        t_formula = model[-1].value
        if float(da[2]) != 0:
            t_formula += '+-5'# + str(int(po_ne))
            #print(t_formula)
            #sys.exit()
        else:
            t_formula += '+1'
            
        #print(len(t_formula.split('+')))
        #print()
        t_formula = mini_2(t_formula)
        #print(len(t_formula.split('+')))
        
        if len(loss_formula) == 0:
            loss_formula = t_formula
        else:
            loss_formula = merge_similar(loss_formula,t_formula)
        print(g,num,'finished')
        num += 1
        
    #print(loss_formula)
    #print(loss_formula.split('+'))
    '''
    miu = []
    with open('./data//Epinions//r_Epinions_15_01.csv',"r") as csvfile:        
        reader = csv.reader(csvfile)
        for rd in reader:
            if len(rd)>0:
                miu = list(map(float,rd))
                break
    '''
    count_z = 1
    la = '+'
    for i in range(1):
        for j in range(len(net_stru[i])):
            if j == 11 or j == 6:
                continue
            else:
                la += W[i] + str(j+1) + '*' + W[i] + str(j+1) + '*' + 'Z' + '-Z+'           
                count_z += 1
    loss_formula += la[:-1]
    
    #print(loss_formula)
    
    with open('./result//loss//loss_'+str(g)+'.txt','w') as f:     #设置文件对象
        f.write(loss_formula)
    
    
















