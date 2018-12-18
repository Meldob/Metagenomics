#!/usr/bin/env python2
#program to remove '.' and 'match'


#editFile = 'RmExtraneousSymbolsTest.txt'
editFile = 'Long2ShortReadComparison.txt'


with open(editFile) as inputFile:
    for line in inputFile:
        line = line.strip()
        if line != '.':
            if line != 'match':
                print line