---
keywords: fastai
title: Functools
toc: true
badges: true
comments: true
categories: [python]
nb_path: _notebooks/2020-09-17-functools.ipynb
layout: notebook
---

<!--
#################################################
### THIS FILE WAS AUTOGENERATED! DO NOT EDIT! ###
#################################################
# file to edit: _notebooks/2020-09-17-functools.ipynb
-->

<div class="container" id="notebook-container">
        
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="partial">partial<a class="anchor-link" href="#partial"> </a></h2>
</div>
</div>
</div>
    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">operator</span> <span class="kn">import</span> <span class="n">mul</span>
<span class="kn">from</span> <span class="nn">functools</span> <span class="kn">import</span> <span class="n">partial</span>

<span class="nb">print</span><span class="p">(</span><span class="n">mul</span><span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">))</span>

<span class="n">tripple</span> <span class="o">=</span> <span class="n">partial</span><span class="p">(</span><span class="n">mul</span><span class="p">,</span> <span class="mi">3</span><span class="p">)</span>
<span class="n">tripple</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">

<div class="output_subarea output_stream output_stdout output_text">
<pre>6
</pre>
</div>
</div>

<div class="output_area">



<div class="output_text output_subarea output_execute_result">
<pre>6</pre>
</div>

</div>

</div>
</div>

</div>
    {% endraw %}

<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Sources">Sources<a class="anchor-link" href="#Sources"> </a></h2><ul>
<li><a href="https://www.oreilly.com/library/view/fluent-python/9781491946237/">Fluent Python</a></li>
<li><a href="https://www.oreilly.com/library/view/python-cookbook-3rd/9781449357337/">Python Cookbook</a></li>
</ul>

</div>
</div>
</div>
</div>
 

