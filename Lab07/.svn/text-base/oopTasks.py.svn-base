
class Experiment:

    def __init__(self, experimentNo, experimentDate, virusName, unitCount, unitCost):
        self.experimentNo = experimentNo
        self.experimentDate = experimentDate
        self.virusName = virusName
        self.unitCount = unitCount
        self.unitCost = unitCost
        self.totalCost = self.unitCount * self.unitCost

    def __str__(self):
        result = "{0:03d}, {1}, ${2:06.2f}: {3}".format(self.experimentNo,self.experimentDate,self.totalCost,self.virusName)
        return result


class Technician:

    def __init__(self, techName, techID):
        self.techName = techName
        self.techID = techID
        self.experiments = {}

    def __str__(self):
        result = "{0}, {1}: {2:02d} Experiments".format(self.techID, self.techName, len(self.experiments))
        return result

    def addExperiment(self, experiment):
        number = experiment.experimentNo
        self.experiments[number] = experiment

    def getExperiment(self, expNo):
        if(expNo in self.experiments):
            return self.experiments[expNo]
        else:
            return None

    def loadExperimentsFromFile(self, fileName):
        with open(fileName,"r") as list_file:
            lines = list_file.readlines()
        for i in range(2,len(lines)):
            data = lines[i].split()
            exp = Experiment(int(data[0]),data[1],data[2],int(data[3]),float(data[4][1:]))
            self.addExperiment(exp)


    def generateTechActivity(self):
        l_key = list(self.experiments.keys())
        l_key.sort()
        result = "{0}, {1}".format(self.techID, self.techName)
        for k in l_key:
            result += "\n" + str(self.experiments[k])
        return result



class Laboratory:

    def __init__(self, labName):
        self.labName = labName
        self.technicians = {}

    def __str__(self):
        l_key = list(self.technicians.keys())
        result = "{0}: {1:02d} Technicians".format(self.labName,len(self.technicians))
        str_list = []
        for v in self.technicians.values():
            str_list = str_list + [str(v)]
        str_list.sort()
        for tech in str_list:
            result += "\n" + tech
        return result

    def addTechnician(self, technician):
        name = technician.techName
        self.technicians[name] = technician

    def getTechnicians(self, *args):
        l=[]
        for arg in args:
            l.append(self.technicians[arg])
        return l

    def generateLabActivity(self):
        l_key = list(self.technicians.keys())
        l_key.sort()
        result = ""
        for k in l_key:
            result += self.technicians[k].generateTechActivity() + "\n\n"
        return result[:-2]




if __name__ == "__main__":
    tech1 = Technician("Sherlock Holmes", "55926-36619")
    tech1.loadExperimentsFromFile("report 55926-36619.txt")

    tech2 = Technician("Irene Adler", "69069-29232")
    tech2.loadExperimentsFromFile("report 69069-29232.txt")

    tech3 = Technician("John Watson", "75471-28954")
    tech3.loadExperimentsFromFile("report 75471-28954.txt")

    # Create a new lab
    lillyLab = Laboratory("Eli Lilly")
    lillyLab.addTechnician(tech2)
    lillyLab.addTechnician(tech1)
    lillyLab.addTechnician(tech3)
    #print(lillyLab)
    print(lillyLab.generateLabActivity())
