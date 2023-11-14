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

W = ['A_', 'B_', 'C_', 'D_', 'E_', 'F_', 'G_', 'H_']

concate = ['*', '+']

#DBLP 0.33
net_stru = [['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14'],
            ['1_8','8_10','8_12','8_13','8_14','2_7','2_8','2_9','4_5','4_8','4_9','5_9','7_8','7_9','8_9'],
            ['2,7_2,8_7.8','2,7_2,9_7.9','4,5_4,8_5,8','4,5_4,9_5,9'],
            ['2,7,8_2,7,9_4,5,8_4,5,9_8,9_8,14_8,13_8,12_8,10_1,8_0_3_6_12']
            ]


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


def cal_value(before, model, wc=way_con):
    '''查找上一层节点并返回value'''
    cal_va = ''
    temp_b = before.split('_')
    for tb in temp_b:
        t = tb.split(',')
        t = sorted(t)
        t_str = ''
        for tt in t:
            t_str += ',' + tt
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
        for j in range(i, len(fo)):
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


def merge_similar(ori_d, new_d):
    '''合并同类项'''
    result = ''
    or_list = ori_d.split('+')
    temp_or = new_d.split('+')
    for i in range(len(or_list)):
        ol = or_list[i].split('*')
        ol[0] = str(float(ol[0]) + float(temp_or[i].split('*')[0]))
        t_result = ''
        for o in ol:
            t_result += '*' + o
        result += '+' + t_result[1:]
    return result[1:]


class fun_neu:
    def __init__(self, value, weight, before, name):
        self.value = value
        self.weight = weight
        # self.formula = '(' + self.value + ')' + '*' + self.weight
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
    with open(path, "r") as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            if len(line) > 0:
                result.append(list(map(float, line)))
    # result = np.array(result)
    return result


def write_csv(path, data):
    with open(path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for i in range(len(data)):
            writer.writerow(data[i])


def deal_data(data, num):
    data = sorted(data, key=lambda s: s[2], reverse=True)
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
    # po_data = po_data[:int(len(po_data)/5.0)]
    # print(len(po_data),len(ne_data))

    test_d1 = po_data[int(len(po_data) / 10) * num:int(len(po_data) / 10) * (num + 1), :]
    test_d2 = ne_data[int(len(ne_data) / 10) * num:int(len(ne_data) / 10) * (num + 1), :]
    test_l1 = po_data[int(len(po_data) / 10) * num:int(len(po_data) / 10) * (num + 1), :3]
    test_l2 = ne_data[int(len(ne_data) / 10) * num:int(len(ne_data) / 10) * (num + 1), :3]
    test_data = np.concatenate((test_d1, test_d2), axis=0)
    test_label = np.concatenate((test_l1, test_l2), axis=0)

    train_d1 = np.concatenate(
        (po_data[:int(len(po_data) / 10) * num, :], po_data[int(len(po_data) / 10) * (num + 1):, :]), axis=0)
    train_d2 = np.concatenate(
        (ne_data[:int(len(ne_data) / 10) * num, :], ne_data[int(len(ne_data) / 10) * (num + 1):, :]), axis=0)
    train_l1 = np.concatenate(
        (po_data[:int(len(po_data) / 10) * num, :3], po_data[int(len(po_data) / 10) * (num + 1):, :3]), axis=0)
    train_l2 = np.concatenate(
        (ne_data[:int(len(ne_data) / 10) * num, :3], ne_data[int(len(ne_data) / 10) * (num + 1):, :3]), axis=0)

    train_data = np.concatenate((train_d1, train_d2), axis=0)
    train_label = np.concatenate((train_l1, train_l2), axis=0)

    write_csv('./result//test_temp//test_temp_d_' + str(num) + '.csv', test_data)
    write_csv('./result//test_temp//test_temp_l_' + str(num) + '.csv', test_label)

    write_csv('./result//test_temp//train_temp_d_' + str(num) + '.csv', train_data)
    write_csv('./result//test_temp//train_temp_l_' + str(num) + '.csv', train_label)

    return train_data, train_label, test_data, test_label, po_ne



opt_num = 9

train_data = read_data('./result//test_temp//train_temp_opt_d_'+str(opt_num)+'.csv')
train_label = read_data('./result//test_temp//train_temp_opt_l_'+str(opt_num)+'.csv')
train_data = np.array(train_data)
train_label = np.array(train_label)


loss_formula = ''
num = 0
for da in train_data:
    model = []
    for i in range(len(net_stru)):
        for j in range(len(net_stru[i])):
            if i == 0:
                t_value = str(da[3 + i + j])
                # t_weight = str(1)
                t_weight = W[i] + str(j + 1)
                t_before = ''
                t_name = net_stru[i][j]
            elif i == len(net_stru) - 1:
                t_weight = str(1)
                # t_weight = W[i]+str(j+1)
                t_before = net_stru[i][j]
                t_value = cal_value(t_before, model, 1)
                t_name = standard_name(net_stru[i][j])
            else:
                t_weight = str(1)
                # t_weight = W[i]+str(j+1)
                t_before = net_stru[i][j]
                t_value = cal_value(t_before, model)
                t_name = standard_name(net_stru[i][j])

            new_fun_neu = fun_neu(t_value, t_weight, t_before, t_name)
            # new_fun_neu.show_data()
            model.append(new_fun_neu)

    t_formula = model[-1].value
    if float(da[2]) != 0:
        t_formula += '+-1'  # + str(int(po_ne))
        # print(t_formula)
        # sys.exit()
    else:
        t_formula += '+1'

    # print(len(t_formula.split('+')))
    # print()
    t_formula = mini_2(t_formula)
    # print(len(t_formula.split('+')))

    if len(loss_formula) == 0:
        loss_formula = t_formula
    else:
        loss_formula = merge_similar(loss_formula, t_formula)
    num += 1

# print(loss_formula)
# print(loss_formula.split('+'))
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
            la += W[i] + str(j + 1) + '*' + W[i] + str(j + 1) + '*' + 'Z' + '-Z+'
            count_z += 1
loss_formula += la[:-1]

# print(loss_formula)

with open('./result//loss//loss_opt_' + str(opt_num) + '.txt', 'w') as f:  # 设置文件对象
    f.write(loss_formula)


















