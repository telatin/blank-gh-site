---
title: Singularity to the rescue
tags:
  - website
---

I love **Singularity containers** because they run in user space and can
seamlessly mount my filesystem, allowing for a native experience of any
bionformatic tool.

Compare:
```
spades.py -1 reads/File_R1.fq -2 reads/File_R2.fq -o assembly
```
<!--more-->
with:
```
sudo docker run --rm --user user:group -v $PWD:/wd my/spades:last /wd/reads/File_R1.fq -2 /wd/reads/File_R2.fq -o /wd/assembly
```

I saved some notes on Singularity containers that I use in bioinformatics
in a separate repository: [https://telatin.github.io/singularities](https://telatin.github.io/singularities).
