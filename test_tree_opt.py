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


#DBLP 0.33
net_stru1 = [['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14'],
            ['1_8','8_10','8_12','8_13','8_14','2_7','2_8','2_9','4_5','4_8','4_9','5_9','7_8','7_9','8_9'],
            ['2,7_2,8_7.8','2,7_2,9_7.9','4,5_4,8_5,8','4,5_4,9_5,9'],
            ['2,7,8_2,7,9_4,5,8_4,5,9_8,9_8,14_8,13_8,12_8,10_1,8_0_3_6_12']
            ]

#DBLP 0.37
W_ = [['A_1','A_2','A_3','A_4','A_5','A_6','A_7','A_8','A_9','A_10','A_11','A_12','A_13','A_14','A_15'],
      [-0.4098,0.1099,2.8044,0.5055,-0.9667,0.9667,-0.2391,-0.3593,1.1129,-0.3724,-0.2773,0,1.0132,-0.4464,-0.1437],
      [-0.3152,-0.5700,1.5299,-0.2835,-1.4590,1.4590,0.7862,-1.5044,-1.5847,-1.3114,-1.0521,0,-1.5875,-0.1400,-0.1144],
      [-0.4082,0.3787,-0.6157,2.9672,-0.8061,0.8061,-0.7455,0.0088,1.0348,0.1172,-0.1930,0,0.9013,-0.4927,-0.1705],
      [-0.0260,-0.1002,-2.7741,0.0877,-3.3433,0.0146,0.0925,-0.6282,1.0035,0.0142,-0.0237,0,0.5769,-0.2490,-0.0758],
      [0.5239,0.8737,-1.6778,-0.3471,-1.0932,-1.0932,0.4348,-0.9726,1.2801,-1.3582,-0.7526,0,1.2565,-0.2399,-0.0556],
      [0.7064,0.7841,1.3856,0.0481,-1.0939,1.0939,-0.0480,-0.8892,-1.1871,-1.5135,1.2882,0,-1.0841,0.4938,0.0294],
      [-0.2637,0.2674,-0.5989,2.9981,0.8075,-0.8075,-0.7531,0.0236,1.0324,0.1230,-0.2135,0,0.8996,-0.4900,-0.1737],
      [-0.0201,-0.0984,-0.0038,0.0817,0.2291,-0.2291,0.0889,-0.5220,3.54576,0.0184,-0.0235,0,0.1618,-0.0710,-0.0321],
      [0.0086,-0.1101,1.7053,0.0787,1.0410,1.0661,0.0837,-0.7229,1.7381,0.0216,-0.0201,0,1.9562,2.9351,-0.1271],
      [-1.0414,-1.7035,1.5933,0.1792,0.9423,-0.9423,-0.1726,-0.8042,-1.1925,1.0691,0.1781,0,-1.1476,0.3246,0.0051]
      ]

'''
#0.1
W_1 = [['A_1','A_2','A_3','A_4','A_5','A_6','A_7','A_8','A_9','A_10','A_11','A_12','A_13','A_14','A_15'],
       [0.3508,-0.1301,0,3.0954,0.8499,0.9238,-2.0575,0,-0.1972,0.8709,-0.3127,0,0.6824,-0.4285,-0.3971],
       [1.3797,0.0037,0,-1.9127,1.5759,1.5744,0.3748,0,0.0252,1.5713,-0.0026,0,-0.0705,0.0182,0.0083],
       [2.5939,-0.2593,0,1.3491,0.8968,0.9800,-1.8944,0,-0.3045,0.9424,-0.4136,0,1.0203,-0.4819,-0.4401],
       [0.2017,-0.0067,0,3.1227,1.0055,1.0108,-1.0168,0,-0.0148,1.0182,-0.0101,0,0.3707,-0.0141,-0.0028],
       [0.1770,-0.7336,0,0.0959,0.8229,1.0233,-5.7261,0,-2.1758,-1.8816,-0.7565,0,-0.1630,-0.9066,-1.0005],
       [-0.2682,-0.0205,0,0.1124,-0.0018,-0.0012,0.1313,0,3.5925,0.0036,-0.0105,0,0.0745,-0.0440,-0.0265],
       [],
       [0.0732,2.0460,0,0.0582,7.2230,-3.8266,0.0725,0,-0.0196,-0.3219,2.4366,0,0.1830,1.4814,0.7316],
       [],
       [0.4259,1.2502,0,-0.0173,0.0967,0.0801,-0.0068,0,0.1008,-0.7748,-1.4904,0,0.4836,-2.4788,-1.4243]
      ]
'''
#0.15

