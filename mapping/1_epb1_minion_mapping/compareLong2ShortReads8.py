#!/usr/bin/env python2

longReadFile = 'ebpminion_vs_assembly.2500.full.filter.fna'
bins = ['bin.102.fa', 'bin.17.fa', 'bin.31.fa', 'bin.45.fa', 'bin.67.fa'] 
binFilePath = '/srv/projects/abisko/mapping/62_epb1_deep_assembly/84_epb_super_deep.raw.fna.metabat-bins-t40/'

#testing data
#remember to edit data in the 'matchingSequences' dictionary for the test as well
#longReadFile = 'ebpminion_vs_assembly.2500.shuf10.fna'
#bins = ["Short1.txt", "Short2.txt", "Short3.txt"]  
#binFilePath = 'compareLong2ShortTest_'


matchingSequences = {
    bins[0]: [],
    bins[1]: [],
    bins[2]: [],
    bins[3]: [],
    bins[4]: [],
    }
        
#matchingSequences = {
#    "Short1.txt": [],
#    "Short2.txt": [],
#    "Short3.txt": [],
#    }

with open(longReadFile) as inputFile_long:
       
      
    for line in inputFile_long:
        if line[0] == '>':
            identifier_long = line 
            identifier_long = identifier_long.replace('>', '')
            identifier_long = identifier_long.strip()
            #print("identifier_long = " + identifier_long)
            for bin in bins:
                binFile = binFilePath + bin
                with open(binFile) as inputFile_short:
                    for line in inputFile_short:
                        if line[0] == '>':
                            identifier_short = line  
                            identifier_short = identifier_short.replace('>', '')
                            identifier_short = identifier_short.strip()
                            if identifier_long == identifier_short:
                                print('match')
                                matchingSequences[bin].append(identifier_long)
                            else:
                                print('.')
                            #else:
                            #    
                            #   print('match')
                                #print(matchingSequences[bin])
                                #print(identifier_short + 'has a match!')    
    for bin in bins:
        binCount = 0
        for number in matchingSequences[bin]:
            binCount += 1
        print(bin + ' count = ' + str(binCount))
        if binCount != 0:
            print(bin + ' dictionary = ')
            for number in matchingSequences[bin]:
                print number
            print('')
        else:
            print('There were no matches in ' + bin)
        