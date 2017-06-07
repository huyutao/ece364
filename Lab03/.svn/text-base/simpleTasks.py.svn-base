#! /usr/local/bin/python3.4

def loadFile():

    with open("signals.txt", "r") as signalFile:
        lines = signalFile.readlines()

    return lines


def getAverageBySignal(signalName):
    data = loadFile()
    rows = len(data)
    if(signalName[0] == 'T'):
        m=0
    elif(signalName[0] == 'Y'):
        m=1
    elif(signalName[0] == 'U'):
        m=2
    if(signalName[1] == '1'):
        n=1
    elif(signalName[1] == '2'):
        n=2
    elif(signalName[1] == '3'):
        n=3
    index = m*3 + n
    sumup = 0
    for i in range(2,rows):
        number = data[i].split()[index]
        sumup += float(number)
    average = sumup/(rows-2)
    return round(average,2)


def getAverageByDay(day):
    data = loadFile()
    if(day[1] == '1'):
        m=0
    elif(day[1] == '2'):
        m=31
    elif(day[1] == '3'):
        m=59
    n = int(day[3:5])
    needed_row = m+n
    numbers = data[needed_row + 1].split()
    numbers.remove(numbers[0])
    sumup = 0
    for number in numbers:
        sumup += float(number)
    average = sumup/len(numbers)
    return round(average,2)


def split(l, n):
    if(type(l) is not list):
        return None
    length = len(l)
    if(length == 0):
        return None
    i = 0
    result = []
    lists = []
    for number in l:
        if(i == n):
            result.append(lists)
            lists = []
            i = 0
        lists.append(number)
        i += 1
    if(len(lists) != 0):
        result.append(lists)
    return result


def getPalindromes():
    list = []
    for i in range(100,1000):
        for j in range(100,1000):
            number = i*j
            if(number >= 100000 and number <= 999999):
                string = str(number)
                if(string[0]==string[5] and string[1]==string[4] and string[2]==string[3]):
                    if(number not in list):
                        list.append(number)
    return list



def getWords(sentence, c):
    s_list = sentence.split()
    result = []
    for word in s_list:
        if(word[0] == c or word[len(word)-1] == c):
            if (word not in result):
                result.append(word)
    return result


def getCumulativeSum():
    result = []
    for i in range(1,101):
        sumup = 0
        while(i>0):
            sumup += i
            i -= 1
        result.append(sumup)
    return result


def transpose(mat):
    rows=len(mat)
    cols=len(mat[0])
    print(rows)
    print(cols)
    result = []
    for i in range(cols):
        small_result = []
        for j in range(rows):
            small_result.append(mat[j][i])
        result.append(small_result)
    return result


def partition(stream):
    length = len(stream)
    count = 1
    cur_char = stream[0]
    result = []
    for i in range(1,length):
        if(stream[i] == cur_char):
            count += 1
        else:
            result.append(cur_char*count)
            cur_char = stream[i]
            count = 1
    result.append(cur_char*count)
    return result


def getTheSolution():
    result = []
    for x in range(1,999):
        for y in range(1,999 - x):
            z = 1000 - x - y
            if(x**2 + y**2 == z**2 and x < y and y < z):
                result.append(x)
                result.append(y)
                result.append(z)
    return result

if __name__ == "__main__":
    #print(lines)
    print(getAverageBySignal("T1"))
    print(getAverageByDay("03/12"))
    print(len(getPalindromes()))
    list1 = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    list2 = [1, 1, 3, 2, 2, 7, 9, 2, 2, 11, 2]
    list3 = [3, 7, -2, 2, 3, 5]
    print(split(list1, 3))
    print(split(list2, 4))
    print(split(list3, 4))
    sentence1 = "the power of this engine matches that of the one we had last year"
    print(getWords(sentence1,'t'))
    print(getWords(sentence1,'r'))
    print(getWords(sentence1,'e'))
    print(len(getCumulativeSum()))
    matrix=[[9,1],[1,3],[3,1]]
    print(transpose(matrix))
    stream_string = "0001111110111100000100"
    print(partition(stream_string))
    print(getTheSolution())
