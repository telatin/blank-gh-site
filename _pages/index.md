---
layout: defaults/page
permalink: index.html
narrow: true
title: Some bioinformatics stuff
---


{% include components/intro.md %}

### Recent Articles

{% for post in site.articles limit:3 %}
{% include components/article-card-mini.html %}
{% endfor %}

### Recent Posts

{% for post in site.posts limit:2 %}
{% include components/post-card.html %}
{% endfor %}

{% for post in site.posts limit:6 offset:2 %}
{% include components/post-card-mini.html %}
{% endfor %}
