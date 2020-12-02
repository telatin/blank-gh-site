---
title: Crafts
narrow: true
permalink: list/projects.html
show_profile: true
---

{% for project in site.projects %}
- [{{ project.title }}]({{ site.baseurl }}{{ project.url }})
{% endfor %}


### Subsites

- :package: [QAX, Qiime Artifact eXtractor (documentation)]({{ site.baseurl }}/qax)

- :package: [SeqFu2 sequence utilities (documentation)]({{ site.baseurl }}/seqfu2)

- :book: [Nim for bioinformatics (ebook)]({{ site.baseurl }}/nim-for-bioinformatics)


### Articles
{% for project in site.articles %}
- [{{ project.title }}]({{ site.baseurl }}{{ project.url }})
{% endfor %}
