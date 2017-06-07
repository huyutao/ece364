import math

def print_matrix(matrix):
    for i in range(9):
        for j in range(9):
            print(matrix[i][j]+' ',end='')
        print('')

def isValidOutput(fileName):
    with open(fileName,"r") as list_file:
        line = list_file.readlines()
    matrix = [[0 for x in range(9)] for y in range(9)]
    for i in range(9):
        for j in range(9):
            matrix[i][j] = line[i][j]
    row_valid = [0] * 9
    col_valid = [0] * 9
    for i in range(9):
        for j in range(9):
            row_valid[int(matrix[i][j])-1] = row_valid[int(matrix[i][j])-1] + 1
            col_valid[int(matrix[j][i])-1] = col_valid[int(matrix[j][i])-1] + 1
        for k in row_valid:
            if(k != i+1):
                return False
        for k in col_valid:
            if(k != i+1):
                return False
    return True

def isColumnPuzzle(fileName):
    with open(fileName,"r") as list_file:
        line = list_file.readlines()
    matrix = [[0 for x in range(9)] for y in range(9)]
    for i in range(9):
        for j in range(9):
            matrix[i][j] = line[i][j]
    for i in range(9):
        if(matrix[0][i] == '.'):
            for j in range(9):
                if(matrix[j][i] != '.'):
                    break
            return True
    return False

def solvePuzzle(sourceFileName, targetFileName):
    with open(sourceFileName,"r") as list_file:
        line = list_file.readlines()
    matrix = [[0 for x in range(9)] for y in range(9)]
    for i in range(9):
        for j in range(9):
            matrix[i][j] = line[i][j]
    cnt = [0] * 9
    if(isColumnPuzzle(sourceFileName)):
        for i in range(9):
            for j in range(9):
                if(matrix[i][j] != '.'):
                    cnt[int(matrix[i][j]) - 1] = cnt[int(matrix[i][j]) - 1] + 1
                else:
                    flag=j
            for k in range(9):
                if(cnt[k] != i+1):
                    matrix[i][flag] = str(k+1)
                    cnt[k]+=1
    else:
        for i in range(9):
            for j in range(9):
                if(matrix[j][i] != '.'):
                    cnt[int(matrix[j][i]) - 1] = cnt[int(matrix[j][i]) - 1] + 1
                else:
                    flag=j
            for k in range(9):
                if(cnt[k] != i+1):
                    matrix[flag][i] = str(k+1)
                    cnt[k]+=1
    with open(targetFileName,"w") as write_file:
        for i in range(9):
            for j in range(9):
                write_file.write(matrix[i][j])
            write_file.write('\n')


def get_call_dict(flag):
    with open("People.txt","r") as People:
        line = People.readlines()
    dict={}
    for i in range(2,len(line)):
        name,num = line[i].split("|")
        name = name.strip()
        num = num.strip()[1:]
        if(flag):
            dict[name] = num
        else:
            dict[num] = name
    return dict

def get_act_list():
    with open("ActivityList.txt","r") as Activities:
        line = Activities.readlines()
    l = []
    for i in range(2,len(line)):
        cfrom,cto,dur = line[i].split()
        l.append((cfrom,cto,dur))
    return l

def get_last(full_num):
    return full_num[8:12]

def getCallersOf(phoneNumber):
    dict = get_call_dict(0)
    l = get_act_list()
    result = []
    for cfrom,cto,dur in l:
        if(cto == phoneNumber):
            result.append(dict[get_last(cfrom)])
    result = list(set(result))
    result.sort()
    return result

def arrange_time(hh,mm,ss):
    result_ss = ss % 60
    inc_min = math.floor(ss/60)
    mm += inc_min
    result_mm = mm % 60
    hh = math.floor(mm/60) + hh
    return (hh,result_mm,result_ss)

def getCallActivity():
    dict = get_call_dict(0)
    l = get_act_list()
    result = {}
    for cfrom,cto,dur in l:
        name = dict[get_last(cfrom)]
        n_mm = dur[:2]
        n_ss = dur[3:5]
        if name not in result:
            result[name] = (0,0,0,0)
        num_call,hh,mm,ss = result[name]
        num_call += 1
        mm += int(n_mm)
        ss += int(n_ss)
        result[name] = (num_call,hh,mm,ss)
    for key, infor in result.items():
        num_call,hh,mm,ss = infor
        hh,mm,ss = arrange_time(hh,mm,ss)
        result_time = "{0:02d}:{1:02d}:{2:02d}".format(hh,mm,ss)
        result[key] = (num_call,result_time)
    return result


if __name__ == "__main__":
    print(isValidOutput('valid.sud'))
    print(isValidOutput('invalid1.sud'))
    print(isValidOutput('invalid2.sud'))
    print(isColumnPuzzle('open1.sud'))
    print(isColumnPuzzle('open2.sud'))
    solvePuzzle('open1.sud', 'open1_solve.sud')
    solvePuzzle('open2.sud', 'open2_solve.sud')
    print(isValidOutput('open1_solve.sud'))
    print(isValidOutput('open2_solve.sud'))
    print(getCallersOf("707-825-5871"))
    print(getCallActivity())
    callMap = getCallActivity ()
    print(callMap["Edwards, Rachel"])
