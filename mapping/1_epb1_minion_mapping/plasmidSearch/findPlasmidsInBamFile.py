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
                        last5001st2ReadList.append(queryName)
                    #include those that are second reads
                    if read.is_secondary:
                        last5002nd2ReadList.append(queryName)
        print('Results for the contig: ' + contigIdentifier)
        print('First 500bp, first read, reverse mapping list is: ' + str(first5001st2ReadList))
        print('First 500bp, second read, reverse mapping list is: ' + str(first5002nd2ReadList))
        print('Last 500bp, first read, forward mapping list is: ' + str(last5001st1ReadList))
        print('Last 500bp, second read, forward mapping list is: ' + str(last5002nd1ReadList))
    
            
    
    #then find those reads that are the second read and are forward mapped
    
    
print(contigRefDict)
        

        
#        line.get_reference_length(self, ref)
#print(contigRefList)   


#for ref in contigRefList:
#    print(ref)
#    print(line.get_reference_length(self, ref))
    #
    #for x in iter:
    #    print (str(x))
        
    
    
    
    #import IPython; IPython.embed()
    #create a list of each of the values in the line containing a forward identifier, separated by a tab
    #values = read.split("\t")
    #print(values[0])
    #contigIdentifier = values[3].strip
    #print contigIdentifier
#find contig name
# if not in list, add to list

#iterate through contigs using the following code, but replace k99_1 with whatever contig is relevant

#iter = samfile.fetch("k99_1", 1, 500)
#for x in iter:
#    print (str(x))
    

samfile.close



