import moduleTasks

def loadSignals(signalNames, signalFolder, maxNonfloatCount):
    result_dict = {}
    for signalName in signalNames:
        try:
            v,c = moduleTasks.loadSignal(signalName, signalFolder)
            if c < maxNonfloatCount:
                result_dict[signalName] = v
            else:
                result_dict[signalName] = []
        except:
            result_dict[signalName] = None
    return result_dict




def saveSignals(signalsDictionary, valueRange, maxCount, targetFolder):
    for k,v in signalsDictionary.items():
        try:
            file_name = targetFolder + "/" + k + ".txt"
            if moduleTasks.isSignalAcceptable(v,valueRange,maxCount):
                with open(file_name,"w") as write_file:
                    write_str = ""
                    for num in v:
                        write_str += "{0:.3f}\n".format(num)
                    write_file.write(write_str[:-1])
        except:
            pass





if __name__ == "__main__":
    signals_name = ["AFW-481","CIG-308","FPT-701","REY-386","stupid"]
    sig_dit = loadSignals(signals_name,"Signals",10)
    saveSignals(sig_dit,(-15,15.7),20,"nice_data")
    for k,v in sig_dit.items():
        print(k)
        print(v)

