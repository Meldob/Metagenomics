#!/usr/bin/env python2

#import relevant modules
import pysam
import argparse

parser = argparse.ArgumentParser(description='Find plasmids within a bam file.')
parser.add_argument('-inputFilePath', '-input', '-i', action = 'store', help = 'the bam input file')
parser.add_argument('-outputFilePath', '-output', '-o', action = 'store', help = 'the output')
args = parser.parse_args()
dict = vars(args)
inputFile = str(dict.get("inputFilePath"))
outputFile = str(dict.get("outputFilePath"))
print inputFile
print outputFile

#changeable element
#inputFile = "brassica_napus_plasmid.fixed.bam/final.contigs.fa.brassica_napus_plasmid.fixed.1.fq.bam"
#inputFile = "AcetobacterPasteurianus.bam/final.contigs.fa.AcetobacterPasteurianus.1.fq.bam"
#inputFile = "nostoc_azollae_plasmid.fixed.bam/final.contigs.fa.nostoc_azollae_plasmid.fixed.1.fq.bam"


#please note for ease of naming conventions, the reads that are to be compared are going to be referred to as follows:
# - first500bp, first read, reverse read = readListA1
# - last500bp, second read, forward read = readListA2
# - first500bp, second read, reverse read = readListB1
# - last500bp, first read, forward read = readListB2

#Write a new file
newFile = open(outputFile, "w")

#opens bam file for reading
samfile = pysam.AlignmentFile(inputFile, "rb")

#create dictionary to store names and length of all contigs
contigRefDict = {}
plasmidList = []

#iterate through lines to find all contigs
readCount = 0
for line in samfile:
    contigIdentifier = line.reference_name
    #if the contiIdentifier isn't already in the dictionary, then add it
    if contigIdentifier not in contigRefDict:
        readListA1 = []
        readListA2 = []
        readListB1 = []    
        readListB2 = []
        contigLength = samfile.lengths[samfile.get_tid(contigIdentifier)]
        contigRefDict[contigIdentifier] = contigLength
        #create list of contigs that are likely to be plasmids
        #checks that contig is > 1000bp
        if contigLength > 1000:
            #find reads associated with first 500bp of contig
            first500Reads = samfile.fetch(str(contigIdentifier), 1, 500)
            for read in first500Reads:
                queryName = read.query_name
                #exclude those reads that are forward mapped
                if read.is_reverse:
                    #include those that are first reads
                    if read.is_read1:            
                        readListA1.append(queryName)
                    #include those that are second reads
                    if read.is_read2:
                        readListB1.append(queryName)
            #find reads associated with last 500bp of contig
            last500Reads = samfile.fetch(str(contigIdentifier), (contigLength-500), contigLength)
            for read in last500Reads:
                queryName = read.query_name
                #include those that are forward mapped
                if read.mate_is_reverse:
                    #include those that are first reads
                    if read.is_read1:
                        readListB2.append(queryName)
                    #include those that are second reads
                    if read.is_read2:
                        readListA2.append(queryName)
            newFile.write('Results for the contig: ' + contigIdentifier)
            newFile.write('First 500bp, first read, reverse mapping list is: ' + str(readListA1))
            newFile.write('')
            newFile.write('First 500bp, second read, reverse mapping list is: ' + str(readListB1))
            newFile.write('')
            newFile.write('Last 500bp, first read, forward mapping list is: ' + str(readListB2))
            newFile.write('')
            newFile.write('Last 500bp, second read, forward mapping list is: ' + str(readListA2))
            newFile.write('')
            #starts count for number of matches
            count_readListA = 0
            count_readListB = 0
            
            #creates list for matching identifiers
            matches_readListA = []
            matches_readListB = []
            #for each entry in the first read lists, find if it matches to a corresponding second read
            for firstRead in readListA1:
                for secondRead in readListA2:
                    if firstRead == secondRead:
                        count_readListA =+ 1
                        newFile.write("It's a match, the identifier is: " + firstRead)
                        matches_readListA.append(firstRead)
            for firstRead in readListB1:
                for secondRead in readListB2:
                    if firstRead == secondRead:
                        count_readListB =+ 1
                        newFile.write("It's a match, the identifier is: " + firstRead)
                        matches_readListB.append(firstRead)            
            #If there are no matches, report this
            if count_readListA == 0:
                newFile.write("")
                newFile.write("There were no matches comparing first reads from the first 500bp with the 2nd reads form the last 500bp")
                newFile.write("")
            #print the matching list of identifiers
            else:
                newFile.write("The matching identifiers when comparing first reads from the first 500bp with the 2nd reads from the last 500bp are: " + str(matches_readListA))
                newFile.write("")
                newFile.write("")
            #If there are no matches, report this
            if count_readListB == 0:
                newFile.write("")
                newFile.write("There were no matches comparing first reads from the last 500bp with the 2nd reads from the first 500bp")
                newFile.write("")
            #print the matching list of identifiers
            else:
                newFile.write("The matching identifiers when comparing first reads from the last 500bp with the 2nd reads from the first 500bp are: " + str(matches_readListB))
                newFile.write("")
                newFile.write("")
            #create list of contigs
            if contigIdentifier not in plasmidList:
                if count_readListA or count_readListB >0:
                    plasmidList.append(contigIdentifier)
    readCount += 1
    print("read " + str(readCount) + " processed")                
    
#Report which contigs are likely to be plasmids
newFile.write('It is likely that the following contigs are plasmids: ' + str(plasmidList))
        



        
samfile.close