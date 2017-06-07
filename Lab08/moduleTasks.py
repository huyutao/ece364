
def isNameValid(signalName):
    length = len(signalName)
    if(length != 7):
        return False
    sig = signalName.split("-")
    sig_c = sig[0]
    sig_n = sig[1]
    if(len(sig_c) != 3 or len(sig_n) != 3):
        return False
    for c in sig_c:
        if not c.isalpha():
            return False
    for n in sig_n:
        if not n.isalnum():
            return False
    return True


def loadSignal(signalName, signalFolder):
    if(not isNameValid(signalName)):
        raise ValueError("{} is invalid".format(signalName))
    file_name = signalFolder + "/" + signalName + ".txt"
    try:
        with open(file_name,"r") as list_file:
            lines = list_file.readlines()
    except:
        raise OSError("{0}.txt is missing in the folder {1}".format(signalName,signalFolder))
    nonf = 0
    l_f = []
    for line in lines:
        try:
            value = float(line)
            l_f.append(value)
        except:
            nonf += 1
    return (l_f,nonf)



def isSignalAcceptable(signal, valueRange, maxCount):
    if signal == None:
        raise ValueError("Signal is None")
    if len(signal) == 0:
        raise ValueError("Signal contains no data")
    min_n,max_n = valueRange
    result = 0
    for num in signal:
        if(num>max_n or num<min_n):
            result += 1
    if(result > maxCount):
        return False
    else:
        return True



if __name__ == "__main__":
    #print(isNameValid("AEF-996"))
    #print(isNameValid("WAEF-996"))
    #print(isNameValid("AEF-2020"))
    v,c = loadSignal("REY-386", "Signals")
    print(len(v))
    print(isSignalAcceptable(v,(-12.0,11.7),5))
    print(isSignalAcceptable([],(-12.0,11.7),20))
