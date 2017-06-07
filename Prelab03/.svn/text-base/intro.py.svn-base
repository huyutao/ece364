#!/usr/local/bin/python3.4

# ###########################################################
#   Use this section if you have file level comments. This is
#   a good style for scripts.
# ########################################################

import os
import sys  # List of module import statements
import math  # Each one on a line


def getHeadAverage(l, n):
    return sum(l[:n]) / n


def getTailMax(l, m):
    return max(l[-m:])


def getNumberAverage(l):
    num_list = [x for x in l if (isinstance(x,int) or isinstance(x,float)) and not isinstance(x,bool)]
    if(len(num_list) == 0):
        return 0
    else:
        return sum(num_list)/len(num_list)

def getFormattedSSN(n):
    string = str(n)
    new_string = "0" * (9-len(string)) + string
    result = new_string[:3] + '-' + new_string[3:6] + '-' + new_string[6:9]
    return result

def findName(l, s):
    for name in l:
        first_name = name.split()[0]
        last_name = name.split()[1]
        if( first_name == s or last_name == s):
            return name

def getColumnSum(mat):
    list = []
    for col in mat:
        list.append(sum(col))
    return list

def getFormattedNames(ln):
    list = []
    for name in ln:
        str_name = name[2] + ', ' + name[0] + ' ' + name[1] + '.'
        list.append(str_name)
    return list

def getElementwiseSum(l1, l2):
    len1 = len(l1)
    len2 = len(l2)
    list = []
    if(len1 > len2):
        s_len = len2
        longer_list = 1
    else:
        s_len = len1
        longer_list = 2

    for i in range(s_len):
        list.append(l1[i]+l2[i])

    if(longer_list == 1):
        return list + l1[s_len:]
    else:
        return list + l2[s_len:]

def removeDuplicates(l):
    list = []
    for number in l:
        if number not in list:
            list.append(number)
    return list

def getMaxOccurrence(l):
    d = {}
    for num in l:
        if num in d:
            d[num] = d[num] + 1
        else:
            d[num] = 1
    max = 0
    max_k = 0
    for k,v in d.items():
        if v > max:
            max = v
            max_k = k
    return max_k

def getMaxProduct(l):
    length = len(l)
    max = l[0]*l[1]*l[2]
    print(l)
    for i in range(1,(length-2)):
        result = l[i]*l[i+1]*l[i+2]
        if result > max:
            max = result
    return max




if __name__ == "__main__":
    list1 = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    list2 = ['av', 'b', True,15,25,15.5]
    list3 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 120]
    list4 = [4, 9, 16, 25, 36, 49, 64, 81, 100, 120, 140]
    list5 = [1, 1, 3, 2, 2, 7, 9, 2, 2, 11, 2]
    list6 = [3, 7, -2, 2, 3, 5]
    matix = [list1,list3,list4]
    ssn_num1 = 12345
    ssn_num2 = 123456789
    namelist=["Geoge Smith", "Mark Johnson", "Cordell Theodore", "Maria Satterfield", "Johnson Cadence"]
    name = "Johnson"
    name1 = ["George", "W", "Bush"]
    name2 = ["Yutao", "N/A", "Hu"]
    name3 = ["heihei", "mi", "last"]
    ln = [name1,name2,name3]
    print(getHeadAverage(list1, 3))
    print(getTailMax(list1, 3))
    print(getNumberAverage(list1))
    print(getNumberAverage(list2))
    print(getFormattedSSN(ssn_num1))
    print(getFormattedSSN(ssn_num2))
    print(findName(namelist, name))
    print(getColumnSum(matix))
    print(getFormattedNames(ln))
    print(getElementwiseSum(list1,list3))
    print(removeDuplicates(list5))
    print(getMaxOccurrence(list5))
    print(getMaxProduct(list6))

    pass
