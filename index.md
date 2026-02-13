---
layout: default
title: News (JSON)
---

<h1>{{ page.title }}</h1>

<ul>
{% for item in site.data.items.news %}
  <li>{{ item }}</li>
{% endfor %}
</ul>