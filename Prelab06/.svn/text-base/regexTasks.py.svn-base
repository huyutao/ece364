import re

def getWords(sentence,letter):
    pattern1 = r"\b[^{0}\s][\w]*[{0}]\b".format(letter)
    pattern2 = r"\b[{0}][\w]*[^{0}\s]\b".format(letter)
    l1 = re.findall(pattern1,sentence,re.IGNORECASE)
    l2 = re.findall(pattern2,sentence,re.IGNORECASE)
    result = l1+l2
    return result

def extractFloats(s):
    pattern = r"[+-]?[0-9]+\.[0-9]+"
    l = re.findall(pattern,s)
    return l

def getUrlParts(url):
    pattern = r"http\://(?P<BaseAddress>[\w.-]+)/(?P<Controller>[\w.-]+)/(?P<Action>[\w.-]+)\?(?P<QueryString>.*)"
    m = re.match(pattern,url)
    BaseAddress = m.group("BaseAddress")
    Controller = m.group("Controller")
    Action = m.group("Action")
    return (BaseAddress,Controller,Action)

def getQueryParameters(url):
    pattern = r"http\://(?P<BaseAddress>[\w.-]+)/(?P<Controller>[\w.-]+)/(?P<Action>[\w.-]+)\?(?P<QueryString>.*)"
    m = re.match(pattern,url)
    QueryString = m.group("QueryString")
    newpattern = r"[\w.-]+=[\w.-]+"
    n = re.findall(newpattern, QueryString)
    l = []
    for q in n:
        s_pattern = r"(?P<question>[\w.-]+)=(?P<answer>[\w.-]+)"
        o = re.match(s_pattern,q)
        l.append((o.group("question"),o.group("answer")))
    return l

def findFunctions(fileName):
    with open(fileName,"r") as fileptr:
        lines = fileptr.readlines()
    result = []
    for line in lines:
        if(re.match("def",line)):
            o = re.match("def(?P<function_name>[\w ]+)(?P<para>.*)", line)
            function_name = o.group("function_name")
            function_name = re.search("[\w]+",function_name).group(0)
            para = o.group("para")
            pa = re.findall("[\( ]?([\w]+)",para)
            result.append((function_name,pa))
    return result


if __name__ == "__main__":
    s = "The TART program runs on Tuesdays and Thursdays, but it does not start until next week."
    print(getWords(s, 'T'))
    s1 = "The tires can tolerate temperatures between -32.5 and 110. That why they cost 149.95 dollars each."
    print(extractFloats(s1))
    s2 = "The signal fluctuates between -0.3452 and +12.6509 volts. Try to keep it at 6 volts."
    print(extractFloats(s2))
    url = "http://www.purdue.edu/Home/Calendar?Year=2016&Month=September&Semester=Fall"
    print(getUrlParts(url))
    print(getQueryParameters(url))
    url1 = "http://www.google.com/Math/Constants?Pi=3.14&Max_Int=65536&What_Else=Nothing-Here"
    print(getUrlParts(url1))
    print(getQueryParameters(url1))
    print(findFunctions("test.py"))
    print(findFunctions("regexTasks.py"))


