#!/usr/bin/env python2


#changeable element
inputFile = "AcetobacterPasteurianus.bam/final.contigs.fa.AcetobacterPasteurianus.1.fq.bam"


import pysam

#opens bam file for reading
samfile = pysam.AlignmentFile(inputFile, "rb")

#create list to store names of all contigs
contigRefList = []
#iterate through lines to find all contigs
for line in samfile:
    contigIdentifier = line.reference_name    
    if contigIdentifier not in contigRefList:
        contigRefList.append(contigIdentifier)
        contigLength = samfile.lengths[samfile.get_tid(contigIdentifier)]
        print(contigIdentifier)
        print(contigLength)
        
        

        
#        line.get_reference_length(self, ref)
#print(contigRefList)   


#for ref in contigRefList:
#    print(ref)
#    print(line.get_reference_length(self, ref))
    #iter = samfile.fetch(str(ref), 1, 500)
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



