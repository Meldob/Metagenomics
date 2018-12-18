#!/usr/bin/env python2

with open("ebpminion_vs_assembly.2500.shuf10.sam") as inputFile:
    for line in inputFile:
        values = line.split("\t")  
        identifier = values[2]
        filterObject = values[2]
        sequence = values[9]
        if values[9] != '*':            
            if  filterObject != '*':
                print('>'+ identifier + '\n' + sequence)
    