
import re
from uuid import UUID

def fix_name(str):
    name = re.search("([\w]+), ([\w]+)",str)
    if(name != None):
        last = name.group(1)
        first = name.group(2)
        return first + " " +last
    return str

def fix_phone(stri):
    temp = re.findall(r"[\w]+",stri)
    result = ""
    for a in temp:
        result = result + a
    result = "("+ result[0:3]+") "+result[3:6]+"-"+result[6:10]
    return result

def fix_id(stri):
    temp = re.findall(r"[\w]+",stri)
    result = ""
    for a in temp:
        result = result + a
    result = "{"+result+"}"
    result = str(UUID(result))
    return result


def make_list():
    with open("CompanyEmployees.txt","r") as list_file:
        lines = list_file.readlines()
    pattern = r"(?P<name>[\w]+[,\s]+?[\w]+)([,;\s]+)?(?P<id>{?[\w-]+}?)?([,;\s]+)?(?P<phone>[\d\(\)\s-]+)?([,;\s]+)?(?P<state>[\w ]+)?"
    result = []
    for line in lines:
        m = re.match(pattern,line)
        name = m.group("name")
        id = m.group("id")
        phone = m.group("phone")
        state = m.group("state")
        if(id != None and len(id) < 32):
            x = re.search(r"[\d]",id)
            if(x != None):
                phone = id
            else:
                if(state != None):
                    state = id+" "+state
                else:
                    state = id
            id = None
        name = fix_name(name)
        if(id != None):
            id = fix_id(id)
        if(phone != None):
            phone = fix_phone(phone)
        l=[name,id,phone,state]
        result.append(l)
    return result

def getRejectedEntries():
    l = make_list()
    result = []
    for name,id,phone,state in l:
        if(id==None and phone==None and state==None):
            result.append(name)
    result.sort()
    return result


def getCompleteEntries():
    l = make_list()
    result = {}
    for name,id,phone,state in l:
        if(id!=None and phone!=None and state!=None):
            result[name] = (id,phone,state)
    return result


def getEmployeesWithIDs():
    l = make_list()
    result = {}
    for name,id,phone,state in l:
        if(id!=None):
            result[name] = id
    return result


def getEmployeesWithPhones():
    l = make_list()
    result = {}
    for name,id,phone,state in l:
        if(phone!=None):
            result[name] = phone
    return result


def getEmployeesWithStates():
    l = make_list()
    result = {}
    for name,id,phone,state in l:
        if(state!=None):
            result[name] = state
    return result


def getEmployeesWithoutIDs():
    l = make_list()
    result = []
    for name,id,phone,state in l:
        if(id==None and (phone!=None or state!=None)):
            result.append(name)
    result.sort()
    return result


def getEmployeesWithoutPhones():
    l = make_list()
    result = []
    for name,id,phone,state in l:
        if(phone==None and (id!=None or state!=None)):
            result.append(name)
    result.sort()
    return result


def getEmployeesWithoutStates():
    l = make_list()
    result = []
    for name,id,phone,state in l:
        if(state==None and (id!=None or phone!=None)):
            result.append(name)
    result.sort()
    return result

if __name__ == "__main__":
    print(getRejectedEntries())
    print(getEmployeesWithIDs())
    print(getEmployeesWithPhones())
    print(getEmployeesWithStates())
    print(getEmployeesWithoutIDs())
    print(getEmployeesWithoutPhones())
    print(getEmployeesWithoutStates())
    print(getCompleteEntries())
