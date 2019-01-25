#!/usr/bin/env python

#PLEASE NOTE: you must module load extern and pysam before using this test
# module load extern
# 

import unittest
import extern
import os.path

path_to_script = 'srv/projects/abisko/melody/mapping/1_epb1_minion_mapping/plasmidSearch/findPlasmidScript/findPlasmidsInBamFile/findPlasmidsInBamFile.py'

class TestStringMethods(unittest.TestCase):
    
    
    def testBrassica(self):
        brassicaCommand = path_to_script + ' -i srv/projects/abisko/melody/mapping/1_epb1_minion_mapping/plasmidSearch/findPlasmidScript/test/data/final.contigs.fa.brassica_napus_plasmid.fixed.1.fq.bam -o /dev/stdout'
        brassicaContents = (extern.run(brassicaCommand)).strip()
        
        expectedBrassicaOutput = "contigName" + "\t" + "numberOfMatches" + "\t" + "matchingReads" + "\n" + "k99_1" + "\t" + "33" + "\t" +"['NC_016583.1_911_1381_2:0:0_3:0:0_3c', 'NC_016583.1_914_1401_1:0:0_1:0:0_8c', 'NC_016583.1_866_1302_7:0:0_5:0:0_c4', 'NC_016583.1_865_1343_3:0:0_4:0:0_1b', 'NC_016583.1_811_1353_2:0:0_3:0:0_38', 'NC_016583.1_797_1311_7:0:0_7:0:0_df', 'NC_016583.1_784_1255_4:0:0_3:0:0_48', 'NC_016583.1_766_1233_0:0:0_5:0:0_35', 'NC_016583.1_751_1329_3:0:0_2:0:0_90', 'NC_016583.1_729_1239_3:0:0_6:0:0_25', 'NC_016583.1_701_1212_2:0:0_4:0:0_ce', 'NC_016583.1_698_1190_3:0:0_3:0:0_84', 'NC_016583.1_690_1134_5:0:0_0:0:0_d0', 'NC_016583.1_684_1129_4:0:0_8:0:0_ae', 'NC_016583.1_683_1201_4:0:0_1:0:0_b8', 'NC_016583.1_676_1213_5:0:0_3:0:0_55', 'NC_016583.1_619_1076_4:1:0_7:0:0_cf', 'NC_016583.1_918_1409_1:0:0_3:0:0_e', 'NC_016583.1_896_1422_2:0:0_6:0:0_de', 'NC_016583.1_888_1365_3:0:0_5:0:0_65', 'NC_016583.1_886_1386_2:0:0_3:0:0_a7', 'NC_016583.1_874_1418_2:0:0_3:0:0_1a', 'NC_016583.1_867_1401_5:0:0_2:0:0_64', 'NC_016583.1_844_1349_2:0:0_3:0:0_3e', 'NC_016583.1_772_1286_3:0:0_2:0:0_47', 'NC_016583.1_757_1280_8:0:0_2:0:0_61', 'NC_016583.1_725_1191_2:0:0_5:0:0_32', 'NC_016583.1_656_1133_4:0:0_4:0:0_ad', 'NC_016583.1_651_1160_2:1:0_1:0:0_ac', 'NC_016583.1_622_1182_2:1:0_3:0:0_b6', 'NC_016583.1_613_1091_0:1:0_4:0:0_10', 'NC_016583.1_567_1140_2:1:0_1:0:0_78', 'NC_016583.1_550_1076_2:1:0_3:0:0_28']"
        expectedBrassicaOutput = expectedBrassicaOutput.strip()

        print ""
        print("expected brassica output: " + str(expectedBrassicaOutput))
        print ""
        print("actual brassica output: " + str(brassicaContents))
        print ""
        
        self.assertEqual(expectedBrassicaOutput, brassicaContents)
    
    def testNostoc(self):        
        #set the output file
        #set the command to check
        nostocCommand = path_to_script + ' -i srv/projects/abisko/melody/mapping/1_epb1_minion_mapping/plasmidSearch/findPlasmidScript/test/data/final.contigs.fa.nostoc_azollae_plasmid.fixed.1.fq.bam -o /dev/stdout'
        # run the test command and put the output into the variable nostocContents
        nostocContents = (extern.run(nostocCommand)).strip()
        
        expectedNostocOutput = "contigName\tnumberOfMatches\tmatchingReads\nk141_2\t49\t['NC_014250.1_14756_15181_5:0:0_3:0:0_296', 'NC_014250.1_14751_15216_4:0:0_5:0:0_58d', 'NC_014250.1_14736_15223_3:0:0_6:0:0_4b', 'NC_014250.1_14733_15224_3:0:0_2:0:0_51e', 'NC_014250.1_14762_15234_5:0:0_3:0:0_58e', 'NC_014250.1_14784_15254_1:0:0_2:0:0_2dc', 'NC_014250.1_14771_15254_1:0:0_2:0:0_404', 'NC_014250.1_14809_15281_3:0:0_2:0:0_2fa', 'NC_014250.1_19398_19872_6:0:0_6:0:0_3c4', 'NC_014250.1_19415_19893_5:0:0_3:0:0_2b9', 'NC_014250.1_14870_15370_4:0:0_3:0:0_451', 'NC_014250.1_14836_15373_4:0:0_2:0:0_3c0', 'NC_014250.1_19541_19967_2:0:0_4:0:0_3ef', 'NC_014250.1_14866_15402_1:0:0_1:0:0_35b', 'NC_014250.1_19500_19996_2:0:0_6:0:0_591', 'NC_014250.1_14863_15436_3:0:0_3:0:0_469', 'NC_014250.1_14928_15439_2:0:0_2:0:0_337', 'NC_014250.1_14909_15444_3:0:0_5:0:0_4b3', 'NC_014250.1_14976_15458_3:0:0_4:0:0_47b', 'NC_014250.1_14977_15488_3:0:0_3:0:0_2f3', 'NC_014250.1_19480_20093_3:0:0_4:0:0_13e', 'NC_014250.1_19528_20097_5:0:0_5:0:0_575', 'NC_014250.1_14750_15179_2:0:0_2:0:0_199', 'NC_014250.1_19241_19772_3:0:0_0:0:0_28c', 'NC_014250.1_14740_15197_5:0:0_2:0:0_1b7', 'NC_014250.1_14788_15208_6:0:0_4:0:0_3c5', 'NC_014250.1_19385_19808_4:0:0_3:0:0_1a7', 'NC_014250.1_14764_15228_0:0:0_2:0:0_1a5', 'NC_014250.1_14768_15239_5:0:0_3:0:0_115', 'NC_014250.1_19326_19830_7:0:0_6:0:0_48c', 'NC_014250.1_14796_15271_1:0:0_2:0:0_375', 'NC_014250.1_14798_15272_6:0:0_4:0:0_ea', 'NC_014250.1_14735_15284_1:0:0_0:0:0_2d6', 'NC_014250.1_19302_19873_3:0:0_2:0:0_147', 'NC_014250.1_19408_19875_1:0:0_2:0:0_324', 'NC_014250.1_19444_19878_3:0:0_2:0:0_4f8', 'NC_014250.1_19402_19891_4:0:0_6:0:0_2a6', 'NC_014250.1_19422_19913_5:0:0_3:0:0_512', 'NC_014250.1_14780_15354_5:0:0_1:0:0_19d', 'NC_014250.1_14927_15364_4:0:0_4:0:0_49e', 'NC_014250.1_19559_19970_2:0:0_2:0:0_276', 'NC_014250.1_19443_19978_3:0:0_8:0:0_3a7', 'NC_014250.1_19535_19984_2:0:0_1:0:0_3a4', 'NC_014250.1_14836_15409_2:0:0_2:0:0_59e', 'NC_014250.1_19518_19996_4:0:0_8:0:0_1a1', 'NC_014250.1_19506_20001_5:0:0_4:0:0_15a', 'NC_014250.1_19556_20024_4:0:0_3:0:0_4c5', 'NC_014250.1_14916_15476_3:0:0_6:0:0_22e', 'NC_014250.1_14920_15477_2:0:0_3:0:0_21e']"
        expectedNostocOutput = expectedNostocOutput.strip()
        
        print ""
        print("expected nostoc output: " + str(expectedNostocOutput))
        print ""
        print("actual nostoc output: " + str(nostocContents))
        print ""
        
        self.assertEqual(expectedNostocOutput, nostocContents)
    
    def testAcetobacter(self):
        acetoCommand = path_to_script + ' -i srv/projects/abisko/melody/mapping/1_epb1_minion_mapping/plasmidSearch/findPlasmidScript/test/data/final.contigs.fa.AcetobacterPasteurianus.1.fq.bam -o /dev/stdout'
        acetoContents = (extern.run(acetoCommand)).strip()
        
        expectedAcetoOutput = "contigName" + "\t" + "numberOfMatches" + "\t" + "matchingReads" + "\n" + "k141_103" + "\t" + "0" + "\t" + "[]k141_106" + "\t" + "0" + "\t" + "[]k141_153" + "\t" + "0" + "\t" + "[]k141_157" + "\t" + "0" + "\t" + "[]k141_164" + "\t" + "0" + "\t" + "[]k141_177" + "\t" + "0" + "\t" + "[]k141_183" + "\t" + "0" + "\t" + "[]k141_184" + "\t" + "0" + "\t" + "[]k141_186" + "\t" + "0" + "\t" + "[]k141_187" + "\t" + "0" + "\t" + "[]k141_196" + "\t" + "0" + "\t" + "[]k141_203" + "\t" + "0" + "\t" + "[]k141_210" + "\t" + "0" + "\t" + "[]k141_213" + "\t" + "0" + "\t" + "[]k141_230" + "\t" + "0" + "\t" + "[]k141_232" + "\t" + "0" + "\t" + "[]k141_236" + "\t" + "0" + "\t" + "[]k141_237" + "\t" + "0" + "\t" + "[]k141_238" + "\t" + "0" + "\t" + "[]k141_240" + "\t" + "0" + "\t" + "[]k141_241" + "\t" + "0" + "\t" + "[]k141_243" + "\t" + "0" + "\t" + "[]k141_246" + "\t" + "0" + "\t" + "[]k141_247" + "\t" + "0" + "\t" + "[]k141_249" + "\t" + "0" + "\t" + "[]k141_253" + "\t" + "0" + "\t" + "[]k141_254" + "\t" + "0" + "\t" + "[]k141_256" + "\t" + "0" + "\t" + "[]k141_257" + "\t" + "0" + "\t" + "[]"
        expectedAcetoOutput = expectedAcetoOutput.strip()

        print ""
        print("expected aceto output: " + str(expectedAcetoOutput))
        print ""
        print("actual aceto output: " + str(acetoContents.strip()))
        print ""
        
        self.assertEqual(expectedAcetoOutput, acetoContents)
        
if __name__ == "__main__":
	unittest.main()
    