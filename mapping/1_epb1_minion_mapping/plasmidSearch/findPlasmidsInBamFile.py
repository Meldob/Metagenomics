#!/usr/bin/env python2


#changeable element
inputFile = "AcetobacterPasteurianus.bam/final.contigs.fa.AcetobacterPasteurianus.1.fq.bam"


import pysam

#opens bam file for reading
samfile = pysam.AlignmentFile(inputFile, "rb")

#create dictionary to store names and length of all contigs
contigRefDict = {}
#iterate through lines to find all contigs
for line in samfile:
    contigIdentifier = line.reference_name
    #if the contiIdentifier isn't already in the dictionary, then add it
    if contigIdentifier not in contigRefDict:
        contigLength = samfile.lengths[samfile.get_tid(contigIdentifier)]
        contigRefDict[contigIdentifier] = contigLength
    #find reads associated with first 500bp of contig
    iter = samfile.fetch(str(ref), 1, 500)
    #of these reads, find those that are the first read and are reverse mapped
    #then find those reads that are the second read and are reverse mapped
    
    #find reads associated with last 500bp of contig
    #of these reads, find those that are the first read and are forward mapped
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



