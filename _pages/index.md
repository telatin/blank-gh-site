---
layout: defaults/page
permalink: index.html
narrow: true
title: Some bioinformatics stuff
---


{% include components/intro.md %}


### Recent Posts

{% for post in site.posts limit:3 %}
{% include components/post-card.html %}
{% endfor %}