W_1 = [['A_1','A_2','A_3','A_4','A_5','A_6','A_7','A_8','A_9','A_10','A_11','A_12','A_13','A_14','A_15'],
       [0.2043,-0.1324,0,3.1591,0.8365,0.9104,-2.0117,0,-0.1986,0.8606,-0.3087,0,0.4974,-0.4112,-0.3738],
       [],
       [1.2740,-0.0232,0,2.8209,0.8423,0.8921,-1.9182,0,-0.2054,0.8977,-0.2161,0,-0.9015,-0.3566,-0.2799],
       [0.2646,0.1892,0,0.2713,8.9603,2.6281,0.2884,0,1.5385,-2.0366,-0.7515,0,0.5903,0.0029,0.9231],
       [0.1140,2.1086,0,-0.0601,4.1558,-2.9268,0.9119,0,2.5190,-0.9555,-0.0848,0,-1.1218,-0.1084,0.0285],
       [-3.2793,-0.9046,0,-0.3913,9.2213,-2.0320,0.3260,0,-1.0221,-0.3182,-0.3226,0,-0.0278,-0.1439,0.0496],
       [0.2733,0.5954,0,-0.3013,-1.7626,0.5230,-0.2979,0,4.5177,-3.0936,1.0308,0,0.5200,-0.1971,1.1240],
       [2.7682,-0.4655,0,1.1362,0.8742,0.9982,-1.1710,0,-0.3450,0.9581,-0.5031,0,0.6757,-0.2898,-0.4866],
       [-0.0149,-0.0704,0,3.2834,0,0,0.2882,0,-0.9330,0.0067,0.0515,0,1.1555,0,-0.07],
       [0.3195,1.6139,0,-0.04899,-0.1425,0.1232,-0.0334,0,0.1095,-0.7089,-1.4105,0,0.5015,-2.4809,-1.1594]
      ]


#0.3
'''
W_1 = [['A_1','A_2','A_3','A_4','A_5','A_6','A_7','A_8','A_9','A_10','A_11','A_12','A_13','A_14','A_15'],
       [0.4207,-0.1460,0,3.1357,0.8307,0.9021,-1.9957,0,-0.1861,0.8524,-0.3008,0,0.5620,-0.4065,-0.3630],
       [-0.0531,-0.0827,0,-0.0168,1.3963,-1.2946,0.4757,0,2.5406,-0.2168,-0.1467,0,-0.5928,1.9308,-1.5449],
       [0.0980,0.0447,0,-0.1925,1.8687,-3.4175,-0.1911,0,1.0066,0.0322,-0.0494,0,0.4553,-0.2118,-0.0523],
       [],
       [-0.3357,1.0139,0,0.0200,-7.1324,0.8776,0.0295,0,-1.2796,-3.0640,1.2194,0,0.3732,-0.1186,0.2446],
       [3.0642,-0.3530,0,0.5817,0.8311,0.9485,-1.1358,0,-0.2168,0.9200,-0.3269,0,0.4757,-0.4455,-0.3628],
       [2.7165,-0.2984,0,1.2713,0.8859,0.9849,-1.8685,0,-0.2950,0.9599,-0.3992,0,0.7855,-0.4160,-0.4494],
       [-0.0947,0.0870,0,-0.0837,-4.9005,1.0454,-0.0748,0,1.0982,-3.0448,-0.8408,0,0.4466,1.3055,0.0336],
       [-0.3020,0.1668,0,-0.2603,0,0,0.6933,0,-0.0353,0.0404,-0.3119,0,3.5534,0,0.2927],
       [-1.1123,0.0233,0,2.7778,0.8387,0.8908,-1.3097,0,-0.2401,0.8946,-0.1968,0,-1.1442,-0.4846,-0.3279]
      ]
'''

