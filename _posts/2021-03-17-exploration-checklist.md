---
keywords: fastai
title: A data exploration checklist
hide: false
toc: true
comments: true
categories: [python, pandas]
nb_path: _notebooks/2021-03-17-exploration-checklist.ipynb
layout: notebook
---

<!--
#################################################
### THIS FILE WAS AUTOGENERATED! DO NOT EDIT! ###
#################################################
# file to edit: _notebooks/2021-03-17-exploration-checklist.ipynb
-->

<div class="container" id="notebook-container">
        
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>A step-by-step recipe for getting to know a new dataset.</p>

</div>
</div>
</div>
    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span>
</pre></div>

    </div>
</div>
</div>

</div>
    {% endraw %}

<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Read-and-have-a-quick-look">Read and have a quick look<a class="anchor-link" href="#Read-and-have-a-quick-look"> </a></h1>
</div>
</div>
</div>
    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="s1">&#39;data/competitor_prices.csv&#39;</span><span class="p">)</span>
<span class="n">df</span><span class="o">.</span><span class="n">head</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">


<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Product_id</th>
      <th>Competitor_id</th>
      <th>Competitor_Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>25/11/2013</td>
      <td>4.0</td>
      <td>C</td>
      <td>74.95</td>
    </tr>
    <tr>
      <th>1</th>
      <td>25/11/2013</td>
      <td>4.0</td>
      <td>D</td>
      <td>74.95</td>
    </tr>
    <tr>
      <th>2</th>
      <td>25/11/2013</td>
      <td>4.0</td>
      <td>E</td>
      <td>75.00</td>
    </tr>
    <tr>
      <th>3</th>
      <td>25/11/2013</td>
      <td>4.0</td>
      <td>F</td>
      <td>99.95</td>
    </tr>
    <tr>
      <th>4</th>
      <td>26/11/2013</td>
      <td>4.0</td>
      <td>C</td>
      <td>74.95</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
    {% endraw %}

    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span><span class="o">.</span><span class="n">describe</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">


<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Product_id</th>
      <th>Competitor_Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>15132.000000</td>
      <td>15132.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>248.535223</td>
      <td>85.339813</td>
    </tr>
    <tr>
      <th>std</th>
      <td>115.916096</td>
      <td>48.460998</td>
    </tr>
    <tr>
      <th>min</th>
      <td>4.000000</td>
      <td>2.300000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>143.000000</td>
      <td>49.950000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>251.000000</td>
      <td>75.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>355.000000</td>
      <td>108.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>421.000000</td>
      <td>500.000000</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
    {% endraw %}

    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span><span class="o">.</span><span class="n">Competitor_id</span><span class="o">.</span><span class="n">describe</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">



<div class="output_text output_subarea output_execute_result">
<pre>count     15132
unique        7
top           D
freq       8092
Name: Competitor_id, dtype: object</pre>
</div>

</div>

</div>
</div>

</div>
    {% endraw %}

    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span><span class="o">.</span><span class="n">info</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">

<div class="output_subarea output_stream output_stdout output_text">
<pre>&lt;class &#39;pandas.core.frame.DataFrame&#39;&gt;
RangeIndex: 15395 entries, 0 to 15394
Data columns (total 4 columns):
 #   Column            Non-Null Count  Dtype  
---  ------            --------------  -----  
 0   Date              15132 non-null  object 
 1   Product_id        15132 non-null  float64
 2   Competitor_id     15132 non-null  object 
 3   Competitor_Price  15132 non-null  float64
dtypes: float64(2), object(2)
memory usage: 481.2+ KB
</pre>
</div>
</div>

</div>
</div>

</div>
    {% endraw %}

<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Missing-values">Missing values<a class="anchor-link" href="#Missing-values"> </a></h1><p><a href="https://github.com/ResidentMario/missingno">https://github.com/ResidentMario/missingno</a></p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Sources">Sources<a class="anchor-link" href="#Sources"> </a></h2><ul>
<li><a href="https://www.oreilly.com/library/view/fluent-python/9781491946237/">Fluent Python</a></li>
<li><a href="https://www.oreilly.com/library/view/python-cookbook-3rd/9781449357337/">Python Cookbook</a></li>
<li><a href="https://www.oreilly.com/library/view/learning-python-5th/9781449355722/">Learning Python</a></li>
<li><a href="https://docs.python-guide.org/writing/structure/">The Hitchhiker's Guide to Python</a></li>
<li><a href="https://effectivepython.com">Effective Python</a></li>
<li><a href="https://www.oreilly.com/library/view/python-for-data/9781491957653/">Python for Data Analysis</a></li>
<li><a href="https://www.oreilly.com/library/view/python-data-science/9781491912126/">Python Data Science Handbook</a></li>
<li><a href="https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html">Pandas cookbook</a></li>
<li><a href="https://numpy.org/doc/stable/">Numpy docs</a></li>
</ul>

</div>
</div>
</div>
</div>
 

