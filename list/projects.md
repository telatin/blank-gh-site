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

- [QAX, Qiime Artifact eXtractor (documentation)](/qax)

- [SeqFu2 sequence utilities (documentation)](/seqfu2)


### Articles
{% for project in site.articles %}
- [{{ project.title }}]({{ site.baseurl }}{{ project.url }})
{% endfor %}
