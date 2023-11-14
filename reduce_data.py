# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 18:57:17 2019

@author: Administrator
"""

import networkx as nx
import csv
import numpy as np
import sys

def read_data(path):
    result = []
    with open(path,"r") as csvfile:        
        reader = csv.reader(csvfile)
        for line in reader:
            if len(line) == 12 or len(line) == 14:
                #print(list(map(str,line)))
                result.append(list(map(str,line)))
    #print(type(result[0][0]))
    result = np.array(result)
    #print(result.shape)
    return result

def write_csv(path,data):
    with open(path,'w',newline='') as csvfile:
        writer = csv.writer(csvfile)
        for i in range(len(data)):
            writer.writerow(data[i])
def cal_indegree(node,edges):
    indegree = 0
    for e in edges:
        if node == e[1]:
            indegree += 1
    return indegree-1

data = read_data('./data//before//OTC//OTC.csv')
# data = read_data('./data//before//Wikivote//Wikivote.csv')
# data = read_data('./data//before//DBLP//CoAuthorNetworks.csv')
# data = read_data('./data//before//Epinions//Epinions.csv')
# data = read_data('./data//before//Alpha//Alpha.csv')

r_data = data[:,:3]       


G_asymmetric = nx.DiGraph()
for rd in r_data:
    G_asymmetric.add_edge(rd[0],rd[1])
    
reduce = []
r_list = []
for rd in r_data:
    if rd[0] not in r_list:
        r_list.append(rd[0])
        reduce.append([rd[0],nx.degree(G_asymmetric,rd[0])])
    if rd[1] not in r_list:
        r_list.append(rd[1])
        reduce.append([rd[1],nx.degree(G_asymmetric,rd[1])])

reduce = sorted(reduce,key=(lambda x:x[1]),reverse=True)
reduce = np.array(reduce)

reduce = reduce[:int(reduce.shape[0]/2)]
'''
for i in range(reduce.shape[0]):
    if int(reduce[i][1])<50:
        reduce = reduce[:i]
        break
'''
#sys.exit()
r_list = []
for r in reduce:
    r_list.append(r[0])

G_asymmetric.clear() 
G_asymmetric = nx.DiGraph()   
G = nx.Graph() 

reduce_data = []
for d in data:
    if d[0] in r_list and d[1] in r_list:
        reduce_data.append(d[:3].tolist())
        G_asymmetric.add_edge(d[0],d[1])
        G.add_edge(d[0],d[1])

'''
print(reduce_data[0])
print(nx.degree_centrality(G_asymmetric)[reduce_data[0][0]])
print(nx.closeness_centrality(G_asymmetric)[reduce_data[0][0]])
print(nx.betweenness_centrality(G_asymmetric)[reduce_data[0][0]])
#nx.algorithms.cluster.clustering()
''' 

betweenness_centrality = nx.betweenness_centrality(G_asymmetric)
closeness_centrality = nx.closeness_centrality(G_asymmetric)
degree_centrality = nx.degree_centrality(G_asymmetric)  
count = 0 
for rd in reduce_data:
    rd.append(cal_indegree(rd[0],reduce_data))
    rd.append(cal_indegree(rd[1],reduce_data))
    rd.append(nx.degree(G_asymmetric,rd[0])-rd[3])
    rd.append(nx.degree(G_asymmetric,rd[1])-rd[4])
    rd.append(nx.degree(G_asymmetric,rd[0]))
    rd.append(nx.degree(G_asymmetric,rd[1]))
    rd.append(len(list(set(nx.neighbors(G_asymmetric,rd[0]))&set(nx.neighbors(G_asymmetric,rd[1])))))    
    rd.append(len(list(set(nx.neighbors(G_asymmetric,rd[0]))|set(nx.neighbors(G_asymmetric,rd[1])))))
    rd.append(nx.clustering(G,rd[0])+nx.clustering(G,rd[1]))
    rd.append(betweenness_centrality[rd[0]]+closeness_centrality[rd[0]]+degree_centrality[rd[0]])
    rd.append(betweenness_centrality[rd[1]]+closeness_centrality[rd[1]]+degree_centrality[rd[1]])
    #print(rd[-2],rd[-1])
    count+=1
    print(count)
    
write_csv('./data//before//OTC//OTC_all_11.csv',reduce_data)
# write_csv('./data//before//Wikivote_reduce//Wikivote_all_11.csv',reduce_data)
#write_csv('./data//before//Epinions//reduce_fu//Epinions_all_11.csv',reduce_data)
#write_csv('./data//before//DBLP//DBLP_all_11.csv',reduce_data)
#write_csv('./data//before//Alpha//Alpha_all_11.csv',reduce_data)

data = read_data('./data//before//OTC//OTC_all_11.csv')
# data = read_data('./data//before//Wikivote_reduce//Wikivote_all_11.csv')
#data = read_data('./data//before//Epinions//reduce_fu//Epinions_all_11.csv')
#data = read_data('./data//before//Alpha//Alpha_all_11.csv')
data = data.tolist()
for i in range(len(data)):
    triangle_1 = 0
    triangle_2 = 0
    triangle_3 = 0
    triangle_4 = 0
    comm = list(set(nx.neighbors(G_asymmetric,data[i][0]))&set(nx.neighbors(G_asymmetric,data[i][1])))
    if len(comm) == 0:
        data[i].append(float(0))
        data[i].append(float(0)) 
        data[i].append(float(0))
        data[i].append(float(0))
    else:
        for j in range(len(comm)):
            num = 1
            positive_num = 0
            if data[i][2] == 1:
                positive_num += 1
            for d in data:
                index_temp = []
                index_temp.append(d[0])
                index_temp.append(d[1])
                if comm[j] in index_temp and (data[i][0] in index_temp or data[i][1] in index_temp) and not (data[i][0] in index_temp and data[i][1] in index_temp):
                    if d[2] == '1':
                        positive_num += 1
                        num+=1
                        #break
                if num==3:
                    break
            if positive_num == 3:
                triangle_1+=1
            elif positive_num == 2:
                triangle_2+=1
            elif positive_num == 1:
                triangle_3+=1
            elif positive_num == 0:
                triangle_4+=1
                
        data[i].append(float(triangle_1))
        data[i].append(float(triangle_2)) 
        data[i].append(float(triangle_3))
        data[i].append(float(triangle_4)) 
        
    #print(float(triangle_1),float(triangle_2),float(triangle_3),float(triangle_4))
    print(i,'finished',len(data))

write_csv('./data//before//OTC//OTC_all_15.csv',data)
# write_csv('./data//before//Wikivote_reduce//Wikivote_all_15.csv',data)
#write_csv('./data//before//Epinions//reduce_fu//Epinions_all_15.csv',data)
#write_csv('./data//before//DBLP//DBLP_all_15.csv',data)
#write_csv('./data//before//Alpha//Alpha_all_15.csv',data)













