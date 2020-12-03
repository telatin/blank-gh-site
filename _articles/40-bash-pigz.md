---
layout: defaults/article
title: Pigz, a faster alternative to gzip for big files
tags:
  - bash
---

## Pigz: a faster alternative to gzip for big files

#### Using multiple threads to compress files but maintaining compatibility with gunzip.

The **gzip** program is incredibly popular among Linux applications,
in spite of some limitations. I think it fits incredibly well the
Unix Philosophy of a single program, doing a single thing and doing it well.

For example, we cannot compress a directory tree with gzip, but only single files.
This makes _gzip_ ideal to compress files that we want to use. On the other hand,
compressing a whole directory is generally used for archiving reasons where
accessing a single file is not the most common scenario.

Gzip libraries are commonly used to allow program directly reading compressed
files, that why we don’t need to decompress **sequencing output** (FASTQ files)
when feeding them to popular tools.

## Compressing large files

Bioinformaticians often need to compress very big files, such as large FASTQ
datasets where every single file can be bigger than 100 Gb¹.
Unfortunately, gzip is not parallelized and thus cannot split the job to use
the multiple processing cores our servers have.

**[Pigz](https://zlib.net/pigz/)** is a multi-threaded version of gzip, it’s widely available through software
repositories and has the important advantage of producing compatible gzip files.

## Installation

If we have administrative privileges we can install _pigz_ from our distribution
repositories. For most Debian based flavors (like Ubuntu) it’s as easy as:
```
sudo apt-get install pigz
```
We can install pigz also with user space repositories, like Miniconda:
```
conda install -y pigz
```

## A simple test

Compressing a single large FASTQ file on a machine with 8 cores:
```
time pigz Dataset.fastq
real 10m44.121s
user 93m37.800s
```
The process took 10 minutes, but the combined time used by all the threads was 93 minutes.

---

¹ The terminal is a multi-threaded environment, for example when we pipe programs
each part of a pipe runs on a separate thread. This means that
[we can parallelise](https://stackoverflow.com/questions/4341442/gzip-with-all-cores)
the compression of several files even without dedicated programs,
but large files can be a bottleneck.

_Norwich, Oct 2, 2018. Originally [published here](https://medium.com/ngs-sh/pigz-a-faster-alternative-to-gzip-for-big-files-d5909e46d659)._
