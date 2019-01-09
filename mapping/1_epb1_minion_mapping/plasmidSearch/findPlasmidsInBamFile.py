#!/usr/bin/env python2


#changeable element
inputFile = "AcetobacterPasteurianus.bam/final.contigs.fa.AcetobacterPasteurianus.1.fq.bam"


import pysam

#opens bam file for reading
samfile = pysam.AlignmentFile(inputFile, "rb")

#create dictionary to store names and length of all contigs
contigRefDict = {}
first5001st2ReadList = []
first5002nd2ReadList = []    
last5001st1ReadList = []
last5002nd1ReadList = []
#iterate through lines to find all contigs
for line in samfile:
    contigIdentifier = line.reference_name
    #if the contiIdentifier isn't already in the dictionary, then add it
    if contigIdentifier not in contigRefDict:
        contigLength = samfile.lengths[samfile.get_tid(contigIdentifier)]
        contigRefDict[contigIdentifier] = contigLength
        #checks that contig is > 1000bp
        if contigLength > 1000:
            #find reads associated with first 500bp of contig
            first500Reads = samfile.fetch(str(contigIdentifier), 1, 500)
            for read in first500Reads:
                queryName = read.query_name
                #exclude those reads that are forward mapped
                if read.is_reverse:
                    #include those that are first reads
                    if not read.is_secondary:            
                        first5001st2ReadList.append(queryName)
                    #include those that are second reads
                    if read.is_secondary:
                        first5002nd2ReadList.append(queryName)
            #find reads associated with last 500bp of contig
            last500Reads = samfile.fetch(str(contigIdentifier), (contigLength-500), contigLength)
            for read in last500Reads:
                queryName = read.query_name
                #include those that are forward mapped
                if not read.is_reverse:
                    #include those that are first reads
                    if not read.is_secondary:            
                        last5001st1ReadList.append(queryName)
                    #include those that are second reads
                    if read.is_secondary:
                        last5002nd1ReadList.append(queryName)
            print('Results for the contig: ' + contigIdentifier)
            print('First 500bp, first read, reverse mapping list is: ' + str(first5001st2ReadList))
            print('')
            print('First 500bp, second read, reverse mapping list is: ' + str(first5002nd2ReadList))
            print('')
            print('Last 500bp, first read, forward mapping list is: ' + str(last5001st1ReadList))
            print('')
            print('Last 500bp, second read, forward mapping list is: ' + str(last5002nd1ReadList))
            print('')
            #starts count for number of matches
            count = 0
            #creates list for identifiers
            identifiers = ['']
            #creates list for matching identifiers
            matchingIdentifiers = []

            #for each entry in the first read lists, find if it matches to a corresponding second read
            matches = []
            for firstRead in first5001st2ReadList:
                for secondRead in last5002nd1ReadList:
                    if firstRead == secondRead:
                        count =+ 1
                        print("It's a match, the identifier is: " + firstRead)
                        matches.append(firstRead)
            for firstRead in last5001st1ReadList:
                for secondRead in first5002nd2ReadList:
                    if firstRead == secondRead:
                        count =+ 1
                        print("It's a match, the identifier is: " + firstRead)
                        matches.append(firstRead)            
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

samfile.close

### COMPARE FORWARD AND REVERSE READS TO SEE IF THERE IS OVERLAP





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



