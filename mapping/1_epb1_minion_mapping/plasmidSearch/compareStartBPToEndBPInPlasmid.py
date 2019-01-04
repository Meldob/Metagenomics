#!/usr/bin/env python2

#REGULAR TEST
#filePath = ''
#forwardFileFirst500 = 'compareStartBPToEndBPInPlasmid_TestText1.txt'
#reverseFileLast500 = 'compareStartBPToEndBPInPlasmid_TestText2.txt'
#forwardFileLast500 = 'compareStartBPToEndBPInPlasmid_TestText1.txt'
#reverseFileFirst500 = 'compareStartBPToEndBPInPlasmid_TestText2.txt'

#BRASSICA PLASMID TEST
#filePath = 'brassica_napus_plasmid.fixed.bam'

#first500ReverseFirstRead = '/final.contigs.brassica.first500_firstRead_2.sam'
#last500ForwardSecondRead = '/final.contigs.brassica.last500_2ndRead_1.sam'
#first500ReverseSecondRead = '/final.contigs.brassica.first500_2ndRead_2.sam'
#last500ForwardFirstRead = '/final.contigs.brassica.last500_firstRead_1.sam'

#NOSTOC PLASMID TEST
filePath = 'nostoc_azollae_plasmid.fixed.bam'

first500ReverseFirstRead = '/final.contigs.nostoc.first500_firstRead_2.sam'
last500ForwardSecondRead = '/final.contigs.nostoc.last500_2ndRead_1.sam'
first500ReverseSecondRead = '/final.contigs.nostoc.first500_2ndRead_2.sam'
last500ForwardFirstRead = '/final.contigs.nostoc.last500_firstRead_1.sam'


#ACETOBACTER PLASMID TEST
#filePath = 'AcetobacterPasteurianus.bam'
#forwardFileFirst500 = '/final.contigs.fa.AcetobacterPasteurianus.1.fq_1st500_1.sam'
#forwardFileLast500 = '/final.contigs.fa.AcetobacterPasteurianus.1.fq_last500_1.sam'
#reverseFileLast500 = '/final.contigs.fa.AcetobacterPasteurianus.1.fq_last500_2.sam'
#reverseFileFirst500 = '/final.contigs.fa.AcetobacterPasteurianus.1.fq_1st500_2.sam'


#Creating the full file paths
fullFilePathLast500ForwardSecondRead = filePath + last500ForwardSecondRead
fullFilePathFirst500ReverseFirstRead = filePath + first500ReverseFirstRead

fullFilePathFirst500ReverseSecondRead = filePath + first500ReverseSecondRead
fullFilePathLast500ForwardFirstRead = filePath + last500ForwardFirstRead

#Defining tests
testName = 'first500ReverseFirstRead vs last500ForwardSecondRead'
testName2 = 'first500ReverseSecondRead vs last500ForwardFirstRead'

#first code compares reads making up the forward strands in the last 500bp of the assembled contig which were read second to the reads in the reverse strand that cover the first 500bp of the assembled contig that were read first

