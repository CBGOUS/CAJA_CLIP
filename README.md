<<<<<<< HEAD
# CLIP tags Around Junction Analysis (CAJA)
### Investigate patterns of target RNAs bound by RNA Binding Protein (RBP) around splicing junctions from HITS-CLIP data.
=======
# findJunctions.v1.7.py
CLIP tags Around Junction Analysis (CAJA). Find patterns of target RNAs around splicing junctions from HITS-CLIP data.
Find the distance between the end/start of tags and splicing sites (SS) located on both positive and negative genomic DNA strand orientation between a given range (e.g. -50~+50, 0 representing splicing sites)
>>>>>>> 194833d94207b69561c512e4f967e9e603968424

#### CAJA consists of two programs: 
- findJunctions.v1.7.py
- plotFrequency.ipynb

<<<<<<< HEAD
#### findJunctions.v1.7.py
Compute the genomic distance between the end/start of HIST-CLIP tags and splicing sites (SS) which are located on both positive and negative genomic DNA strand orientation between a given range (e.g. -50~+50, 0 representing splicing sites).<br />

A parser for command-line options, arguments and sub-commands. Basic usage of findJunctions.v1.7.py:<br />

```console
python3 findJunctions.v1.7.py splicesites_coordinates.txt file.bed -n 50 -o outfile_name
```

- splicesites_coordinates.txt: tab-delimited text containing splicing sites coordinates which is generated from GTF file by using "hisat2_extract_splice_sites.py" in hisat2 package.
- file.bed: the output bed file of the [CTK pipeline](https://github.com/chaolinzhanglab/ctk) for HITS-CLIP data analysis. It provides genomic coordinate information for unique tags bound by RNA-binding proteins.
- -n 50: the given range around splicing sites is -50nt~+50nt.
- -o outfile_name: output files contain four bed-like format files and four summary txt files.

<br />

Output files (bed-like files):<br />

The genomic distance between the end/start of tags and splicing sites in a given nucleiotide window. The 1st column: Chromosome; the 2nd column: HITS-CLIP unique tag name; the 3rd column: Coordinates of end/start of tag; the 4th column: Coordinates of 5'SS/3'SS.

- outfile_name.pos.junc.1.bed: HITS-CLIP tags around 5'SS on positive genomic DNA strand orientation, values in the 3rd column are coordinates of the end of tags, and values in the 4th column are coordinates of 5'SS.
- outfile_name.pos.junc.2.bed: HITS-CLIP tags around 3'SS on positive genomic DNA strand orientation, values in the 3rd column are coordinates of the start of tags, and values in the 4th column are coordinates of 3'SS.
- outfile_name.neg.junc.1.bed: HITS-CLIP tags around 3'SS on negative genomic DNA strand orientation, values in the 3rd column are coordinates of the end of tags, and values in the 4th column are coordinates of 3'SS.
- outfile_name.neg.junc.2.bed: HITS-CLIP tags around 5'SS on negative genomic DNA strand orientation, values in the 3rd column are coordinates of the start of tags, and values in the 4th column are coordinates of 5'SS.

<br />

Output files (summary txt files):<br />

The summary of the distance between the end/start of tags and splicing sites and their read counts. The following four files are generated based on coordinated in the four bed-like files above, respectively. The 1st column: Count of tags at each site; the 2nd column: Genomic distance between tag and SS, 0 representing SS:

- outfile_name.pos.junc.1.summary.txt
- outfile_name.pos.junc.2.summary.txt
- outfile_name.neg.junc.1.summary.txt
- outfile_name.neg.junc.2.summary.txt

#### plotFrequency.ipynb

After generating outfiles above, the four summary text files are used for plotting the frequency of occurence of RNA tags bound by the RNA Binding Protein (RBP).<br />

For the plotting around 5'SS, outfile_name.pos.junc.1.summary.txt and outfile_name.neg.junc.2.summary.txt are concatenated:

```console
( cat outfile_name.pos.junc.1.summary.txt ; echo ""; cat outfile_name.neg.junc.2.summary.txt; echo ) > outfile_name.junc.5SS.summary.txt
```

For the plotting around 3'SS, outfile_name.pos.junc.2.summary.txt and outfile_name.neg.junc.1.summary.txt are concatenated:

```console
( cat outfile_name.pos.junc.2.summary.txt ; echo ""; cat outfile_name.neg.junc.1.summary.txt; echo ) > outfile_name.junc.3SS.summary.txt
```

The plotting is done using plotFrequency.ipynb in jupyter notebook.
=======
python3 findJunctions.v1.7.py splicesites_coordinates.txt file.bed -n 50 -o outfile_name

where splicesites_coordinates.txt is tab-delimited text containing splicing sites coordinates which is generated from GTF file by using "hisat2_extract_splice_sites.py" in hisat2 package.
file.bed is the output file of the CTK pipeline for HITS-CLIP data analysis, showing the genomic coordinate information of unique tags bound by RNA binding protein.
-n 50, the given range around splicing sites is -50nt~+50nt.
-o outfile_name, output files contain four bed-like format files (1st column: Chromosome; 2nd column: HITS-CLIP unique tag name; 3rd column: Coordinates of end/start of tag; 4th column: Coordinates of 5'SS/3'SS) and four txt files (1st column: Count of tags at each site; 2nd: Genomic distance between tag and SS, 0 representing SS).

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
>>>>>>> 194833d94207b69561c512e4f967e9e603968424
