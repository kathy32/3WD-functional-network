# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 16:10:15 2019

@author: Administrator
"""

import numpy as np
from sklearn.metrics import roc_curve
from sklearn.metrics import auc

def read_dat(path):
    result = []
    with open(path,"r") as file:        
        reader = file.readlines()
        for line in reader:
            if len(line) > 0:
                result.append(line)
    return result

def auc_calculate(labels,preds,n_bins=100):
    postive_len = sum(labels)
    negative_len = len(labels) - postive_len
    total_case = postive_len * negative_len
    pos_histogram = [0 for _ in range(n_bins)]
    neg_histogram = [0 for _ in range(n_bins)]
    bin_width = 1.0 / n_bins
    for i in range(len(labels)):
        nth_bin = int(preds[i]/bin_width)
        if labels[i]==1:
            pos_histogram[nth_bin] += 1
        else:
            neg_histogram[nth_bin] += 1
    accumulated_neg = 0
    satisfied_pair = 0
    for i in range(n_bins):
        satisfied_pair += (pos_histogram[i]*accumulated_neg + pos_histogram[i]*neg_histogram[i]*0.5)
        accumulated_neg += neg_histogram[i]

    return satisfied_pair / float(total_case)

'''
if __name__ == '__main__':

    y = data = read_data('./data//Epinions//Epinions.csv')
    pred = np.array([0.9, 0.8, 0.3, 0.1,0.4,0.9,0.66,0.7])


    fpr, tpr, thresholds = roc_curve(y, pred, pos_label=1)
    print("-----sklearn:",auc(fpr, tpr))
    print("-----py脚本:",auc_calculate(y,pred))
    '''