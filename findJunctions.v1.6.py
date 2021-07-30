#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Friday, 16 July 2021 at 10:36

@author: siqing-liu
"""


import argparse
parser = argparse.ArgumentParser()
parser.add_argument('splicefile', type=argparse.FileType('r'), help='splicesites file')
parser.add_argument('bedfile', type=argparse.FileType('r'), help='bed file')
parser.add_argument('-n', dest='nucleotides', help='specifying absolute distance to splicing sites')
parser.add_argument('-o', dest='outfile', help='name of output files')

args = parser.parse_args()
splicefile = args.splicefile
bedfile = args.bedfile
D = int(args.nucleotides)
outfile = args.outfile

import pandas as pd
import numpy as np
import os

#transfer splicesites file into DataFrame with index column of strand, and split DataFrame into two by strand
dat = pd.read_csv(splicefile, sep='\t', header=None, dtype={0: object}, index_col=3)
dat.columns = ['chro', 'start', 'end']
dat = dat.sort_values(['chro'])
datPos = dat.loc['+', :]
datNeg = dat.loc['-', :]
#load splicesites file to a dict; set column "chro" as key, and column "start" as value
datPos_dict = datPos.groupby('chro').start.apply(list).to_dict()
datPos_dict2 = datPos.groupby('chro').end.apply(list).to_dict()
datNeg_dict = datNeg.groupby('chro').start.apply(list).to_dict()
datNeg_dict2 = datNeg.groupby('chro').end.apply(list).to_dict()

#split unique target bed file into two DataFrame by strand
tagBed = pd.read_csv(bedfile, sep='\t', header=None, index_col=5)
tagBed = tagBed.sort_values([0])
tagBedPos = tagBed.loc['+', :]
tagBedNeg = tagBed.loc['-', :]
print(tagBedPos)
print(tagBedNeg)

junctionsPos = open(outfile + '.pos.junc.1.bed','w')
junctionsPos2 = open(outfile + '.pos.junc.2.bed','w')
junctionsNeg= open(outfile + '.neg.junc.1.bed','w')
junctionsNeg2 = open(outfile + '.neg.junc.2.bed','w')
summaryP = open(outfile + '.pos.junc.1.summary.txt','w')
summaryP2 = open(outfile + '.pos.junc.2.summary.txt','w')
summaryN = open(outfile + '.neg.junc.1.summary.txt','w')
summaryN2 = open(outfile + '.neg.junc.2.summary.txt','w')


with open('distances.txt', 'w') as d1, open('distances2.txt', 'w') as d2, open('distances3.txt', 'w')as d3, open('distances4.txt', 'w') as d4:

    # iterate over DataFrame rows as namedtuples, with index value as first element of the tuple.
    for row in tagBedPos.itertuples(index=True, name='Pandas'):
        readName = row[4]
    #    print(readName)
        readEnd = row[3]
        readStart = row[2]
        chromosome = row[1]
    #    print(chromosome)
    #    print(readEnd)
        #restrict the name of chromosom of tags in the list of chromosome where splicing sites located, avoiding "TypeError: 'NoneType' object is not iterable"
        if chromosome in dat.loc[:, 'chro'].tolist():
            #find a key by using chromosome name, and iterate the values in the key; only consider unique coordinates
            splice_record = set(datPos_dict.get(chromosome))
            #print(splice_record)
            for intronPos_start in splice_record:
                distance = abs(readEnd - intronPos_start)
                distance_range = readEnd - intronPos_start
                if distance < D+1:
                    junctionsPos.write(str(chromosome) + "\t" + readName + "\t" + str(readEnd) + "\t" + str(intronPos_start) + "\n")
                if distance_range >= -D:
                    if distance_range <= D:
                        d1.write(str(distance_range) + "\n")

            splice_record2 = set(datPos_dict2.get(chromosome))
            for intronPos_end in splice_record2:
                distance2 = abs(readStart - intronPos_end)
                #change readEnd to readStart when calculating junction2 in version 1.6
                distance2_range = readStart - intronPos_end
                if distance2 < D + 1:
                    junctionsPos2.write(
                        str(chromosome) + "\t" + readName + "\t" + str(readStart) + "\t" + str(intronPos_end) + "\n")
                if distance2_range >= -D:
                    if distance2_range <= D:
                        d2.write(str(distance2_range) + "\n")

    #change tagBedPos to tagBedNeg in version 1.5
    for rowN in tagBedNeg.itertuples(index=True, name='Pandas'):
        readNameN = rowN[4]
        #    print(readNameN)
        chromosomeN = rowN[1]
        readEndN = rowN[3]
        readStartN = rowN[2]
        #    print(chromosomeN)
        #    print(readEndN)
        if chromosomeN in dat.loc[:, 'chro'].tolist():
            splice_recordN = set(datNeg_dict.get(chromosomeN))
            for intronNeg_start in splice_recordN:
                distance3 = abs(readEndN - intronNeg_start)
                distance3_range = readEndN - intronNeg_start
                if distance3 < D + 1:
                    junctionsNeg.write(
                        str(chromosomeN) + "\t" + readNameN + "\t" + str(readEndN) + "\t" + str(intronNeg_start) + "\n")
                if distance3_range >= -D:
                    if distance3_range <= D:
                        d3.write(str(distance3_range) + "\n")

            splice_recordN2 = set(datNeg_dict2.get(chromosomeN))
            for intronNeg_end in splice_recordN2:
                distance4 = abs(readStartN - intronNeg_end)
                distance4_range = readStartN - intronNeg_end
                if distance4 < D + 1:
                    junctionsNeg2.write(
                        str(chromosomeN) + "\t" + readNameN + "\t" + str(readStartN) + "\t" + str(intronNeg_end) + "\n")
                if distance4_range >= -D:
                    if distance4_range <= D:
                        d4.write(str(distance4_range) + "\n")


a = np.array(pd.read_csv('distances.txt', header=None))
unique_elements, counts_elements = np.unique(a, return_counts=True)
uniqa = pd.DataFrame(unique_elements, counts_elements)
summaryP.write(uniqa.to_string(header=False))

a = np.array(pd.read_csv('distances2.txt', header=None))
unique_elements, counts_elements = np.unique(a, return_counts=True)
uniqa = pd.DataFrame(unique_elements, counts_elements)
summaryP2.write(uniqa.to_string(header=False))

a = np.array(pd.read_csv('distances3.txt', header=None))
unique_elements, counts_elements = np.unique(a, return_counts=True)
uniqa = pd.DataFrame(unique_elements, counts_elements)
summaryN.write(uniqa.to_string(header=False))

a = np.array(pd.read_csv('distances4.txt', header=None))
unique_elements, counts_elements = np.unique(a, return_counts=True)
uniqa = pd.DataFrame(unique_elements, counts_elements)
summaryN2.write(uniqa.to_string(header=False))

os.remove('distances.txt')
os.remove('distances2.txt')
os.remove('distances3.txt')
os.remove('distances4.txt')

junctionsPos.close()
junctionsPos2.close()
junctionsNeg.close()
junctionsNeg2.close()
summaryP.close()
summaryP2.close()
summaryN.close()
summaryN2.close()