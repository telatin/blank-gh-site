---
layout: defaults/article
title: Downloading NGS data sets from the command line
tags:
  - bash
---

## Sequencing data archives

When you publish a paper based on nucleic acids sequencing it is mandatory to
submit the “raw” data, i. e. all the reads produced without any filtering process,
to a public repository. The two major repositories for NGS reads are the
[SRA](https://www.ncbi.nlm.nih.gov/sra)
(Short Reads Archive, hosted in the USA by the NCBI), and the
[ENA](https://www.ebi.ac.uk/ena)
(European Nucleotide Archive, hosted in the EU at the EBI). They are both very good, yet for this short note we’ll address the former.

They both have an interesting hierarchical data description, so that each “sequencing run” is linked to an experiment (or project) and finally to one or more biological samples. Sometimes the information describing both the experiment and the sample is quite limited, but at least the bibliographical reference to a paper can lead to further details.

## Downloading URLs from the command line

We often are offered access to a resource (like a database, or reference genome)
in the form of a link in a website.
While it’s trivial to download it in the machine we are using to browse the
Internet (our laptop, for example), we usually have to use it from a Linux server
located elsewhere. We can thus right click on the link, choose
“Copy link location” (or similar) and then use the terminal to connect to the
remote server and then:
```
wget "http://hgdownload.cse.ucsc.edu/goldenPath/hg38/chromosomes/chr22.fa.gz"
```

The `wget` command simply downloads a remote file in the path we are currently working in. I recommend using quotes around the URL, as sometimes it contains characters like “&” that have a special meaning in the terminal.

## The Short Reads Archive (SRA) data portal

The SRA can be accessed from a web browser.
A typical entry for this database is a sequencing run made using some NGS platform.
Since a typical project involves more runs, there is an entity called BioProject
(its records are identified as PRJNAxxxx) to describe the whole study.
Here an example, the genome sequencing of a microalga:
- [https://www.ncbi.nlm.nih.gov/bioproject/PRJNA170989](https://www.ncbi.nlm.nih.gov/bioproject/PRJNA170989)

From the record we see a the table (depicted on the right)
that enumerates the SRA experiments associated with the same “BioProject”.

Clicking on the number we are redirected to this page:
- [https://www.ncbi.nlm.nih.gov/sra?linkname=bioproject_sra_all&from_uid=170989](https://www.ncbi.nlm.nih.gov/sra?linkname=bioproject_sra_all&from_uid=170989)

This is the list:
1. [SOLiD3Plus run of Nannochloropsis gaditana B-31 (MP) ](https://www.ncbi.nlm.nih.gov/sra/SRX390681%5Baccn%5D)
1 ABI_SOLID (AB SOLiD 3 Plus System) run: 153.5M spots, 15.3G bases, 12.3Gb downloads; Accession: **SRX390681**
1. [SOLiD3Plus run of Nannochloropsis gaditana B-31 (MP)](https://www.ncbi.nlm.nih.gov/sra/SRX390674%5Baccn%5D)
ABI_SOLID (AB SOLiD 3 Plus System) run: 138M spots, 13.8G bases, 11.1Gb downloads; Accession: **SRX390674**
1. [454GSFLX run of Nannochloropsis gaditana B-31 (FRAGMENT)](https://www.ncbi.nlm.nih.gov/sra/SRX390591%5Baccn%5D)
LS454 (454 GS FLX+) run: 1.3M spots, 1.6G bases, 3.2Gb downloads; Accession: **SRX390591**

Each record has a unique identifier, in this case starting by **SRX** (Short Reads Experiment).
This genome has been sequenced with a mixed approach combining long(ish) reads from a
_Roche 454_ run and scaffolding them with _SOLiD Mate Pairs_.
Each experiment is associated to one or more sequencing runs (**SRR**).
For the last entry (the 454 run), the run accession is SRR1048055.

There is another record describing the sample the nucleic acids were taken from:
the BioSample, in our example **[SAMN02440168](https://www.ncbi.nlm.nih.gov/biosample/SAMN02440168)**.

## Accessing the Short Reads Archive (SRA) from the command line

There are many toolkits to access the SRA, but to simply download reads knowing
the Accession ID (reads are in the sequencing run record, starting with SRR),
the task is made simple by `fastq-dump`, a program of the sra-toolkit.

#### Installing fastq-dump

If we don’t have the utility we can install it from the Debian/Ubuntu repositories with:

```
sudo apt-get install sra-toolkit
```

If we don’t have administrative privileges in the Linux box, but we installed Miniconda:

```
conda config --add channels bioconda
conda install -y sra-tools
```

#### Downloading reads
If we want to download reads from the 454 run on N. gaditana (SRR1048055) we can use the command:
```
fastq-dump SRR1048055
```

An important option that is (almost) always used is `--split-lanes`.
If we want to download a paired-end (or mate-paired) library, the default behaviour of fastq-dump
is to produce a single file interleaving the first and the second pair, while we usually are interested in producing two separate files.
For example:
```
fastq-dump --split-lanes SRR1553607
```

#### Where are temporary files stored?

It’s important to note that, by default, fastq-dump stores temporary files
(and cache) in our home, even if we download data elsewhere.
It’s wise to check the disk usage of the `~/ncbi/` directory used by fastq-dump,
and we can do so with the du (disk usage) command:
```
du -hs ~/ncbi/
```

## Conclusions

The ability to access big repositories from the command line has to main benefits.

First, when we use a remote Linux server to perform the analyses, we can directly
download from there the control data sets, avoiding to download them locally in
our computer and then to transfer them. This is an immediate benefit for all users,
and the reason why I wrote this short note.

Advanced users also use this to be able to be able to include in their script
commands to programmatically retrieve data. I mention this at the end of the
note just hoping that some beginner bioinformaticians will aspire to develop
scripting abilities in their future.

_Norwich, March 14, 2018_
