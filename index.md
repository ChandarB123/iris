---
layout: default
title: UI for my github repos
---


<style>
.bond-row {
  display: flex;
  border-bottom: 1px solid #ddd;
  padding: 15px 0;
  align-items: stretch;   /* makes both sides equal height */
}

.bond-left {
  flex: 2;
  padding-right: 20px;
}

.bond-right {
  flex: 1;
  display: flex;
}

.payment-scroll {
  max-height: 120px;   /* 3 rows visible */
  overflow-y: auto;
  width: 100%;
  border: 1px solid #ccc;
}

.payment-row {
  height: 40px;        /* fixed row height */
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 10px;
  border-bottom: 1px solid #eee;
}

.payment-scroll {
  scroll-behavior: smooth;
}

.payment-scroll::-webkit-scrollbar {
  width: 5px;
}

  
</style>

<h1>{{ page.title }}</h1>

<h3>News: </h3>
<ul>
{% for item in site.data.items.news %}
  <li>{{ item }}</li>
{% endfor %}
</ul>

<h3>Bonds worth investing in : </h3>
{% for item in site.data.bonds.data %}
  <div class="bond-row">
    <!-- LEFT SIDE -->
    <div class="bond-left">
      <div><strong>{{ item.symbol }}</strong></div>
      <div>Buy Price - {{ item.askprice }}</div>
      <div>Yield - {{ item.xirr }} %</div>
      <div>
        Rating - {{ item.Rating }}
        ({{ item.Rating_Agency }})
      </div>
      <div>
        Risk - {{ item.Seniority }}
        {{ item.Secure_UnSecure }}
      </div>
      <div>Interest Frequency - {{ item.IntrPay_Mode }}</div>
    </div>
    <!-- RIGHT SIDE -->
    <div class="bond-right">
      <div class="payment-scroll">
        {% for payment in item.finalCashArray %}
          <div class="payment-row">
            <span>{{ payment.date }}</span>
            <span>{{ payment.interest }}</span>
          </div>
        {% endfor %}
      </div>
    </div>
  </div>
{% endfor %}
