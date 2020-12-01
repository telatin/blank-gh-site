#!/usr/bin/env python3

from scholarly import scholarly
import sys
def stderr(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


author_id = 'Bua3yncAAAAJ'
author = scholarly.search_author_id(author_id).fill()

stderr("Author retrieved")

def getFirstAuthor(auth):
	authList = auth.split(" and ")
	return authList[0]

for paper in author.publications:
    paper.fill()
    authors = paper.bib['author'] if 'author' in paper.bib else ''
    title   = paper.bib['title'] if 'title' in paper.bib else ''
    abstract = paper.bib['abstract'] if 'abstract' in paper.bib else ''
    journal = paper.bib['journal'] if 'journal' in paper.bib else ''
    year = paper.bib['year'] if 'year' in paper.bib else ''
    eprint = paper.bib['eprint'] if 'eprint' in paper.bib else ''
    first_author = getFirstAuthor(authors)
    stderr(" - ", first_author)
    print( f"{first_author} _et al._ ({year}) *{title}*, [{journal}]({eprint})_\n")
      




## AUTHOR FILLED
#{'affiliation': 'Quadram Institute, Norwich, United Kingdom',
# 'citedby': 553,
# 'citedby5y': 516,
# 'cites_per_year': {2013: 5,
#                    2014: 26,
#                    2015: 49,
#                    2016: 72,
#                    2017: 81,
#                    2018: 84,
#                    2019: 103,
#                    2020: 126},

## SINGLE 'paper'
# {'bib': {'cites': '187',
#          'title': 'A deep survey of alternative splicing in grape reveals '
#                   'changes in the splicing machinery related to tissue, stress '
#                   'condition and genotype',
#          'year': '2014'},
#  'filled': False,
#  'id_citations': 'Bua3yncAAAAJ:UeHWp8X0CEIC',
#  'source': 'citations'}

## Single 'paper'.fill()
# {'bib': {'abstract': 'Alternative splicing (AS) significantly enhances '
#                      'transcriptome complexity. It is differentially regulated '
#                      'in a wide variety of cell types and plays a role in '
#                      'several cellular processes. Here we describe a detailed '
#                      'survey of alternative splicing in grape based on 124 '
#                      'SOLiD RNAseq analyses from different tissues, stress '
#                      'conditions and genotypes.We used the RNAseq data to '
#                      'update the existing grape gene prediction with 2,258 new '
#                      'coding genes and 3,336 putative long non-coding RNAs. '
#                      'Several gene structures have been improved and '
#                      'alternative splicing was described for about 30% of the '
#                      'genes. A link between AS and miRNAs was shown in 139 '
#                      'genes where we found that AS affects the miRNA target '
#                      'site. A quantitative analysis of the isoforms indicated '
#                      'that most of the spliced genes have one major isoform '
#                      'and tend to simultaneously …',
#          'author': 'Nicola Vitulo and Claudio Forcato and Elisa Corteggiani '
#                    'Carpinelli and Andrea Telatin and Davide Campagna and '
#                    "Michela D'Angelo and Rosanna Zimbello and Massimiliano "
#                    'Corso and Alessandro Vannozzi and Claudio Bonghi and '
#                    'Margherita Lucchin and Giorgio Valle',
#          'cites': '187',
#          'cites_id': '10975719285356258513',
#          'eprint': 'https://link.springer.com/article/10.1186/1471-2229-14-99',
#          'journal': 'BMC plant biology',
#          'number': '1',
#          'pages': '99',
#          'publisher': 'BioMed Central',
#          'title': 'A deep survey of alternative splicing in grape reveals '
#                   'changes in the splicing machinery related to tissue, stress '
#                   'condition and genotype',
#          'url': 'https://link.springer.com/article/10.1186/1471-2229-14-99',
#          'volume': '14',
#          'year': '2014'},
#  'citations_link': '/scholar?cites=10975719285356258513',
#  'cites_per_year': {2013: 1,
#                     2014: 5,
#                     2015: 25,
#                     2016: 27,
#                     2017: 34,
#                     2018: 34,
#                     2019: 37,
#                     2020: 23},
#  'filled': True,
#  'id_citations': 'Bua3yncAAAAJ:UeHWp8X0CEIC',
#  'source': 'citations'}