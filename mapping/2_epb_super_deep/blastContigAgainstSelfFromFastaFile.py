#!/usr/bin/env python2

import extern

# This script takes an input fasta file and blasts the first 500bp against the last 500bp
# It is thought that when the genome of a plasmid is assembled the start and ends will show overlap
# This is because a plasmid is circular and when represented as a linear sequence, the assembler cannot recognise this and will produce overlap as a result
# This hypothesis has been tested by simulating known plasmids, reassembling them and finding this overlap

#Notes
#1/ This file is made to read a file in this format:
    # >k141_1 flag=1 multi=4.0000 len=320
    # CCGTGCTCGACGTGCTCGTGGTCACCGTCCTGCTCGTCGGCTCGGTGCAGTGGGGGCGAGGTCGCTGGCACATCCACGGCACCGGTCGGCGCATCGCTCTCGTGGTGAGCGCCGTGGCAGTGGTCGTGGCCGTTCCCACCCTG
    # >k141_2 flag=1 multi=4.0000 len=320
    # CCGTGCTCGACGTGCTCGTGGTCACCGTCCTGCTCGTCGGCTCGGTGCAGTGGGGGCGAGGTCGCTGGCACATCCACGGCACCGGTCGGCGCATCGCTCTCGTGGTGAGCGCCGTGGCAGTGGTCGTGGCCGTTCCCACCCTG
#2/ The module 'extern' must be loaded on the terminal by typing 'module load extern'
#3/ The module 'blast' must be loaded on the terminal by typing 'module load blast'
#4/ Place the fasta file that you wish to analyse for plasmids as the variable 'fastaFileInput'
    
fastaFileInput = '/srv/projects/abisko/assemblies/84_epb_super_deep/megahit_out/final.contigs.fa'

#open the file of interest
with open(fastaFileInput) as inputFile:
    commandLineString = ''
    #loop through each line
    for line in inputFile:
        # checks if the line is an identifier line
        if line[0] == '>':
            # assigns the sequence on the next line to the variable 'sequence'
            sequence = (next(inputFile)).strip()
            # finds the length of the sequence
            length = len(sequence.strip())
            if length > 1000:
                #finds the start and end of the identifier number
                identifierStartingPoint = line.find('k')
                identifierEndingPoint = line.find(' ')
                identifier = ((line[identifierStartingPoint:identifierEndingPoint]).strip())
                #find sequences that will be compared
                first500 = (sequence[:500]).strip()
                last500 = (sequence[(length-500):]).strip()
                command = 'blastn -task blastn -outfmt 6 -query <(echo ">' + identifier + '\n"' + first500 + ') -subject <(echo ">' + identifier + '\n"' + last500 + ')'
                output = extern.run(command)
                print('new contig')
                print(output)
                