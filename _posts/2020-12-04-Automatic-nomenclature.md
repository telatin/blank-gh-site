---
title: Generating latin bacterial names with GAN
tags:
  - paper
---

<p class="d-flex align-items-center">

    <span class="icon red ml-2 pb-2">
        {% include entypo/documents.svg %}
    </span>
    <span>
    Mark J. Pallen, Andrea Telatin, Aharon Oren<br>
    <strong><a href="https://www.sciencedirect.com/science/article/pii/S0966842X20302717">
    The Next Million Names for Archaea and Bacteria</a>
    </strong>
    </span>
</p>

I recently had the opportunity to work on an intriguing project: the
**Great Automatic Nomenclaturer**, conceived by Mark Pallen in his
attempt to give a valid latin (binomial) name to the novel species he
identified in a metagenomic exploration of chicken gut samples.

Metagenomics allows us to recover _novel genomes_ (referred to as
_Magenomics Assembled Genomes_, or _MAGs_), and comparing them with the
known genomes we can often identify new species (and even new genera).

We can easily produce hundreds or thousands new genomes for each experiment,
so giving a name to each can be challenging. Unless we use a **combinatorial**
approach, so with a bunch of components we can produce thousands new names.

Here an example of the roots to be used:
![roots](https://raw.githubusercontent.com/telatin/gan/master/docs/input_table.png)

"The great automatic nomenclaturer" is a reference to a short story
("[The Great Automatic Grammatizator](https://en.wikipedia.org/wiki/The_Great_Automatic_Grammatizator)")
written by the British author Roald Dahl.

- [Software repository](https://github.com/telatin/gan)
- [Example output: PDF](https://telatin.github.io/gan/example.pdf)
- [Example output: HTML](https://telatin.github.io/gan/example.html)
