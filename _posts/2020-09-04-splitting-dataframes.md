---
keywords: fastai
title: Splitting dataframes based on column values
toc: true 
badges: true
comments: true
categories: [python, pandas]
nb_path: _notebooks/2020-09-04-splitting-dataframes.ipynb
layout: notebook
---

<!--
#################################################
### THIS FILE WAS AUTOGENERATED! DO NOT EDIT! ###
#################################################
# file to edit: _notebooks/2020-09-04-splitting-dataframes.ipynb
-->

<div class="container" id="notebook-container">
        
    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span>
<span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
</pre></div>

    </div>
</div>
</div>

</div>
    {% endraw %}

<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="The-problem">The problem<a class="anchor-link" href="#The-problem"> </a></h2>
</div>
</div>
</div>
    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">data</span><span class="o">=</span><span class="p">{</span><span class="s1">&#39;case&#39;</span><span class="p">:</span> <span class="p">[</span><span class="s1">&#39;A&#39;</span><span class="p">,</span> <span class="s1">&#39;A&#39;</span><span class="p">,</span> <span class="s1">&#39;A&#39;</span><span class="p">,</span> <span class="s1">&#39;B&#39;</span><span class="p">,</span> <span class="s1">&#39;A&#39;</span><span class="p">,</span> <span class="s1">&#39;A&#39;</span><span class="p">,</span> <span class="s1">&#39;B&#39;</span><span class="p">,</span> <span class="s1">&#39;A&#39;</span><span class="p">,</span><span class="s1">&#39;A&#39;</span><span class="p">],</span>
                        <span class="s1">&#39;data&#39;</span><span class="p">:</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">randn</span><span class="p">(</span><span class="mi">9</span><span class="p">)})</span>
<span class="n">df</span>
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
      <th>case</th>
      <th>data</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A</td>
      <td>0.684978</td>
    </tr>
    <tr>
      <th>1</th>
      <td>A</td>
      <td>0.000269</td>
    </tr>
    <tr>
      <th>2</th>
      <td>A</td>
      <td>-1.040497</td>
    </tr>
    <tr>
      <th>3</th>
      <td>B</td>
      <td>0.451358</td>
    </tr>
    <tr>
      <th>4</th>
      <td>A</td>
      <td>0.448596</td>
    </tr>
    <tr>
      <th>5</th>
      <td>A</td>
      <td>0.222168</td>
    </tr>
    <tr>
      <th>6</th>
      <td>B</td>
      <td>1.031011</td>
    </tr>
    <tr>
      <th>7</th>
      <td>A</td>
      <td>-2.208787</td>
    </tr>
    <tr>
      <th>8</th>
      <td>A</td>
      <td>-0.440758</td>
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

<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>You want to split the dataframe every time case equals B and store the resulting dataframes in a list.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Understanding-the-cookbook-solution">Understanding the cookbook solution<a class="anchor-link" href="#Understanding-the-cookbook-solution"> </a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>From the <a href="https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#id2">cookbook</a>:</p>

