---
layout: defaults/page
permalink: index.html
narrow: true
title: A binfie’s garret
---


{% include components/intro.md %}

[![GitHub](https://github-readme-stats.vercel.app/api?username=telatin&count_private=true&show_icons=true)](https://github.com/telatin)

### Some Articles

{% for post in site.articles limit:4 %}
{% include components/article-card-mini.html %}
{% endfor %}

### Recent Posts

{% for post in site.posts limit:3 %}
{% include components/post-card.html %}
{% endfor %}

### And less recent posts

{% for post in site.posts limit:6 offset:3 %}
{% include components/post-card-mini.html %}
{% endfor %}
