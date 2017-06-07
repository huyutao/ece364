from oopTasks import *

# Populate some technicians
tech1 = Technician("Sherlock Holmes", "55926-36619")
tech1.loadExperimentsFromFile("report 55926-36619.txt")

tech2 = Technician("Irene Adler", "69069-29232")
tech2.loadExperimentsFromFile("report 69069-29232.txt")

tech3 = Technician("John Watson", "75471-28954")
tech3.loadExperimentsFromFile("report 75471-28954.txt")

# Create a new lab
lillyLab = Laboratory("Eli Lilly")
lillyLab.addTechnician(tech1)
lillyLab.addTechnician(tech2)
lillyLab.addTechnician(tech3)

# Prepare the report
firstLine = "About the Current Laboratory:"
separator = "-" * 50

reportLines = [firstLine]
reportLines.append(separator)
reportLines.append(str(lillyLab))
reportLines.append("")
reportLines.append("Current Activities in the Lab:")
reportLines.append(separator)
reportLines.append(lillyLab.generateLabActivity())

# Persist in a file.
with open("output.txt", "w") as outFile:
    report = "\n".join(reportLines)
    outFile.write(report)

