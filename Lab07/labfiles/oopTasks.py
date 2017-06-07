
class Experiment:

    def __init__(self, experimentNo, experimentDate, virusName, unitCount, unitCost):
        pass

    def __str__(self):
        pass


class Technician:

    def __init__(self, techName, techID):
        pass

    def __str__(self):
        pass

    def addExperiment(self, experiment):
        pass

    def getExperiment(self, expNo):
        pass

    def loadExperimentsFromFile(self, fileName):
        pass

    def generateTechActivity(self):
        pass


class Laboratory:

    def __init__(self, labName):
        pass

    def __str__(self):
        pass

    def addTechnician(self, technician):
        pass

    def getTechnicians(self, *args):
        pass

    def generateLabActivity(self):
        pass
