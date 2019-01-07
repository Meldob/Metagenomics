#!/usr/bin/env python2


#changeable element
inputFile = "AcetobacterPasteurianus.bam/final.contigs.fa.AcetobacterPasteurianus.1.fq.bam"


import pysam

#opens bam file for reading
samfile = pysam.AlignmentFile(inputFile, "rb")

#iterate through lines
for read in samfile:
    #print(read)
    #create a list of each of the values in the line containing a forward identifier, separated by a tab
    values = read.split("\t")
    print(values[0])
    #contigIdentifier = values[3].strip
    #print contigIdentifier
#find contig name
# if not in list, add to list

#iterate through contigs using the following code, but replace k99_1 with whatever contig is relevant

#iter = samfile.fetch("k99_1", 1, 500)
#for x in iter:
#    print (str(x))
    
    
samfile.close



