#!/usr/bin/env python

import unittest
import extern

class TestStringMethods(unittest.TestCase):
    #def testBrassica(self):
        
    
    def testNostoc(self):        
        #set the output file
        #set the command to check
        path_to_script = './findPlasmidsInBamFile.py'
        nostocCommand = path_to_script + ' -i nostoc_azollae_plasmid.fixed.bam/final.contigs.fa.nostoc_azollae_plasmid.fixed.1.fq.bam -o /dev/stdout'
        # run the test command and put the output into the variable nostocContents
        nostocContents = extern.run(nostocCommand)
        
        expectedNostocOutput = 'contigName      numberOfMatches matchingReads'
        expectedNostocOutput += "k141_2  49      ['NC_014250.1_14756_15181_5:0:0_3:0:0_296', 'NC_014250.1_14751_15216_4:0:0_5:0:0_58d', 'NC_014250.1_14736_15223_3:0:0_6:0:0_4b', 'NC_014250.1_14733_15224_3:0:0_2:0:0_51e', 'NC_014250.1_14762_15234_5:0:0_3:0:0_58e', 'NC_014250.1_14784_15254_1:0:0_2:0:0_2dc', 'NC_014250.1_14771_15254_1:0:0_2:0:0_404', 'NC_014250.1_14809_15281_3:0:0_2:0:0_2fa', 'NC_014250.1_19398_19872_6:0:0_6:0:0_3c4', 'NC_014250.1_19415_19893_5:0:0_3:0:0_2b9', 'NC_014250.1_14870_15370_4:0:0_3:0:0_451', 'NC_014250.1_14836_15373_4:0:0_2:0:0_3c0', 'NC_014250.1_19541_19967_2:0:0_4:0:0_3ef', 'NC_014250.1_14866_15402_1:0:0_1:0:0_35b', 'NC_014250.1_19500_19996_2:0:0_6:0:0_591', 'NC_014250.1_14863_15436_3:0:0_3:0:0_469', 'NC_014250.1_14928_15439_2:0:0_2:0:0_337', 'NC_014250.1_14909_15444_3:0:0_5:0:0_4b3', 'NC_014250.1_14976_15458_3:0:0_4:0:0_47b', 'NC_014250.1_14977_15488_3:0:0_3:0:0_2f3', 'NC_014250.1_19480_20093_3:0:0_4:0:0_13e', 'NC_014250.1_19528_20097_5:0:0_5:0:0_575', 'NC_014250.1_14750_15179_2:0:0_2:0:0_199', 'NC_014250.1_19241_19772_3:0:0_0:0:0_28c', 'NC_014250.1_14740_15197_5:0:0_2:0:0_1b7', 'NC_014250.1_14788_15208_6:0:0_4:0:0_3c5', 'NC_014250.1_19385_19808_4:0:0_3:0:0_1a7', 'NC_014250.1_14764_15228_0:0:0_2:0:0_1a5', 'NC_014250.1_14768_15239_5:0:0_3:0:0_115', 'NC_014250.1_19326_19830_7:0:0_6:0:0_48c', 'NC_014250.1_14796_15271_1:0:0_2:0:0_375', 'NC_014250.1_14798_15272_6:0:0_4:0:0_ea', 'NC_014250.1_14735_15284_1:0:0_0:0:0_2d6', 'NC_014250.1_19302_19873_3:0:0_2:0:0_147', 'NC_014250.1_19408_19875_1:0:0_2:0:0_324', 'NC_014250.1_19444_19878_3:0:0_2:0:0_4f8', 'NC_014250.1_19402_19891_4:0:0_6:0:0_2a6', 'NC_014250.1_19422_19913_5:0:0_3:0:0_512', 'NC_014250.1_14780_15354_5:0:0_1:0:0_19d', 'NC_014250.1_14927_15364_4:0:0_4:0:0_49e', 'NC_014250.1_19559_19970_2:0:0_2:0:0_276', 'NC_014250.1_19443_19978_3:0:0_8:0:0_3a7', 'NC_014250.1_19535_19984_2:0:0_1:0:0_3a4', 'NC_014250.1_14836_15409_2:0:0_2:0:0_59e', 'NC_014250.1_19518_19996_4:0:0_8:0:0_1a1', 'NC_014250.1_19506_20001_5:0:0_4:0:0_15a', 'NC_014250.1_19556_20024_4:0:0_3:0:0_4c5', 'NC_014250.1_14916_15476_3:0:0_6:0:0_22e', 'NC_014250.1_14920_15477_2:0:0_3:0:0_21e']"
        
        self.assertEqual(expectedNostocOutput, nostocContents)
        
        # Check the index exists also
        self.assertEqual(True, os.path.isfile(nostocContents))

if __name__ == "__main__":
	unittest.main()
        
    
    #def testAcetobacter(self):
        
        
        
        #test commands
# ./findPlasmidsInBamFile.py -i AcetobacterPasteurianus.bam/final.contigs.fa.AcetobacterPasteurianus.1.fq.bam -o testAceto.txt
# ./findPlasmidsInBamFile.py -i nostoc_azollae_plasmid.fixed.bam/final.contigs.fa.nostoc_azollae_plasmid.fixed.1.fq.bam -o testNostoc.txt
# ./findPlasmidsInBamFile.py -i brassica_napus_plasmid.fixed.bam/final.contigs.fa.brassica_napus_plasmid.fixed.1.fq.bam -o testBrassica.txt