---
title: Projects
narrow: true
permalink: list/projects.html
show_profile: true
---

{% for project in site.projects %}
- [{{ project.title }}]({{ site.baseurl }}{{ project.url }})
{% endfor %}


## Articles 
{% for project in site.articles %}
- [{{ project.title }}]({{ site.baseurl }}{{ project.url }})
{% endfor %}