import sys
import os
import string
import re
import collections

#   Entry Class
class Entry:
    #   Constructor
    def __init__(self, k = 0, v = '' ):
        if type(k) is int:
            self.key = k
        else:
            raise TypeError( "First argument needs to be an int")
        if type(v) is str:
            self.value = v
        else:
            raise TypeError( "Second argument needs to be a string")

    #   Function overloads
    def __str__(self):
        retStr = "({0}: \"{1}\")".format( self.key, self.value )
        return retStr

    def __hash__(self):
        t = (self.key, self.value)
        return hash(t)

class Lookup:
    #   Member Variables
    typed = {}

    #   Constructor
    def __init__(self, name=""):
        if name == "":
            raise ValueError( "Name cannot be empty")
        else:
            self._name = name
            self._entrySet = set()

    #   Function Overloads
    def __str__(self):
        retStr = "[\"{0}\": {1:02d} Entries]".format( self.name, len( self._entrySet ))

    #   Function Declarations
    def addEntry(self, entry):
        for element in self._entrySet:
            if element.key == entry.key:
                raise ValueError( "Entry already exists" )
                return
        #   Add to backing store
        self._entrySet.add( entry )

    def updateEntry(self, entry):
        exists = 0
        for element in self._entrySet:
            if element.key == entry.key:
                #   Update entry
                exists = 1
                removing = element
        if exists:
            self._entrySet.remove( removing )
        else:
            raise ValueError( "Entry does not exist" )

    def addOrUpdateEntry(self, entry):
        exists = 0
        for element in self._entrySet:
            if element.key == entry.key:
                #   Update entry
                exists = 1
        if exists:
            self.updateEntry( entry )
        else:
            self.addEntry( entry )

    def removeEntry( self, entry ):
        if entry in self._entrySet:
            self._entrySet.remove( entry )
        else:
            raise KeyError( "Entry does not exist" )

    def getEntry(self, key ):
        exists = 0
        for element in self._entrySet:
            if element.key == key:
                #   exists
                exists = 1
                get = element
        if exists:
            return get
        else:
            raise KeyError( "Entry does not exist" )

    def addOrUpdateFromDictionary(self, someDict):
        allKeys = someDict.keys()
        keylist = []

        for key in allKeys:
            keylist.append( key )

        for key in keylist:
            entry = Entry( key, someDict[key])
            self.addOrUpdateEntry( entry )

    def getAdDictionary(self):
        retDict = {}
        for element in self._entrySet:
            retDict[element.key] = element.value

        return retDict

    def getKeys(self):
        keyList = []
        for element in self._entrySet:
            keyList.append( element.key )


        return keyList

    def getValues(self):
        valueList = []
        for element in self._entrySet:
            valueList.append( element.value )

        return valueList

    def ElementCount(self):
        count = 0
        for element in self._entrySet:
            count += 1

        return count

def main():
    pass

if __name__ == "__main__" :
    main()