#open a pre-prepared sam file, that has included only the forward reads that were second reads in the last 500bp of the final assembled contig
with open(fullFilePathLast500ForwardSecondRead) as inputFile:
    #starts count for number of matches
    count = 0
    #creates list for identifiers
    identifiers = ['']
    #creates list for matching identifiers
    matchingIdentifiers = []
    #for each second read in the forward direction of the last 500bp of the original sam file, find if any of these reads match 1st reads in the reverse direction of the first 500bp of the original sam file
    #start by finding and recording the forward read identifier in the list
    for line in inputFile:
        #create an empty variable for the forward read identifier, find if the line has an identifier, and the starting point of this identifier
        forwardReadIdentifier = ''
        startForwardReadIdentifier = line.find('N')
        #test
        #print startForwardReadIdentifier
        if line[0] == 'N':
            #create a list of each of the values in the line containing a forward identifier, separated by a tab
            forwardValues = line.split("\t")
            #assuming the first value in the list is the forward read identifier, strip the whitespace and then add this value to the list of identifiers
            forwardReadIdentifier = forwardValues[0].strip()
            identifiers.append(forwardReadIdentifier)
            #test
            #print("forward read identifier is" + forwardReadIdentifier)
            #open a pre-prepared sam file, that has included only the reverse reads in the first 500bp of the final assembled contig
            with open(fullFilePathFirst500ReverseFirstRead) as inputFile2:
                for line in inputFile2:
                    #create an empty variable for the reverse read identifier, find if the line has an identifier
                    reverseReadIdentifier = 'reverseRead'
                    if line[0] == 'N':
                        reverseValues = line.split("\t")
                        #assuming the first value in the list is the reverse read identifier, strip the whitespace and then identify this as the reverseReadIdentifier
                        reverseReadIdentifier = reverseValues[0].strip()
                        #test
                        #print("reverse read identifier is" + reverseReadIdentifier)
                        #if the forward read identifier from inputFile is the same as the reverse read identifier from inputFile2, then print that they match and add the identifier to the matching Identifiers list
                        if forwardReadIdentifier == reverseReadIdentifier:
                            print("It's a match, the identifier is: " + forwardReadIdentifier)
                            matchingIdentifiers.append(forwardReadIdentifier)
                            #increase count of matches by 1
                            count += 1 
    
    #If there are no matches, report this
    if count == 0:
        print("")
        print("There were no matches from the " + testName + " match test")
        print("")
    #print the matching list of identifiers
    else:
        print("The matching identifiers of the " + testName + " match test were " + str(matchingIdentifiers))
        print("")
        print("")

        
#open a pre-prepared sam file, that has included only the forward reads that were second reads in the last 500bp of the final assembled contig
with open(fullFilePathLast500ForwardFirstRead) as inputFile:
    #starts count for number of matches
    count = 0
    #creates list for identifiers
    identifiers = ['']
    #creates list for matching identifiers
    matchingIdentifiers = []
    #for each second read in the forward direction of the last 500bp of the original sam file, find if any of these reads match 1st reads in the reverse direction of the first 500bp of the original sam file
    #start by finding and recording the forward read identifier in the list
    for line in inputFile:
        #create an empty variable for the forward read identifier, find if the line has an identifier, and the starting point of this identifier
        forwardReadIdentifier = ''
        startForwardReadIdentifier = line.find('N')
        #test
        #print startForwardReadIdentifier
        if line[0] == 'N':
            #create a list of each of the values in the line containing a forward identifier, separated by a tab
            forwardValues = line.split("\t")
            #assuming the first value in the list is the forward read identifier, strip the whitespace and then add this value to the list of identifiers
            forwardReadIdentifier = forwardValues[0].strip()
            identifiers.append(forwardReadIdentifier)
            #test
            #print("forward read identifier is" + forwardReadIdentifier)
            #open a pre-prepared sam file, that has included only the reverse reads in the first 500bp of the final assembled contig
            with open(fullFilePathFirst500ReverseSecondRead) as inputFile2:
                for line in inputFile2:
                    #create an empty variable for the reverse read identifier, find if the line has an identifier
                    reverseReadIdentifier = 'reverseRead'
                    if line[0] == 'N':
                        reverseValues = line.split("\t")
                        #assuming the first value in the list is the reverse read identifier, strip the whitespace and then identify this as the reverseReadIdentifier
                        reverseReadIdentifier = reverseValues[0].strip()
                        #test
                        #print("reverse read identifier is" + reverseReadIdentifier)
                        #if the forward read identifier from inputFile is the same as the reverse read identifier from inputFile2, then print that they match and add the identifier to the matching Identifiers list
                        if forwardReadIdentifier == reverseReadIdentifier:
                            print("It's a match, the identifier is: " + forwardReadIdentifier)
                            matchingIdentifiers.append(forwardReadIdentifier)
                            #increase count of matches by 1
                            count += 1 
    
    #If there are no matches, report this
    if count == 0:
        print("")
        print("There were no matches from the " + testName2 + " match test")
        print("")
    #print the matching list of identifiers
    else:
        print("The matching identifiers of the " + testName2 + " match test were " + str(matchingIdentifiers))
        print("")
        print("")