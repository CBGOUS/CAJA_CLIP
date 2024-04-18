# findJunctions.v1.7.py
CLIP tags Around Junction Analysis (CAJA). Find patterns of target RNAs around splicing junctions from HITS-CLIP data.
Find the distance between the end/start of tags and splicing sites (SS) located on both positive and negative genomic DNA strand orientation between a given range (e.g. -50~+50, 0 representing splicing sites)

Parser for command-line options, arguments and sub-commands. Basic usage:

python3 findJunctions.v1.7.py splicesites_coordinates.txt file.bed -n 50 -o outfile_name

where splicesites_coordinates.txt is tab-delimited text containing splicing sites coordinates which is generated from GTF file by using "hisat2_extract_splice_sites.py" in hisat2 package.
file.bed is the output file of the CTK pipeline for HITS-CLIP data analysis, showing the genomic coordinate information of unique tags bound by RNA binding protein.
-n 50, the given range around splicing sites is -50nt~+50nt.
-o outfile_name, output files contain four bed-like format files (1st column: Chromosome; 2nd column: HITS-CLIP unique tag name; 3rd column: Coordinates of end/start of tag; 4th column: Coordinates of 5'SS/3'SS) and four txt files (1st column: Frequency of occurrence of tags at each site; 2nd: Genomic distance between tag and SS, 0 representing SS).

outfile_name.pos.junc.1.bed: HITS-CLIP tags around 5'SS on positive genomic DNA strand orientation, values in the 3rd column are coordinates of the end of tags, and values in the 4th column are coordinates of 5'SS <br />
outfile_name.pos.junc.2.bed: HITS-CLIP tags around 3'SS on positive genomic DNA strand orientation, values in the 3rd column are coordinates of the start of tags, and values in the 4th column are coordinates of 3'SS <br />
outfile_name.neg.junc.1.bed: HITS-CLIP tags around 3'SS on negative genomic DNA strand orientation, values in the 3rd column are coordinates of the end of tags, and values in the 4th column are coordinates of 3'SS <br />
outfile_name.neg.junc.2.bed: HITS-CLIP tags around 5'SS on negative genomic DNA strand orientation, values in the 3rd column are coordinates of the start of tags, and values in the 4th column are coordinates of 5'SS <br />

The summary of the distance between the end/start of tags and splicing sites on either positive or negative DNA strand orientation and their read counts:

outfile_name.pos.junc.1.summary.txt <br />
outfile_name.pos.junc.2.summary.txt <br />
outfile_name.neg.junc.1.summary.txt <br />
outfile_name.neg.junc.2.summary.txt <br />

When above outfiles are used for plotting, for 5'SS plotting, pool outfile_name.pos.junc.1.summary.txt and outfile_name.neg.junc.2.summary.txt; for 3'SS plotting, pool outfile_name.pos.junc.2.summary.txt and outfile_name.neg.junc.1.summary.txt. The plotting is done using matplotlib in jupyter notebook.
