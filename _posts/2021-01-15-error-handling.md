---
keywords: fastai
title: Error handling
hide: false
toc: false
comments: true
categories: [python]
nb_path: _notebooks/2021-01-15-error-handling.ipynb
layout: notebook
---

<!--
#################################################
### THIS FILE WAS AUTOGENERATED! DO NOT EDIT! ###
#################################################
# file to edit: _notebooks/2021-01-15-error-handling.ipynb
-->

<div class="container" id="notebook-container">
        
    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="o">%</span><span class="k">config</span> InlineBackend.figure_format = &#39;retina&#39;
<span class="o">%</span><span class="k">load_ext</span> autoreload
<span class="o">%</span><span class="k">autoreload</span> 2
</pre></div>

    </div>
</div>
</div>

</div>
    {% endraw %}

<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>A brief reminder of different ways to handle errors in Python.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Print message only</p>

</div>
</div>
</div>
    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">divide</span><span class="p">(</span><span class="n">a</span><span class="p">,</span> <span class="n">b</span><span class="p">):</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">a</span> <span class="o">/</span> <span class="n">b</span>
    <span class="k">except</span> <span class="ne">ZeroDivisionError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="n">e</span><span class="p">)</span>
        
<span class="n">divide</span><span class="p">(</span><span class="mi">4</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">

<div class="output_subarea output_stream output_stdout output_text">
<pre>division by zero
</pre>
</div>
</div>

</div>
</div>

</div>
    {% endraw %}

<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Raise original error (traceback and message)</p>

</div>
</div>
</div>
    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">divide</span><span class="p">(</span><span class="n">a</span><span class="p">,</span> <span class="n">b</span><span class="p">):</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">a</span> <span class="o">/</span> <span class="n">b</span>
    <span class="k">except</span> <span class="ne">ZeroDivisionError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
        <span class="k">raise</span> <span class="n">e</span>
        
<span class="n">divide</span><span class="p">(</span><span class="mi">4</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">

<div class="output_subarea output_text output_error">
<pre>
<span class="ansi-red-fg">---------------------------------------------------------------------------</span>
<span class="ansi-red-fg">ZeroDivisionError</span>                         Traceback (most recent call last)
<span class="ansi-green-fg">&lt;ipython-input-11-4ca87b7cf0dc&gt;</span> in <span class="ansi-cyan-fg">&lt;module&gt;</span>
<span class="ansi-green-intense-fg ansi-bold">      5</span>         <span class="ansi-green-fg">raise</span> e
<span class="ansi-green-intense-fg ansi-bold">      6</span> 
<span class="ansi-green-fg">----&gt; 7</span><span class="ansi-red-fg"> </span>divide<span class="ansi-blue-fg">(</span><span class="ansi-cyan-fg">4</span><span class="ansi-blue-fg">,</span> <span class="ansi-cyan-fg">0</span><span class="ansi-blue-fg">)</span>

<span class="ansi-green-fg">&lt;ipython-input-11-4ca87b7cf0dc&gt;</span> in <span class="ansi-cyan-fg">divide</span><span class="ansi-blue-fg">(a, b)</span>
<span class="ansi-green-intense-fg ansi-bold">      3</span>         <span class="ansi-green-fg">return</span> a <span class="ansi-blue-fg">/</span> b
<span class="ansi-green-intense-fg ansi-bold">      4</span>     <span class="ansi-green-fg">except</span> ZeroDivisionError <span class="ansi-green-fg">as</span> e<span class="ansi-blue-fg">:</span>
<span class="ansi-green-fg">----&gt; 5</span><span class="ansi-red-fg">         </span><span class="ansi-green-fg">raise</span> e
<span class="ansi-green-intense-fg ansi-bold">      6</span> 
<span class="ansi-green-intense-fg ansi-bold">      7</span> divide<span class="ansi-blue-fg">(</span><span class="ansi-cyan-fg">4</span><span class="ansi-blue-fg">,</span> <span class="ansi-cyan-fg">0</span><span class="ansi-blue-fg">)</span>

<span class="ansi-green-fg">&lt;ipython-input-11-4ca87b7cf0dc&gt;</span> in <span class="ansi-cyan-fg">divide</span><span class="ansi-blue-fg">(a, b)</span>
<span class="ansi-green-intense-fg ansi-bold">      1</span> <span class="ansi-green-fg">def</span> divide<span class="ansi-blue-fg">(</span>a<span class="ansi-blue-fg">,</span> b<span class="ansi-blue-fg">)</span><span class="ansi-blue-fg">:</span>
<span class="ansi-green-intense-fg ansi-bold">      2</span>     <span class="ansi-green-fg">try</span><span class="ansi-blue-fg">:</span>
<span class="ansi-green-fg">----&gt; 3</span><span class="ansi-red-fg">         </span><span class="ansi-green-fg">return</span> a <span class="ansi-blue-fg">/</span> b
<span class="ansi-green-intense-fg ansi-bold">      4</span>     <span class="ansi-green-fg">except</span> ZeroDivisionError <span class="ansi-green-fg">as</span> e<span class="ansi-blue-fg">:</span>
<span class="ansi-green-intense-fg ansi-bold">      5</span>         <span class="ansi-green-fg">raise</span> e

<span class="ansi-red-fg">ZeroDivisionError</span>: division by zero</pre>
</div>
</div>

</div>
</div>

</div>
    {% endraw %}

<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Raise different error type to be clearer that invalid value was supplied</p>

</div>
</div>
</div>
    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">divide</span><span class="p">(</span><span class="n">a</span><span class="p">,</span> <span class="n">b</span><span class="p">):</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">a</span> <span class="o">/</span> <span class="n">b</span>
    <span class="k">except</span> <span class="ne">ZeroDivisionError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s1">&#39;invalid inputs; division by zero is undefined&#39;</span><span class="p">)</span>
        
<span class="n">divide</span><span class="p">(</span><span class="mi">4</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">

<div class="output_subarea output_text output_error">
<pre>
<span class="ansi-red-fg">---------------------------------------------------------------------------</span>
<span class="ansi-red-fg">ZeroDivisionError</span>                         Traceback (most recent call last)
<span class="ansi-green-fg">&lt;ipython-input-5-b41638ecf455&gt;</span> in <span class="ansi-cyan-fg">divide</span><span class="ansi-blue-fg">(a, b)</span>
<span class="ansi-green-intense-fg ansi-bold">      2</span>     <span class="ansi-green-fg">try</span><span class="ansi-blue-fg">:</span>
<span class="ansi-green-fg">----&gt; 3</span><span class="ansi-red-fg">         </span><span class="ansi-green-fg">return</span> a <span class="ansi-blue-fg">/</span> b
<span class="ansi-green-intense-fg ansi-bold">      4</span>     <span class="ansi-green-fg">except</span> ZeroDivisionError <span class="ansi-green-fg">as</span> e<span class="ansi-blue-fg">:</span>

<span class="ansi-red-fg">ZeroDivisionError</span>: division by zero

During handling of the above exception, another exception occurred:

<span class="ansi-red-fg">ValueError</span>                                Traceback (most recent call last)
<span class="ansi-green-fg">&lt;ipython-input-5-b41638ecf455&gt;</span> in <span class="ansi-cyan-fg">&lt;module&gt;</span>
<span class="ansi-green-intense-fg ansi-bold">      5</span>         <span class="ansi-green-fg">raise</span> ValueError<span class="ansi-blue-fg">(</span><span class="ansi-blue-fg">&#39;invalid inputs; division by zero is undefined&#39;</span><span class="ansi-blue-fg">)</span>
<span class="ansi-green-intense-fg ansi-bold">      6</span> 
<span class="ansi-green-fg">----&gt; 7</span><span class="ansi-red-fg"> </span>divide<span class="ansi-blue-fg">(</span><span class="ansi-cyan-fg">4</span><span class="ansi-blue-fg">,</span> <span class="ansi-cyan-fg">0</span><span class="ansi-blue-fg">)</span>

<span class="ansi-green-fg">&lt;ipython-input-5-b41638ecf455&gt;</span> in <span class="ansi-cyan-fg">divide</span><span class="ansi-blue-fg">(a, b)</span>
<span class="ansi-green-intense-fg ansi-bold">      3</span>         <span class="ansi-green-fg">return</span> a <span class="ansi-blue-fg">/</span> b
<span class="ansi-green-intense-fg ansi-bold">      4</span>     <span class="ansi-green-fg">except</span> ZeroDivisionError <span class="ansi-green-fg">as</span> e<span class="ansi-blue-fg">:</span>
<span class="ansi-green-fg">----&gt; 5</span><span class="ansi-red-fg">         </span><span class="ansi-green-fg">raise</span> ValueError<span class="ansi-blue-fg">(</span><span class="ansi-blue-fg">&#39;invalid inputs; division by zero is undefined&#39;</span><span class="ansi-blue-fg">)</span>
<span class="ansi-green-intense-fg ansi-bold">      6</span> 
<span class="ansi-green-intense-fg ansi-bold">      7</span> divide<span class="ansi-blue-fg">(</span><span class="ansi-cyan-fg">4</span><span class="ansi-blue-fg">,</span> <span class="ansi-cyan-fg">0</span><span class="ansi-blue-fg">)</span>

<span class="ansi-red-fg">ValueError</span>: invalid inputs; division by zero is undefined</pre>
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
</ul>

</div>
</div>
</div>
</div>
 

