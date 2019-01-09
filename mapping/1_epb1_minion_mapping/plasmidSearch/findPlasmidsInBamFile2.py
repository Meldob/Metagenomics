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
            count_1st5001stVSlast5002nd = 0
            count_last5001stVS1st5002nd = 0
            
            #creates list for matching identifiers
            matches_1st5001stVSlast5002nd = []
            matches_last5001stVS1st5002nd = []
            #for each entry in the first read lists, find if it matches to a corresponding second read
            for firstRead in first5001st2ReadList:
                for secondRead in last5002nd1ReadList:
                    if firstRead == secondRead:
                        count =+ 1
                        print("It's a match, the identifier is: " + firstRead)
                        matches_1st5001stVSlast5002nd.append(firstRead)
            for firstRead in last5001st1ReadList:
                for secondRead in first5002nd2ReadList:
                    if firstRead == secondRead:
                        count =+ 1
                        print("It's a match, the identifier is: " + firstRead)
                        matches_last5001stVS1st5002nd.append(firstRead)            
            #If there are no matches, report this
            if count_1st5001stVSlast5002nd == 0:
                print("")
                print("There were no matches comparing first reads from the first 500bp with the 2nd reads form the last 500bp")
                print("")
            #print the matching list of identifiers
            else:
                print("The matching identifiers when comparing first reads from the first 500bp with the 2nd reads from the last 500bp are: " + str(matches_1st5001stVSlast5002nd))
                print("")
                print("")
            #If there are no matches, report this
            if count_last5001stVS1st5002nd == 0:
                print("")
                print("There were no matches comparing first reads from the last 500bp with the 2nd reads from the first 500bp")
                print("")
            #print the matching list of identifiers
            else:
                print("The matching identifiers when comparing first reads from the last 500bp with the 2nd reads from the first 500bp are: " + str(matches_1st5001stVSlast5002nd))
                print("")
                print("")    
            

samfile.close



