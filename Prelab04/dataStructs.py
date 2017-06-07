#! /usr/local/bin/python3.4
import glob

def uniqueLetters(s):
    set_result = set(s)
    result = ''
    for c in set_result:
        result += c
    return result

def scaleSet(aSet, num):
    list = []
    for i in aSet:
        list.append(round(i*num,2))
    return set(list)

def printNames(aSet):
    l = list(aSet)
    l.sort()
    for i in l:
        print (i)

def getStateName(stateAbb):
    state = {"Indiana": "IN", "California": "CA", "Ohio": "OH", "Alabama": "AL", "New York": "NY"}
    for key, value in state.items():
        if value == stateAbb:
            return key

def getZipCodes(stateName):
    d1 = {"Indiana": "IN", "California": "CA", "Ohio": "OH", "Alabama": "AL", "New York": "NY"}
    d2 = {47906: "IN", 47907: "IN", 10001: "NY", 10025: "NY", 90001: "CA", 90005: "CA", 90009: "CA"}
    abb = d1[stateName]
    l = []
    for key, value in d2.items():
        if value == abb:
            l.append(key)
    return set(l)

def printSortedMap(s):
    l = []
    for (lastName, firstName, mi), weight in s.items():
        o = "{1} {2} {0} has a weight of {3} lb.".format(lastName, firstName, mi, weight)
        l.append(o)
    l.sort()
    for line in l:
        print(line)

def switchNames(s):
    d = {}
    for (lastName, firstName, mi), weight in s.items():
        o = firstName + " " + lastName
        d[o] = weight
    return d

def getPossibleMatches(record, n):
    l = []
    for name,(mm,dd,yy) in record.items():
        if (mm == n or dd == n or yy == n):
            l.append(name)
    return set(l)


def getPurchaseReport():
    with open("Item List.txt","r") as list_file:
        line = list_file.readlines()
    d = {}
    for i in range(2,len(line)):
        goods = line[i].split()
        d[goods[0]] = float(goods[1][1:])
    result = {}
    files_id = glob.glob('purchase_*')
    for purchase_id in files_id:
        with open(purchase_id,"r") as list_file:
            line = list_file.readlines()
        sum_price = 0
        for i in range(2,len(line)):
            brought = line[i].split()
            sum_price += d[brought[0]] * int(brought[1])
        result[int(purchase_id[9:12])] = round(sum_price,2)
    return result

def getTotalSold():
    with open("Item List.txt","r") as list_file:
        line = list_file.readlines()
    d = {}
    for i in range(2,len(line)):
        d[line[i].split()[0]] = 0
    files_id = glob.glob('purchase_*')
    for purchase_id in files_id:
        with open(purchase_id,"r") as list_file:
            line = list_file.readlines()
        for i in range(2,len(line)):
            brought = line[i].split()
            d[brought[0]] += int(brought[1])
    return d


if __name__ == "__main__":

    print(uniqueLetters("ABDBDARWET"))
    a_set = {3.12, 5.0, 7.2, 15.24}
    print(scaleSet(a_set, 2.1))
    a_set1 = {'name','yutao','shi','bendan','niuniu'}
    printNames(a_set1)
    print(getStateName('CA'))
    print(getStateName('OH'))
    print(getZipCodes('Indiana'))
    print(getZipCodes('Ohio'))
    print(getZipCodes('New York'))
    stmp = {("Frank", "Xavier", "L"): 209.9, ("James", "Rodney", "M"): 199.0, ("George", "Johnson", "T"): 250.9}
    printSortedMap(stmp)
    print(switchNames(stmp))
    record = {'niuniu': (11, 3, 1995), 'yutao': (11, 2, 1995), 'xitong': (2, 5, 1996)}
    print(getPossibleMatches(record, 1995))
    print(getPossibleMatches(record, 2))
    print(getPurchaseReport())
    print(getTotalSold())






