# coding=utf-8                        # 全文utf-8编码
import sys
import csv


def apriori(D, minSup):
    '''频繁项集用keys表示，
    key表示项集中的某一项，
    cutKeys表示经过剪枝步的某k项集。
    C表示某k项集的每一项在事务数据库D中的支持计数
    '''

    C1 = {}
    for T in D:
        for I in T:
            if I in C1:
                C1[I] += 1
            else:
                C1[I] = 1

    # print(C1)
    _keys1 = C1.keys()

    keys1 = []
    for i in _keys1:
        keys1.append([i])

    n = len(D)
    cutKeys1 = []
    for k in keys1[:]:
        if C1[k[0]] * 1.0 / n >= minSup:
            cutKeys1.append(k)

    cutKeys1.sort()

    keys = cutKeys1
    all_keys = []
    while keys != []:
        C = getC(D, keys)
        cutKeys = getCutKeys(keys, C, minSup, len(D))
        # print(cutKeys)
        for key in cutKeys:
            all_keys.append(key)
        keys = aproiri_gen(cutKeys)
    # print(keys)

    return all_keys


def getC(D, keys):
    '''对keys中的每一个key进行计数'''
    C = []
    for key in keys:
        c = 0
        for T in D:
            have = True
            for k in key:
                if k not in T:
                    have = False
            if have:
                c += 1
        C.append(c)
    return C


def getCutKeys(keys, C, minSup, length):
    '''剪枝步'''
    i = 0
    while i < len(keys):
        # print(keys[i], float(C[i]) / length, minSup)
        if float(C[i]) / length < minSup:
            keys.remove(keys[i])
            C.remove(C[i])
        else:
            i += 1
    return keys


def keyInT(key, T):
    '''判断项key是否在数据库中某一元组T中'''
    for k in key:
        if k not in T:
            return False
    return True


def aproiri_gen(keys1):
    '''连接步'''
    keys2 = []
    for k1 in keys1:
        for k2 in keys1:
            if k1 != k2:
                key = []
                for k in k1:
                    if k not in key:
                        key.append(k)
                for k in k2:
                    if k not in key:
                        key.append(k)
                key.sort()
                if key not in keys2 and len(key) == len(k1) + 1:
                    keys2.append(key)

    return keys2


def read_data(path):
    result = []
    with open(path, "r") as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            result.append(line)
    # result = np.array(result)
    return result


if __name__ == '__main__':
    classes = 2
    target = 0.01
    Ex = []
    En = []
    He = []
    CD = []

    data = read_data('./data//before//Alpha//Alpha_15_01.csv')
    # data = read_data('./data//before//OTC//OTC_15_01.csv')
    # data = read_data('./data//before//DBLP//DBLP_15_01.csv')
    # data = read_data('./data//before//Slashdot//Slashdot_15_01.csv')
    D = []
    C = ['a', 'b', 'c', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']
    for i in range(len(data)):
        temp = []
        for j in range(3, len(data[0])):
            if data[i][j] == '1.0':
                temp.append(C[j])
        D.append(temp)

    # D = [['A','B','C','D'],['A','B','C','E'],['A','B','C','D','E'],['B','D','E'],['A','B','C','D']]
    F = apriori(D, 0.21)
    '''
    Fl = []
    for i in range(len(F)):
        if '6' not in F[i]:
            Fl.append(F[i])
    '''
    print('\nfrequent itemset:\n', F)
