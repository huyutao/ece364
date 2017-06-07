from operations import Duration

def read_Events():
    result = {}
    with open("Events.txt","r") as list_file:
        lines = list_file.readlines()
    for i in range(2,len(lines)):
        data = lines[i].split()
        length_time = int(data[1][:2])
        if(data[1][2] == 'w'):
            d = Duration(length_time,0,0)
        elif(data[1][2] == 'd'):
            d = Duration(0,length_time,0)
        else:
            d = Duration(0,0,length_time)
        if int(data[2]) != 0:
            d *= int(data[2])
            if data[0] in result:
                new_d = result[data[0]]
                new_d += d
                result[data[0]] = new_d
            else:
                result[data[0]] = d
    return result



def getTotalDuration(eventName):
    dic = read_Events()
    return dic[eventName]


def rankEventsByDuration(*args):
    result = []
    dic = read_Events()
    help_dic = {}
    for eve in args:
        time = str(dic[eve])
        result.append(time)
        help_dic[time] = eve
    result.sort()
    result.reverse()
    final_result = []
    for t in result:
        final_result.append(help_dic[t])
    return final_result


if __name__ == "__main__":
    # dic = read_Events()
    # print(dic["Event17"])
    # for k,v in dic.items():
    #     print(k)
    #     print(v)
    d = getTotalDuration("Event17")
    print(d)
    e = rankEventsByDuration("Event01","Event02","Event03")
    print(e)
