# findJunctions.v1.6.py
Find pattern of target RNAs around splicing junctions from CLIP-seq data.
Find distance between the end/start of tags and splicing sites on both positive and negative strands between a given range (e.g. -200~~200, 0 respresenting splicing sites)

# Parser for command-line options, arguments and sub-commands. Basic usage:

python3 findJunctions.v1.6.py splicesites_coordinates.txt file.bed -n 200 -o outfile_name

# where splicesites_coordinates.txt is tab-delimited text containing splicing sites coordinates which is generated from GTF file by using "hisat2_extract_splice_sites.py" in hisat2 package. -n 200, the given range around splicing sites is -200nt~+200nt. -o outfile_name, output files contain four bed files and four txt files:

# outfile_name.pos.junc.1.bed: bed file of CLIP tags around 5'SS on positive strand, values in the 4th column are coordinate of the end of tags, and values in the 5th column are coordinate of 5'SS 
outfile_name.pos.junc.2.bed: bed file of CLIP tags around 3'SS on positive strand, values in the 4th column are coordinate of the start of tags, and values in the 5th column are coordinate of 3'SS 
outfile_name.neg.junc.1.bed: bed file of CLIP tags around 5'SS on negative strand, values in the 4th column are coordinate of the end of tags, and values in the 5th column are coordinate of 5'SS 
outfile_name.neg.junc.2.bed: bed file of CLIP tags around 3'SS on negative strand, values in the 4th column are coordinate of the start of tags, and values in the 5th column are coordinate of 3'SS 

# The summary of the distance between the end/start of tags and splicing sites on both positive and negative strands and their read counts. They can be used for plotting:
outfile_name.pos.junc.1.summary.txt
outfile_name.pos.junc.2.summary.txt
outfile_name.neg.junc.1.summary.txt
outfile_name.neg.junc.2.summary.txt