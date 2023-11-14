# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 21:12:24 2019

@author: Administrator
"""

import matplotlib.pyplot as plt
 
x1 = ['1', '2', '3', '4', '5']
 
y1 = [0.9225, 0.9376, 0.9376, 0.9376, 0.9376]
y2 = [0.9376, 0.9376, 0.9376, 0.9376, 0.9376]
y3 = [0.9162, 0.9279, 0.9162, 0.9270, 0.9251]
y4 = [0.9376, 0.9376, 0.9376, 0.9376, 0.9376]

 
# 设置画布大小
plt.figure(figsize=(6, 4))
 
# 数据
plt.plot(x1, y1, label='LR ', linewidth=2, color='g', marker='o', markersize=5)
plt.plot(x1, y2, label='CN', linewidth=2, color='b', marker='o', markersize=5)
plt.plot(x1, y3, label='e-Trus', linewidth=2, color='yellow', marker='o', markersize=5)
plt.plot(x1, y4, label='OURS', linewidth=2, color='r', marker='o', markersize=5)
 
# 横坐标描述
plt.xlabel('Times')
 
# 纵坐标描述
plt.ylabel('Acc')
 
plt.legend()
plt.savefig("Acc.png")
plt.show()



