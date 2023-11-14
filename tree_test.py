# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 22:48:11 2019

@author: Administrator
"""

import csv
import numpy as np
import operator

way_con = 0

W = ['A_', 'B_', 'C_', 'D_', 'E_', 'F_', 'G_', 'H_']

concate = ['*', '+']


def read_data(path):
    result = []
    with open(path, "r") as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            if len(line) > 0:
                result.append(list(map(float, line)))
    # result = np.array(result)
    return result


class fun_neu:
    def __init__(self, value, weight, before, name):
        self.value = value
        self.weight = weight
        # self.formula = '(' + self.value + ')' + '*' + self.weight
        self.before = before
        self.name = name
        self.isUse = False
        self.del_brackets()

    def show_data(self):
        print(self.value, self.weight, self.formula, self.before, self.name, self.isUse)

    def del_brackets(self):
        self.formula = ''
        temp_value = self.value.split('+')
        for tv in temp_value:
            self.formula += '+' + tv + '*' + self.weight
        self.formula = self.formula[1:]


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

def write_csv(path,data):
    with open(path,'w',newline='') as csvfile:
        writer = csv.writer(csvfile)
        for i in range(len(data)):
            writer.writerow(data[i])

way_con = 0

W = ['A_', 'B_', 'C_', 'D_', 'E_', 'F_', 'G_', 'H_']

concate = ['*', '+']


#DBLP 0.37
net_stru = [['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14'],
            ['8_12','8_13','8_14','2_7','4_5'],
            ['8,12_8,13_8,14_2,7_4,5_0_1_2_3_6_9_10_14']
            ]


# #DBLP 0.33
# net_stru = [['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14'],
#             ['1_8','8_10','8_12','8_13','8_14','2_7','2_8','2_9','4_5','4_8','4_9','5_9','7_8','7_9','8_9'],
#             ['2,7_2,8_7.8','2,7_2,9_7.9','4,5_4,8_5,8','4,5_4,9_5,9'],
#             ['2,7,8_2,7,9_4,5,8_4,5,9_8,9_8,14_8,13_8,12_8,10_1,8_0_3_6_12']
#             ]


#DBLP 0.37
'''
W_ = [['A_1','A_2','A_3','A_4','A_5','A_6','A_7','A_8','A_9','A_10','A_11','A_13','A_14','A_15'],
      [-0.4098,0.1099,2.8044,0.5055,-0.9667,0.9667,-0.2391,-0.3593,1.1129,-0.3724,-0.2773,1.0132,-0.4464,-0.1437],
      [-0.3152,-0.5700,1.5299,-0.2835,-1.4590,1.4590,0.7862,-1.5044,-1.5847,-1.3114,-1.0521,-1.5875,-0.1400,-0.1144],
      [-0.4082,0.3787,-0.6157,2.9672,-0.8061,0.8061,-0.7455,0.0088,1.0348,0.1172,-0.1930,0.9013,-0.4927,-0.1705],
      [-0.0260,-0.1002,-2.7741,0.0877,-3.3433,0.0146,0.0925,-0.6282,1.0035,0.0142,-0.0237,0.5769,-0.2490,-0.0758],
      [0.5239,0.8737,-1.6778,-0.3471,-1.0932,-1.0932,0.4348,-0.9726,1.2801,-1.3582,-0.7526,1.2565,-0.2399,-0.0556],
      [0.7064,0.7841,1.3856,0.0481,-1.0939,1.0939,-0.0480,-0.8892,-1.1871,-1.5135,1.2882,-1.0841,0.4938,0.0294],
      [-0.2637,0.2674,-0.5989,2.9981,0.8075,-0.8075,-0.7531,0.0236,1.0324,0.1230,-0.2135,0.8996,-0.4900,-0.1737],
      [-0.0201,-0.0984,-0.0038,0.0817,0.2291,-0.2291,0.0889,-0.5220,3.54576,0.0184,-0.0235,0.1618,-0.0710,-0.0321],
      [0.0086,-0.1101,1.7053,0.0787,1.0410,1.0661,0.0837,-0.7229,1.7381,0.0216,-0.0201,1.9562,2.9351,-0.1271],
      [-1.0414,-1.7035,1.5933,0.1792,0.9423,-0.9423,-0.1726,-0.8042,-1.1925,1.0691,0.1781,-1.1476,0.3246,0.0051]
      ]
'''





print(len(W_[0]), len(W_[1]))
number_time = 0

test_data = read_data('./result//test_temp//DBLP//train_temp_d_' + str(number_time) + '.csv')
test_lable = read_data('./result//test_temp//DBLP//train_temp_l_' + str(number_time) + '.csv')

count = 0
num = 0
p_all = 0
tp = 0
fp = 0
fn = 0
tn = 0
b_count_r = 0
b_count_f = 0

train_opt = []
train_opt_l = []

for da in test_data:
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

    final_result = 0
    tf = t_formula.split('+')
    for t in tf:
        temp_t = t.split('*')
        temp_result = 1
        for tt in temp_t:
            if tt[:2] not in W:
                temp_result *= float(tt)
            else:
                # print(W_[0].index(tt),number_time+1)
                # print(W_[number_time+1][W_[0].index(tt)])
                temp_result *= float(W_[number_time + 1][W_[0].index(tt)])

        final_result += temp_result

    final_pre = -1
    if final_result < 0:
        final_pre = 0
    else:
        final_pre = 1

    if final_pre == float(test_data[num][2]):
        count += 1

    if final_pre == float(test_data[num][2]) and final_result >= -0.3 and final_result <= 0.3:
        b_count_r += 1
        train_opt.append(da)
        train_opt_l.append(test_lable[num])
        continue

    if final_pre != float(test_data[num][2]) and final_result >= -0.3 and final_result <= 0.3:
        b_count_f += 1
        train_opt.append(da)
        train_opt_l.append(test_lable[num])
        continue

    if float(test_data[num][2]) == 1 and final_pre == float(test_data[num][2]):
        tp += 1
    if float(test_data[num][2]) == 0 and final_pre == float(test_data[num][2]):
        tn += 1
    if float(test_data[num][2]) == 1 and final_pre != float(test_data[num][2]):
        fp += 1
    if float(test_data[num][2]) == 0 and final_pre != float(test_data[num][2]):
        fn += 1
    num += 1

write_csv('./result//test_temp//train_temp_opt_d_'+str(number_time)+'.csv',train_opt)
write_csv('./result//test_temp//train_temp_opt_l_'+str(number_time)+'.csv',train_opt_l)

accuracy = (tp + tn) / (tp + tn + fp + fn)
precision = (tp) / (tp + fp)
recall = (tp) / (tp + fn)
f1 = 2 * precision * recall / (precision + recall)

print('accuracy', accuracy * 100)
print('precision', precision * 100)
print('recall', recall * 100)
print('F1', f1 * 100)

print('boundary pre:', tp + tn + fp + fn, b_count_f, b_count_r, b_count_r / (b_count_r + b_count_f))
