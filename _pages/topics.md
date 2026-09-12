---
layout: page
title: Topics
permalink: /topics/
---

<div class="tags">
  {% for tag in site.data.tags %}
  <a class="internal-link tag" href="{{ site.baseurl }}/topics/{{ tag | slugify }}/">{{ tag }}</a>
  {% endfor %}
</div>
