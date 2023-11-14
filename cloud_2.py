# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 18:41:24 2019

@author: Administrator
"""

import csv
import numpy as np
import cloud


def read_data(path):
    result = []
    with open(path, "r") as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            result.append(line)
    # result = np.array(result)
    return result


def write_csv(path, data):
    with open(path, "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        for i in range(len(data)):
            writer.writerow(data[i])


def deal_data(o_data):
    data = []
    for d in o_data:
        temp = list(map(lambda x: float(x), d))
        data.append(temp)

    data = np.array(data)

    # 归一化
    temp = []
    for i in range(data.shape[1]):
        if i == data.shape[1] - 1:
            temp1 = data[:, i:]
        else:
            temp1 = data[:, i:i + 1]
        if np.max(temp1) == 0 or i == 0 or i == 1 or i == 2:
            pass
        else:
            temp1 = temp1 / np.max(temp1)
        temp.append(temp1)

    data = np.concatenate((temp[0], temp[1], temp[2], temp[3], temp[4], temp[5], temp[6], temp[7], temp[8], temp[9],
                           temp[10], temp[11], temp[12], temp[13], temp[14], temp[15], temp[16], temp[17]), axis=1)

    return data


if __name__ == '__main__':

    classes = 2
    target = 0.01
    Ex = []
    En = []
    He = []
    CD = []

    data = read_data('./data//before//OTC//OTC_all_15.csv')
    print(len(data[0]))
    # data = read_data('./data//before//Epinions//reduce_fu//Epinions_all_15.csv')
    # data = read_data('./data//before//DBLP//DBLP_all_15.csv')
    data = deal_data(data)

    for i in range(3, data.shape[1]):
        if i == data.shape[1] - 1:
            cloud_in = data[:, i:]
        else:
            cloud_in = data[:, i:i + 1]
        print(i)

        cloud_in = cloud_in * 1000
        cloud_in = cloud_in.astype(np.int32)
        cloud_in = cloud_in.reshape((data.shape[0]))
        cloud_re = cloud_in.reshape((1, data.shape[0]))

        if i == 14 or i == 16 or i == 17:
            for j in range(len(cloud_in)):
                if cloud_in[j] != 0:
                    data[j][i] = 1

        else:
            Ex_t, En_t, He_t, CD_t = cloud.t_cloud_tran(cloud_in, classes, target)
            # print(i,CD_t)

            for j in range(cloud_in.shape[0]):
                temp_, temp = cloud.t_calculate_certain(Ex_t, En_t, He_t, cloud_in[j])
                data[j][i] = temp_[1]

            Ex.append(Ex_t)
            En.append(En_t)
            He.append(He_t)
            CD.append(CD_t)
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            if data[i][j] < 0.01:
                data[i][j] = 0
    # print(len(data_save),len(data_save[0]))
    # write_csv('./data//before//Slashdot//Slashdot_15_01.csv',data)
    # write_csv('./data//before//Epinions//reduce_fu//Epinions_15_2.csv',data)
    # write_csv('./data//before//DBLP//DBLP_15_2.csv',data)
    # write_csv('./data//before//DBLP//DBLP_15_01.csv',data)
    # write_csv('./data//before//Alpha//Alpha_15_2.csv',data)
    write_csv('./data//before//OTC//OTC_15_2.csv', data)
    # write_csv('./data//before//OTC//OTC_15_01.csv', data)