</div>
</div>
</div>
    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dfs</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="nb">zip</span><span class="p">(</span><span class="o">*</span><span class="n">df</span><span class="o">.</span><span class="n">groupby</span><span class="p">((</span><span class="mi">1</span> <span class="o">*</span> <span class="p">(</span><span class="n">df</span><span class="p">[</span><span class="s1">&#39;case&#39;</span><span class="p">]</span> <span class="o">==</span> <span class="s1">&#39;B&#39;</span><span class="p">))</span><span class="o">.</span><span class="n">cumsum</span><span class="p">()</span><span class="o">.</span><span class="n">rolling</span><span class="p">(</span><span class="n">window</span><span class="o">=</span><span class="mi">3</span><span class="p">,</span> <span class="n">min_periods</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span><span class="o">.</span><span class="n">median</span><span class="p">())))[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span>
<span class="n">dfs</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">



<div class="output_text output_subarea output_execute_result">
<pre>(  case      data
 0    A  0.684978
 1    A  0.000269
 2    A -1.040497
 3    B  0.451358,
   case      data
 4    A  0.448596
 5    A  0.222168
 6    B  1.031011,
   case      data
 7    A -2.208787
 8    A -0.440758)</pre>
</div>

</div>

</div>
</div>

</div>
    {% endraw %}

<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>This works. But because it's so heavily nested and uses methods like <code>rolling()</code> and <code>median()</code> not really designed for that purpose, the code is impossible to interpret at a glance.</p>
<p>Let's break this down into separate pieces.</p>
<p>First, the code creates a grouping variable that changes its value each time <em>case</em> equaled <em>B</em> on the previous row. The code below shows how it does this.</p>

</div>
</div>
</div>
    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">a</span> <span class="o">=</span> <span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">case</span> <span class="o">==</span> <span class="s1">&#39;B&#39;</span><span class="p">)</span>
<span class="n">b</span> <span class="o">=</span> <span class="mi">1</span> <span class="o">*</span> <span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">case</span> <span class="o">==</span> <span class="s1">&#39;B&#39;</span><span class="p">)</span>
<span class="n">c</span> <span class="o">=</span> <span class="mi">1</span> <span class="o">*</span> <span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">case</span> <span class="o">==</span> <span class="s1">&#39;B&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">cumsum</span><span class="p">()</span>
<span class="n">d</span> <span class="o">=</span> <span class="mi">1</span> <span class="o">*</span> <span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">case</span> <span class="o">==</span> <span class="s1">&#39;B&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">cumsum</span><span class="p">()</span><span class="o">.</span><span class="n">rolling</span><span class="p">(</span><span class="n">window</span><span class="o">=</span><span class="mi">3</span><span class="p">,</span> <span class="n">min_periods</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span><span class="o">.</span><span class="n">median</span><span class="p">()</span>

<span class="n">a</span><span class="p">,</span> <span class="n">b</span><span class="p">,</span> <span class="n">c</span><span class="p">,</span> <span class="n">d</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">



<div class="output_text output_subarea output_execute_result">
<pre>(0    False
 1    False
 2    False
 3     True
 4    False
 5    False
 6     True
 7    False
 8    False
 Name: case, dtype: bool,
 0    0
 1    0
 2    0
 3    1
 4    0
 5    0
 6    1
 7    0
 8    0
 Name: case, dtype: int64,
 0    0
 1    0
 2    0
 3    1
 4    1
 5    1
 6    2
 7    2
 8    2
 Name: case, dtype: int64,
 0    0.0
 1    0.0
 2    0.0
 3    0.0
 4    1.0
 5    1.0
 6    1.0
 7    2.0
 8    2.0
 Name: case, dtype: float64)</pre>
</div>

</div>

</div>
</div>

</div>
    {% endraw %}

<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Series <em>d</em> above is the argument passed to <code>groupby()</code> in the solution. This works, but is a very roundabout way to create such a series. I'll use a different approach below.</p>
<p>Next, the code uses <code>list()</code>, <code>zip()</code>, and argument expansion to pack the data for each group into a single list of dataframes. Let's look at these one by one.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>First, a quick review of how argument expansion works:</p>

</div>
</div>
</div>
    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">printer</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>    
    <span class="nb">print</span><span class="p">(</span><span class="s1">&#39;Printing args:&#39;</span><span class="p">)</span>
    <span class="k">for</span> <span class="n">arg</span> <span class="ow">in</span> <span class="n">args</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="n">arg</span><span class="p">)</span>
    <span class="nb">print</span><span class="p">(</span><span class="s1">&#39;Printing kwargs:&#39;</span><span class="p">)</span>
    <span class="k">for</span> <span class="n">kwarg</span> <span class="ow">in</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
        <span class="nb">print</span><span class="p">(</span><span class="n">kwarg</span><span class="p">)</span>
    
<span class="n">mylist</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;a&#39;</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="s1">&#39;k&#39;</span><span class="p">,</span> <span class="mi">3</span><span class="p">]</span>
<span class="n">mydict</span> <span class="o">=</span> <span class="p">{</span><span class="s1">&#39;first&#39;</span><span class="p">:</span> <span class="mi">1</span><span class="p">,</span> <span class="s1">&#39;second&#39;</span><span class="p">:</span> <span class="mi">2</span><span class="p">}</span>

<span class="n">printer</span><span class="p">(</span><span class="o">*</span><span class="n">mylist</span><span class="p">,</span> <span class="o">**</span><span class="n">mydict</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">

<div class="output_subarea output_stream output_stdout output_text">
<pre>Printing args:
a
2
k
3
Printing kwargs:
(&#39;first&#39;, 1)
(&#39;second&#39;, 2)
</pre>
</div>
</div>

</div>
</div>

</div>
    {% endraw %}

<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Now, <code>groupby()</code> stores the grouped data as (label, dataframe) tuples, like so:</p>

</div>
</div>
</div>
    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">groups</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">groupby</span><span class="p">(</span><span class="s1">&#39;case&#39;</span><span class="p">)</span>
<span class="k">for</span> <span class="n">g</span> <span class="ow">in</span> <span class="n">groups</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">g</span><span class="p">)</span>
    <span class="nb">print</span><span class="p">(</span><span class="nb">type</span><span class="p">(</span><span class="n">g</span><span class="p">))</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">

<div class="output_subarea output_stream output_stdout output_text">
<pre>(&#39;A&#39;,   case      data
0    A  0.684978
1    A  0.000269
2    A -1.040497
4    A  0.448596
5    A  0.222168
7    A -2.208787
8    A -0.440758)
&lt;class &#39;tuple&#39;&gt;
(&#39;B&#39;,   case      data
3    B  0.451358
6    B  1.031011)
&lt;class &#39;tuple&#39;&gt;
</pre>
</div>
</div>

</div>
</div>

</div>
    {% endraw %}

<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>So <code>zip()</code> is used to separate the group label from the data, and <code>list()</code> consumes the iterator created by zip and displays its content.</p>

</div>
</div>
</div>
    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">list</span><span class="p">(</span><span class="nb">zip</span><span class="p">(</span><span class="o">*</span><span class="n">groups</span><span class="p">))</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">



<div class="output_text output_subarea output_execute_result">
<pre>[(&#39;A&#39;, &#39;B&#39;),
 (  case      data
  0    A  0.684978
  1    A  0.000269
  2    A -1.040497
  4    A  0.448596
  5    A  0.222168
  7    A -2.208787
  8    A -0.440758,
    case      data
  3    B  0.451358
  6    B  1.031011)]</pre>
</div>

</div>

</div>
</div>

</div>
    {% endraw %}

<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Because we only want the data, we select the last element from the list:</p>

</div>
</div>
</div>
    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">list</span><span class="p">(</span><span class="nb">zip</span><span class="p">(</span><span class="o">*</span><span class="n">groups</span><span class="p">))[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">



<div class="output_text output_subarea output_execute_result">
<pre>(  case      data
 0    A  0.684978
 1    A  0.000269
 2    A -1.040497
 4    A  0.448596
 5    A  0.222168
 7    A -2.208787
 8    A -0.440758,
   case      data
 3    B  0.451358
 6    B  1.031011)</pre>
</div>

</div>

</div>
</div>

</div>
    {% endraw %}

<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Now we're basically done. What remains is to use the <code>list(zip(*groups))</code> procedure on the more complicated grouping variable, to obtain the original result.</p>

</div>
</div>
</div>
    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">d</span> <span class="o">=</span> <span class="mi">1</span> <span class="o">*</span> <span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">case</span> <span class="o">==</span> <span class="s1">&#39;B&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">cumsum</span><span class="p">()</span><span class="o">.</span><span class="n">rolling</span><span class="p">(</span><span class="n">window</span><span class="o">=</span><span class="mi">3</span><span class="p">,</span> <span class="n">min_periods</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span><span class="o">.</span><span class="n">median</span><span class="p">()</span>
<span class="n">groups</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">groupby</span><span class="p">(</span><span class="n">d</span><span class="p">)</span>
<span class="nb">list</span><span class="p">(</span><span class="nb">zip</span><span class="p">(</span><span class="o">*</span><span class="n">groups</span><span class="p">))[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">



<div class="output_text output_subarea output_execute_result">
<pre>(  case      data
 0    A  0.684978
 1    A  0.000269
 2    A -1.040497
 3    B  0.451358,
   case      data
 4    A  0.448596
 5    A  0.222168
 6    B  1.031011,
   case      data
 7    A -2.208787
 8    A -0.440758)</pre>
</div>

</div>

</div>
</div>

</div>
    {% endraw %}

<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Simplifying-the-code">Simplifying the code<a class="anchor-link" href="#Simplifying-the-code"> </a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>I think this can be made much more readable like so:</p>

</div>
</div>
</div>
    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span>
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
      <th>case</th>
      <th>data</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A</td>
      <td>0.684978</td>
    </tr>
    <tr>
      <th>1</th>
      <td>A</td>
      <td>0.000269</td>
    </tr>
    <tr>
      <th>2</th>
      <td>A</td>
      <td>-1.040497</td>
    </tr>
    <tr>
      <th>3</th>
      <td>B</td>
      <td>0.451358</td>
    </tr>
    <tr>
      <th>4</th>
      <td>A</td>
      <td>0.448596</td>
    </tr>
    <tr>
      <th>5</th>
      <td>A</td>
      <td>0.222168</td>
    </tr>
    <tr>
      <th>6</th>
      <td>B</td>
      <td>1.031011</td>
    </tr>
    <tr>
      <th>7</th>
      <td>A</td>
      <td>-2.208787</td>
    </tr>
    <tr>
      <th>8</th>
      <td>A</td>
      <td>-0.440758</td>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">grouper</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">case</span><span class="o">.</span><span class="n">eq</span><span class="p">(</span><span class="s1">&#39;B&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">cumsum</span><span class="p">()</span><span class="o">.</span><span class="n">shift</span><span class="p">()</span><span class="o">.</span><span class="n">fillna</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
<span class="n">grouper</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">



<div class="output_text output_subarea output_execute_result">
<pre>0    0.0
1    0.0
2    0.0
3    0.0
4    1.0
5    1.0
6    1.0
7    2.0
8    2.0
Name: case, dtype: float64</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dfs</span> <span class="o">=</span> <span class="p">[</span><span class="n">df</span> <span class="k">for</span> <span class="p">(</span><span class="n">g</span><span class="p">,</span> <span class="n">df</span><span class="p">)</span> <span class="ow">in</span> <span class="n">df</span><span class="o">.</span><span class="n">groupby</span><span class="p">(</span><span class="n">grouper</span><span class="p">)]</span>
<span class="n">dfs</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">



<div class="output_text output_subarea output_execute_result">
<pre>[  case      data
 0    A  0.684978
 1    A  0.000269
 2    A -1.040497
 3    B  0.451358,
   case      data
 4    A  0.448596
 5    A  0.222168
 6    B  1.031011,
   case      data
 7    A -2.208787
 8    A -0.440758]</pre>
</div>

</div>

</div>
</div>

</div>
    {% endraw %}

<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>In case the logic of this isn't immediately obvious, the below makes clear what's going on.</p>

</div>
</div>
</div>
    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dd</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">set_index</span><span class="p">(</span><span class="s1">&#39;case&#39;</span><span class="p">,</span> <span class="n">drop</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>   <span class="c1"># Use case as index for clarity</span>
<span class="n">a</span> <span class="o">=</span> <span class="n">dd</span><span class="o">.</span><span class="n">case</span><span class="o">.</span><span class="n">eq</span><span class="p">(</span><span class="s1">&#39;B&#39;</span><span class="p">)</span>                     <span class="c1"># Boolean logic</span>
<span class="n">b</span> <span class="o">=</span> <span class="n">a</span><span class="o">.</span><span class="n">cumsum</span><span class="p">()</span>                          <span class="c1"># Create groups</span>
<span class="n">c</span> <span class="o">=</span> <span class="n">b</span><span class="o">.</span><span class="n">shift</span><span class="p">()</span>                           <span class="c1"># Shift so B included in previous group</span>
<span class="n">d</span> <span class="o">=</span> <span class="n">c</span><span class="o">.</span><span class="n">fillna</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>                         <span class="c1"># Replace 0th element emptied by shift</span>
<span class="n">a</span><span class="p">,</span> <span class="n">b</span><span class="p">,</span> <span class="n">c</span><span class="p">,</span> <span class="n">d</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">



<div class="output_text output_subarea output_execute_result">
<pre>(case
 A    False
 A    False
 A    False
 B     True
 A    False
 A    False
 B     True
 A    False
 A    False
 Name: case, dtype: bool,
 case
 A    0
 A    0
 A    0
 B    1
 A    1
 A    1
 B    2
 A    2
 A    2
 Name: case, dtype: int64,
 case
 A    NaN
 A    0.0
 A    0.0
 B    0.0
 A    1.0
 A    1.0
 B    1.0
 A    2.0
 A    2.0
 Name: case, dtype: float64,
 case
 A    0.0
 A    0.0
 A    0.0
 B    0.0
 A    1.0
 A    1.0
 B    1.0
 A    2.0
 A    2.0
 Name: case, dtype: float64)</pre>
</div>

</div>

</div>
</div>

</div>
    {% endraw %}

</div>
 

