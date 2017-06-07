def make_dic1():
    with open("AccessCards.txt","r") as list_file:
        line = list_file.readlines()
    dict1 = {}
    for i in range(2,len(line)-1):
        cards = line[i].split('|')
        dict1[cards[1].strip()] = cards[0].strip()
    return dict1


def make_dic2():
    dict2 = {}
    with open("Permissions.txt","r") as pe_file:
        line_p = pe_file.readlines()
    for i in range(2,len(line_p)):
        permission = line_p[i].split(' - ')
        if(permission[0].strip() in dict2):
            dict2[permission[0].strip()].add(permission[1].strip())
        else:
            dict2[permission[0].strip()] = set()
            dict2[permission[0].strip()].add(permission[1].strip())
    return dict2


def getUserPermissions():
    dict1 = make_dic1()
    dict2 = make_dic2()
    result = {}
    for key,value in dict2.items():
        result[dict1[key]] = value
    return result


def getFloorPermissions():
    dict1 = make_dic1()
    result = {}
    with open("Permissions.txt","r") as pe_file:
        line_p = pe_file.readlines()
    for i in range(2,len(line_p)):
        permission = line_p[i].split(' - ')
        if(permission[1].strip() not in result):
            result[permission[1].strip()] = set()
        result[permission[1].strip()].add(dict1[permission[0].strip()])
    return result


def getFloorRooms():
    with open("AccessLog.txt","r") as list_file:
        line_log = list_file.readlines()
    result = {}
    for i in range(2,len(line_log)):
        building = line_log[i].split(' - ')[1]
        floor,room = building.split('-')
        if(floor not in result):
            result[floor] = set()
        result[floor].add(room.strip())
    return result


def isAccessGrantedFor(userName, attempt):
    dict_p = getUserPermissions()
    floor,room = attempt
    if(floor in dict_p[userName]):
        return True
    else:
        return False


def checkAttempts():
    with open("AccessLog.txt","r") as list_file:
        line_log = list_file.readlines()
    result = []
    dict1 = make_dic1()
    dict2 = make_dic2()
    for i in range(len(line_log)):
        id, building = line_log[i].split(' - ')
        name = dict1[id]
        floor,room = building.split('-')
        room = room.strip()
        if(floor in dict2[id]):
            tup = (name,floor,room,True)
        else:
            tup = (name,floor,room,False)
        result.append(tup)
    return result


def getAttemptsOf(userName):
    l = checkAttempts()
    result = []
    for name,floor,room,bol in l:
        if (userName == name):
            result.append((floor,room,bol))
    result.sort()
    return result


def getUserAttemptSummary():
    l = checkAttempts()
    result = {}
    for name,floor,room,bol in l:
        if(name not in result):
            result[name] = (0,0)
        passed,not_passed = result[name]
        if(bol):
            passed += 1
        else:
            not_passed += 1
        result[name] = (passed,not_passed)
    return result


def getFloorAttemptSummary():
    l = checkAttempts()
    result = {}
    for name,floor,room,bol in l:
        if(floor not in result):
            result[floor] = (0,0)
        passed,not_passed = result[floor]
        if(bol):
            passed += 1
        else:
            not_passed += 1
        result[floor] = (passed,not_passed)
    return result


def getRoomAttemptSummary():
    l = checkAttempts()
    result = {}
    for name,floor,room,bol in l:
        if(room not in result):
            result[room] = (0,0)
        passed,not_passed = result[room]
        if(bol):
            passed += 1
        else:
            not_passed += 1
        result[room] = (passed,not_passed)
    return result


if __name__ == "__main__":
    print(make_dic1())
    print(make_dic2())
    print(getUserPermissions())
    print(getFloorPermissions())
    print(getFloorRooms())
    print(checkAttempts())
    print(getAttemptsOf('Gray, Tammy'))
    print(isAccessGrantedFor('Rivera, Patricia', ('Servers','Room46')))
    print(isAccessGrantedFor('Reed, Bobby', ('Equipments','Room86')))
    print(getUserAttemptSummary())
    print(getFloorAttemptSummary())
    print(getRoomAttemptSummary())

