---
layout: default
title: UI for my github repos
---

<h1>{{ page.title }}</h1>

<h3>News: </h3>
<ul>
{% for item in site.data.items.news %}
  <li>{{ item }}</li>
{% endfor %}
</ul>

<h3>Bonds worth investing in : </h3>
{% for item in site.data.bonds.data %}
  Symbol - {{ item.symbol }}
  Buy Price - {{ item.askprice }}
  Yield - {{ item.xirr }} %
  Rating - {{ item.Rating }} ( {{ item.Rating_Agency }} )
  Risk - {{ item.Seniority }} &nbsp; {{ item.Secure_UnSecure }} 
  Interest Frequency - {{ item.IntrPay_Mode }}
  Payment Schedule - <br/>
  <table>
  {% for item1 in item.finalCashArray %}
    <tr>
      <td>{{item1.date}}</td>
      <td>{{item1.interest}}</td>
    </tr>
  {% endfor %}
  </table>
{% endfor %}