#0.2
'''
W_1 = [['A_1','A_2','A_3','A_4','A_5','A_6','A_7','A_8','A_9','A_10','A_11','A_12','A_13','A_14','A_15'],
       [0.2123,-0.1325,0,3.1791,0.8291,0.8999,-2.0154,0,-0.1878,0.8509,-0.2919,0,0.4459,-0.4050,-0.3544],
       [-0.0515,-0.0950,0,-0.0179,5.0156,-1.3988,0.4480,0,2.5442,-0.1497,-0.1126,0,-0.4488,1.8641,-1.6743],
       [0.1667,0.0212,0,-0.2248,0.1120,-0.0792,-0.2211,0,3.5867,0.01337,-0.0107,0,0.1835,-0.0585,-0.0142],
       [],
       [0.0053,-0.0011,0,0.0025,-2.0844,-2.0810,-17.6993,0,-0.1049,2.0768,-0.0013,0,0.0039,-0.0010,-0.0011],
       [-0.2633,-0.0935,0,0.0969,-1.130,3.4376,0.1099,0,0.9892,0.0213,-0.0398,0,0.2314,-0.2101,-0.1295],
       [1.5649,-0.0259,0,1.9308,0.8361,0.8819,-1.4223,0,-0.3360,0.9750,-0.2082,0,-1.9886,-0.4272,-0.3181],
       [-0.0185,0.0786,0,0.0035,7.7841,-0.2262,0.0200,0,7.3051,3.5128,0.1788,0,0.2989,-0.6933,0.0040],
       [-0.0149,-0.0704,0,3.2834,0,0,0.2882,0,-0.9330,0.0067,0.0515,0,1.1555,0,-0.0700],
       [0.9618,-0.0976,0,2.9777,0.8251,0.8906,-2.1902,0,-0.1560,0.8370,-0.3018,0,0.7765,-0.4133,-0.3661]
      ]
'''

#0.25
'''
W_1 = [['A_1','A_2','A_3','A_4','A_5','A_6','A_7','A_8','A_9','A_10','A_11','A_12','A_13','A_14','A_15'],
       [0.2814,-0.1347,0,3.1742,0.8279,0.8983,-2.0072,0,-0.1863,0.8500,-0.2921,0,0.4535,-0.4014,-0.3528],
       [],
       [2.6568,-0.2631,0,1.4612,0.8895,0.9783,-1.9362,0,-0.2805,0.9556,-0.3616,0,0.7206,-0.4047,-0.4272],
       [],
       [0.6254,-0.2753,0,-2.4906,-0.9268,0.8728,1.4275,0,-0.5098,-0.9180,0.3256,0,-1.7860,0.0256,0.5562,],
       [3.0706,-0.3722,0,0.5250,0.8301,0.9526,-1.0841,0,-0.2264,0.9233,-0.3378,0,0.4564,-0.4450,-0.3687],
       [2.7677,-0.3009,0,1.2260,0.8872,0.9828,-1.8513,0,-0.2979,0.9605,-0.3839,0,0.6970,-0.3977,-0.4354],
       [1.9270,-0.2843,0,2.3976,0.8553,0.9568,-1.7661,0,-0.2603,0.9065,-0.4071,0,0.6265,-0.3917,-0.4564],
       [3.1128,-0.0124,0,0.7908,0,0,1.2352,0,-0.0003,-0.0027,-0.0003,0,1.6378,0,-0.0456],
       [0.0136,-0.1441,0,0.0170,-1.2083,1.0123,-0.3838,0,-2.2760,-1.1938,-0.2350,0,0.0351,1.7315,-0.9129]
      ]
'''



