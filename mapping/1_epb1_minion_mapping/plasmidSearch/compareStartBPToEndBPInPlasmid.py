#!/usr/bin/env python2

#REGULAR TEST
#filePath = ''
#forwardFileFirst500 = 'compareStartBPToEndBPInPlasmid_TestText1.txt'
#reverseFileLast500 = 'compareStartBPToEndBPInPlasmid_TestText2.txt'
#forwardFileLast500 = 'compareStartBPToEndBPInPlasmid_TestText1.txt'
#reverseFileFirst500 = 'compareStartBPToEndBPInPlasmid_TestText2.txt'

#BRASSICA PLASMID TEST
filePath = 'brassica_napus_plasmid.fixed.bam'
forwardFileFirst500 = '/final.contigs.fa.brassica_napus_plasmid.fixed.1.fq_1st500_1.sam'
forwardFileLast500 = '/final.contigs.fa.brassica_napus_plasmid.fixed.1.fq_last500_1.sam'
reverseFileLast500 = '/final.contigs.fa.brassica_napus_plasmid.fixed.1.fq_last500_2.sam'
reverseFileFirst500 = '/final.contigs.fa.brassica_napus_plasmid.fixed.1.fq_1st500_2.sam'

#NOSTOC PLASMID TEST
#filePath = 'nostoc_azollae_plasmid.fixed.bam'
#forwardFileFirst500 = '/final.contigs.fa.nostoc_azollae_plasmid.fixed.1.fq_1st500_1.sam'
#forwardFileLast500 = '/final.contigs.fa.nostoc_azollae_plasmid.fixed.1.fq_last500_1.sam'
#reverseFileLast500 = '/final.contigs.fa.nostoc_azollae_plasmid.fixed.1.fq_last500_2.sam'
#reverseFileFirst500 = '/final.contigs.fa.nostoc_azollae_plasmid.fixed.1.fq_1st500_2.sam'


#ACETOBACTER PLASMID TEST
#filePath = 'AcetobacterPasteurianus.bam'
#forwardFileFirst500 = '/final.contigs.fa.AcetobacterPasteurianus.1.fq_1st500_1.sam'
#forwardFileLast500 = '/final.contigs.fa.AcetobacterPasteurianus.1.fq_last500_1.sam'
#reverseFileLast500 = '/final.contigs.fa.AcetobacterPasteurianus.1.fq_last500_2.sam'
#reverseFileFirst500 = '/final.contigs.fa.AcetobacterPasteurianus.1.fq_1st500_2.sam'




fullForwardFilePathFirst500 = filePath + forwardFileFirst500
fullForwardFilePathLast500 = filePath + forwardFileLast500
fullReverseFilePathLast500 = filePath + reverseFileLast500
fullReverseFilePathFirst500 = filePath + reverseFileFirst500

#fullForwardFilePath = forwardFile
#fullReverseFilePath = reverseFile


#first code compares first 500bp in the forward strand to the last 500bp in the reverse strand
with open(fullForwardFilePathFirst500) as inputFile:
    count = 0
    identifiers = ['']
    matchingIdentifiers = []
    for line in inputFile:
        forwardReadIdentifier = 'forwardRead'
        startForwardReadIdentifier = line.find('N')
        print startForwardReadIdentifier
        if line[0] == 'N':
            forwardValues = line.split("\t")
            forwardReadIdentifier = forwardValues[0].strip()
            identifiers.append(forwardReadIdentifier)
            #print("forward read identifier is" + forwardReadIdentifier)
            with open(fullReverseFilePathLast500) as inputFile2:
                for line in inputFile2:
                    reverseReadIdentifier = 'reverseRead'
                    if line[0] == 'N':
                        reverseValues = line.split("\t")
                        reverseReadIdentifier = reverseValues[0].strip()
                        #print("reverse read identifier is" + reverseReadIdentifier)
                        if forwardReadIdentifier == reverseReadIdentifier:
                            print("It's a match, the identifier is: " + forwardReadIdentifier)
                            matchingIdentifiers.append(forwardReadIdentifier)
                            count += 1 
    if count == 0:
        print("")
        print("There were no matches from the 1stforward-lastreverse bp match test")
        print("")
    else:
        print("The matching identifiers of the 1stforward-lastreverse bp match test were " + str(matchingIdentifiers))
        print("")
        print("")

        
#the following code compares last 500bp in the forward strand to the first 500bp in the reverse strand
with open(fullForwardFilePathLast500) as inputFile:
    count = 0
    identifiers = ['']
    matchingIdentifiers = []
    for line in inputFile:
        forwardReadIdentifier = 'forwardRead'
        if line[0] == 'N':
            forwardValues = line.split("\t")
            forwardReadIdentifier = forwardValues[0].strip()
            identifiers.append(forwardReadIdentifier)
            #print("forward read identifier is" + forwardReadIdentifier)
            with open(fullReverseFilePathFirst500) as inputFile2:
                for line in inputFile2:
                    reverseReadIdentifier = 'reverseRead'
                    if line[0] == 'N':
                        reverseValues = line.split("\t")
                        reverseReadIdentifier = reverseValues[0].strip()
                        #print("reverse read identifier is" + reverseReadIdentifier)
                        if forwardReadIdentifier == reverseReadIdentifier:
                            print("It's a match, the identifier is: " + forwardReadIdentifier)
                            matchingIdentifiers.append(forwardReadIdentifier)
                            count += 1 
    if count == 0:
        print("There were no matches from the lastforward-1streverse bp match test")
    else:
        print("The matching identifiers of the lastforward-1streverse bp match test were " + str(matchingIdentifiers))
        print("")
        print("")          
                
                