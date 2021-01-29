---
title: Crafts
narrow: true
permalink: list/projects.html
show_profile: true
---


### Subsites

- :package: [QAX, Qiime Artifact eXtractor (documentation)]({{ site.baseurl }}/qax)

- :package: [SeqFu2 sequence utilities (documentation)]({{ site.baseurl }}/seqfu2)

- :book: [Nim for bioinformatics (ebook)]({{ site.baseurl }}/nim-for-bioinformatics)

- :book: [Singularity for bioinformatics]({{ site.baseurl }}/singularities)


### Projects

{% for project in site.projects %}
- [{{ project.title }}]({{ site.baseurl }}{{ project.url }})
{% endfor %}


### Articles
{% for project in site.articles %}
- [{{ project.title }}]({{ site.baseurl }}{{ project.url }})
{% endfor %}
