# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 21:21:53 2019

@author: gangqZhang
"""
import csv
from itertools import combinations, permutations

def read_data(path):
    result = []
    with open(path,"r") as csvfile:        
        reader = csv.reader(csvfile)
        for line in reader:
            result.append(line)
    #result = np.array(result)
    return result

def write_csv(path,data):
    with open(path,"w",newline='') as csvfile: 
        writer = csv.writer(csvfile)
        for i in range(len(data)):
            writer.writerow(data[i])


if __name__ == '__main__':
    
    #data = read_data('./data//before//Slashdot//Slashdot_15_multi.csv')
    data = read_data('./data//before//Wikivote//Wikivote_15_multi.csv')
    '''
    data = [[4.0,5.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0],
            [4.0,155.0,0.0,0.0,3.0,0.0,2.0,0.0,2.0,0.0,2.0,0.0,2.0,0.0,0.0,0.0,1.0,1.0],
            [4.0,1509.0,0.0,0.0,3.0,0.0,1.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
            [4.0,2282.0,1.0,0.0,2.0,0.0,2.0,0.0,2.0,0.0,1.0,0.0,2.0,0.0,0.0,0.0,1.0,0.0],
            [4.0,2984.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
            [5.0,8.0,0.0,0.0,0.0,2.0,0.0,0.0,0.0,0.0,0.0,0.0,2.0,0.0,0.0,0.0,2.0,1.0],
            [5.0,52.0,1.0,0.0,3.0,2.0,1.0,0.0,2.0,0.0,0.0,0.0,2.0,2.0,0.0,1.0,1.0,0.0],
            [5.0,155.0,1.0,0.0,3.0,2.0,2.0,0.0,2.0,0.0,0.0,0.0,2.0,2.0,0.0,1.0,2.0,0.0],
            [5.0,183.0,1.0,0.0,0.0,2.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,1.0,1.0,0.0],
            [5.0,197.0,1.0,0.0,2.0,2.0,0.0,0.0,1.0,1.0,0.0,0.0,1.0,2.0,0.0,1.0,2.0,0.0],
            [5.0,245.0,1.0,0.0,0.0,2.0,0.0,0.0,1.0,2.0,0.0,0.0,0.0,2.0,0.0,1.0,2.0,0.0],
            [5.0,302.0,1.0,0.0,0.0,2.0,0.0,0.0,0.0,2.0,0.0,0.0,0.0,0.0,0.0,2.0,1.0,0.0],
            [5.0,311.0,1.0,0.0,3.0,2.0,1.0,0.0,2.0,0.0,0.0,0.0,2.0,2.0,0.0,1.0,1.0,0.0],
            [5.0,317.0,1.0,0.0,3.0,2.0,1.0,0.0,2.0,0.0,0.0,0.0,0.0,2.0,0.0,1.0,2.0,0.0],
            [5.0,361.0,1.0,0.0,3.0,2.0,0.0,0.0,1.0,0.0,0.0,0.0,1.0,2.0,0.0,1.0,2.0,0.0],
            [5.0,410.0,0.0,0.0,3.0,2.0,2.0,0.0,1.0,0.0,0.0,0.0,0.0,2.0,0.0,0.0,2.0,1.0],
            [5.0,450.0,1.0,0.0,0.0,2.0,2.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,1.0,1.0,0.0],
            [5.0,453.0,1.0,0.0,3.0,2.0,2.0,0.0,2.0,0.0,0.0,0.0,2.0,0.0,0.0,1.0,2.0,0.0],
            [5.0,655.0,1.0,0.0,0.0,2.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,2.0,0.0,1.0,2.0,0.0],
            [5.0,671.0,1.0,0.0,3.0,2.0,2.0,0.0,2.0,0.0,0.0,0.0,0.0,2.0,0.0,1.0,2.0,0.0],
            [5.0,691.0,1.0,0.0,3.0,2.0,2.0,0.0,2.0,0.0,0.0,0.0,0.0,2.0,0.0,1.0,2.0,0.0],
            [5.0,727.0,1.0,0.0,3.0,2.0,1.0,0.0,1.0,2.0,0.0,0.0,0.0,1.0,0.0,2.0,2.0,0.0],
            [5.0,731.0,1.0,0.0,0.0,2.0,0.0,0.0,1.0,2.0,0.0,0.0,0.0,2.0,0.0,1.0,2.0,0.0],
            [5.0,851.0,1.0,0.0,0.0,2.0,2.0,0.0,0.0,0.0,0.0,0.0,0.0,2.0,0.0,1.0,1.0,0.0],
            [5.0,904.0,1.0,0.0,3.0,2.0,2.0,0.0,2.0,0.0,0.0,0.0,2.0,2.0,0.0,1.0,2.0,0.0],
            [5.0,913.0,1.0,0.0,3.0,2.0,1.0,0.0,2.0,0.0,0.0,0.0,1.0,2.0,0.0,1.0,1.0,0.0],
            [5.0,966.0,1.0,0.0,3.0,2.0,0.0,0.0,0.0,0.0,0.0,0.0,2.0,0.0,0.0,1.0,2.0,0.0],
            [5.0,974.0,1.0,0.0,0.0,2.0,1.0,0.0,1.0,2.0,0.0,0.0,0.0,2.0,0.0,1.0,2.0,0.0],
            [5.0,999.0,1.0,0.0,0.0,2.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,2.0,1.0,0.0],
            [5.0,1005.0,0.0,0.0,0.0,2.0,0.0,0.0,0.0,2.0,0.0,0.0,2.0,0.0,0.0,0.0,2.0,1.0]]
    '''
    r_1 = []
    r_0 = []
    r_1_c = []
    r_0_c = []
    
    lr_1 = []
    lr_0 = []
    num_char = [var for var in range(3,18)]

    for i in range(len(data)):
        temp = data[i][3:]
        if float(data[i][2]) == 1:
            r_1.append(i)
            lr_1.append(temp)
        else:
            r_0.append(i)
            lr_0.append(temp)
            
    uncertain = [v for v in lr_0 if v in lr_1]
    print('uncertain:',len(uncertain))
    for i in range(len(r_1)):
        if lr_1[i] not in uncertain:
            r_1_c.append(r_1[i])
    for i in range(len(r_0)):
        if lr_0[i] not in uncertain:
            r_0_c.append(r_0[i])
    pos_r = r_1_c + r_0_c
    
    
    rough_result = [] 
    all_rough = []
    isend = False
    for i in range(len(num_char)):
        ind = []
        ind_index = []
        num_list = list(combinations(num_char, len(num_char)-i))
        #print(len(num_list))
        ind_index += num_list
        #print(num_list)
        for nl in (num_list):
            #print(nl)
            index = []
            temp_ind = []
            for p in pos_r:
                temp = []
                for t in range(len(nl)):
                    temp.append(data[p][nl[t]])
                if temp not in index:
                    temp_ind.append([p])
                    index.append(temp)
                else:
                    temp_ind[index.index(temp)].append(p)        
            ind.append(temp_ind)   
        if i==0:
            all_rough = ind
        else:
            isend = True
            for j in range(len(ind)):
                if ind[j]==all_rough[0]:
                    isend = False
                    print(j,ind_index[j]) 
                    rough_result.append(ind_index[j]) 
            
        print(len(num_char)-i,'finished')
        
        if isend:
            break
    '''
    rough_result = []    
    for i in range(len(ind)):
        if ind[i]==ind[-1]:
            print(i,ind_index[i]) 
            rough_result.append(ind_index[i])'''              
            #print()
    #write_csv('./data//before//DBLP//DBLP_15_rough.csv',rough_result)          
            
            
            
            
            
            
            
        
    
    
