import numpy as np


#Wikivote 0.315
net_stru = [['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14'],
            ['3_12','6_12','6_13','3_6'],
            ['3,12_6,12_6,13_3,6_0_1_2_4_5_7_8_9_10_14']
            ]
W = []
for i in range(len(net_stru[0])):
    W.append('A_' + str(int(net_stru[0][i]) + 1))

result = ''
for i in range(len(net_stru[1])):
    temp_str = net_stru[1][i].split('_')
    for j in range(i + 1, len(net_stru[1])):
        is_begin = True
        # for ts in temp_str:
        #     if ts in net_stru[1][j]:
        #         is_begin = False
        #         break
        if is_begin:
            temp_w = []
            for ts in temp_str:
                temp_w.append(W[int(ts)])
            temp_str_n = net_stru[1][j].split('_')
            for tsn in temp_str_n:
                temp_w.append(W[int(tsn)])
            for ti in range(len(temp_w)):
                for tj in range(ti+1,len(temp_w)):
                    result += 'exp(2*' + temp_w[ti] + '*' + temp_w[tj] + '+' + temp_w[ti] + '*' + temp_w[ti] + '+' + temp_w[tj] + '*' + temp_w[ti] + ')+'
                # if i == len(temp_w) - 1:
                #     result += '3*' + temp_w[i] + '*' + temp_w[i] + '+'
                # else:
                #     result += '3*' + temp_w[i] + '*' + temp_w[i] + '+' + '2*' + temp_w[i] + '*' + temp_w[i + 1] + '+'
        else:
            continue
result = result[:-1]
print(result)
