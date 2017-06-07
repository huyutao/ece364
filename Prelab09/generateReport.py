#!/usr/local/bin/python3.4
import glob
import sys
import os
import filecmp
import re


def convertToAttrib():
    with open("rawGrades.xml","r") as f:
        lines = f.read()
    o = open("finalGrades.xml",'w', newline="\r\n")
    lines = lines.strip(" ")
    #print(lines)
    ID = re.findall(r"<(.*?)>(.*?):(.*?)</(.*?)>",lines)

    o.write("<?xml version=\"1.0\"?>")
    o.write("\n<students>")
    #print(ID[0])
    subject = []
    for i in range(0,len(ID)):
        marks = {}
        id = ID[i][0]
        name = ID[i][1]
        rest = ID[i][2]
        id2 = ID[i][3]
        if id == id2:
            o.write("\n   <student name=\""+name+"\" "+"id=\""+id+"\">")
            marks_subject = re.findall(r"\[(.*?):(.*?)\]",rest)
            for i in range(0,len(marks_subject)):
                marks[marks_subject[i][0]] = marks_subject[i][1]
            keylist = []
            new = []
            new = marks.keys()
            for key in new:
                keylist.append(key)
            keylist.sort()
            for key in keylist:
                value = marks[key]
                o.write("\n      <ECE"+key+" score=\""+value+"\""+" grade=\"")
                if(int(value) < 60):
                    o.write("F\"/>")
                if(int(value) >= 60 and int(value) < 70):
                    o.write("D\"/>")
                if(int(value) >= 70 and int(value) < 80):
                    o.write("C\"/>")
                if(int(value) >= 80 and int(value) < 90):
                    o.write("B\"/>")
                if(int(value) >= 90):
                    o.write("A\"/>")
            o.write("\n   </student>")
    o.write("\n</students>")
    o.close()

if __name__ == "__main__":
    convertToAttrib()