print(len(W_[0]), len(W_[1]))
number_time = 0

test_data = read_data('./result//test_temp//DBLP//test_temp_d_' + str(number_time) + '.csv')
test_lable = read_data('./result//test_temp//DBLP//test_temp_l_' + str(number_time) + '.csv')

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

    if final_pre == float(test_data[num][2]) and final_result >= -0.15 and final_result <= 0.15:
        b_count_r += 1
        train_opt.append(da)
        train_opt_l.append(test_lable[num])
        continue

    if final_pre != float(test_data[num][2]) and final_result >= -0.15 and final_result <= 0.15:
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

# write_csv('./result//test_temp//train_temp_opt_d_'+str(number_time)+'.csv',train_opt)
# write_csv('./result//test_temp//train_temp_opt_l_'+str(number_time)+'.csv',train_opt_l)

accuracy = (tp + tn) / (tp + tn + fp + fn)
precision = (tp) / (tp + fp)
recall = (tp) / (tp + fn)
f1 = 2 * precision * recall / (precision + recall)

count_low = tp + tn + fp + fn
tp_low = tp
tn_low = tn
fp_low = fp
fn_low = fn

print('accuracy', accuracy * 100)
print('precision', precision * 100)
print('recall', recall * 100)
print('F1', f1 * 100)

print('boundary pre:', tp + tn + fp + fn, b_count_f, b_count_r, b_count_r / (b_count_r + b_count_f))

count = 0
num = 0
p_all = 0
tp = 0
fp = 0
fn = 0
tn = 0
for da in train_opt:
    model = []
    for i in range(len(net_stru1)):
        for j in range(len(net_stru1[i])):
            if i == 0:
                t_value = str(da[3 + i + j])
                # t_weight = str(1)
                t_weight = W[i] + str(j + 1)
                t_before = ''
                t_name = net_stru1[i][j]
            elif i == len(net_stru1) - 1:
                t_weight = str(1)
                # t_weight = W[i]+str(j+1)
                t_before = net_stru1[i][j]
                t_value = cal_value(t_before, model, 1)
                t_name = standard_name(net_stru1[i][j])
            else:
                t_weight = str(1)
                # t_weight = W[i]+str(j+1)
                t_before = net_stru1[i][j]
                t_value = cal_value(t_before, model)
                t_name = standard_name(net_stru1[i][j])

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
                temp_result *= float(W_1[number_time + 1][W_1[0].index(tt)])

        final_result += temp_result

    final_pre = -1
    if final_result < 0:
        final_pre = 0
    else:
        final_pre = 1

    if final_pre == float(test_data[num][2]):
        count += 1

    if float(test_data[num][2]) == 1 and final_pre == float(test_data[num][2]):
        tp += 1
    if float(test_data[num][2]) == 0 and final_pre == float(test_data[num][2]):
        tn += 1
    if float(test_data[num][2]) == 1 and final_pre != float(test_data[num][2]):
        fp += 1
    if float(test_data[num][2]) == 0 and final_pre != float(test_data[num][2]):
        fn += 1
    num += 1

accuracy = (tp + tn) / (tp + tn + fp + fn)
precision = (tp) / (tp + fp)
recall = (tp) / (tp + fn)
f1 = 2 * precision * recall / (precision + recall)

print('accuracy', accuracy * 100)
print('precision', precision * 100)
print('recall', recall * 100)
print('F1', f1 * 100)

count_high = tp + tn + fp + fn
tp_high = tp
tn_high = tn
fp_high = fp
fn_high = fn
print()
print('final result:')

accuracy = (tp_low + tn_low + tp_high + tn_high) / (count_high + count_low)
precision = (tp_low + tp_high) / (tp_low + fp_low + tp_high + fp_high)
recall = (tp_low + tp_high) / (tp_low + fn_low + tp_high + fn_high)
f1 = 2 * precision * recall / (precision + recall)

print('accuracy', accuracy * 100)
print('precision', precision * 100)
print('recall', recall * 100)
print('F1', f1 * 100)