---
keywords: fastai
title: Feature engineering
hide: false
toc: true
comments: true
categories: [ml]
nb_path: _notebooks/2020-03-05-feature-engineering.ipynb
layout: notebook
---

<!--
#################################################
### THIS FILE WAS AUTOGENERATED! DO NOT EDIT! ###
#################################################
# file to edit: _notebooks/2020-03-05-feature-engineering.ipynb
-->

<div class="container" id="notebook-container">
        
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="General-points">General points<a class="anchor-link" href="#General-points"> </a></h2><ul>
<li>Having many uninformative features in your model might lower performance as it makes is more likely that the model overfits (e.g. including country names when predicting life satisfaction and using OECD sample finds that "w" in country name predicts high life satisfaction because of Norway, Switzerland, New Zealand, and Sweden. But this doesn't generalize to Rwanda and Zimbabwe). Hence, the more uninformative features, the bigger the chance that the model will find a pattern by chance in one of them in your training set.</li>
</ul>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Process-in-practice">Process in practice<a class="anchor-link" href="#Process-in-practice"> </a></h2><ol>
<li>Brainstorm features</li>
<li>Decide what features to create</li>
<li>Create the features</li>
<li>Test impact on model performance</li>
<li>Interacting on features is useful</li>
<li>Iterate (go to 3 or 1)</li>
</ol>
<p>Stuff to try:</p>
<ul>
<li>Ratios</li>
<li>Counts</li>
<li>Cutoff points</li>
<li>Iterate on features (change cutoff and see whether it makes a difference) </li>
<li>Rate of Change in Values</li>
<li>Range of Values</li>
<li>Density within Intervals of Time</li>
<li>Proportion of Instances of Commonly Occurring Values</li>
<li>Time Between Occurrences of Commonly Occurring Values</li>
</ul>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Data-processing">Data processing<a class="anchor-link" href="#Data-processing"> </a></h2><ul>
<li><p>Data transformations for individual predictors</p>
</li>
<li><p>Data transformations for multiple predictors</p>
</li>
<li><p>Dealing with missing values</p>
</li>
<li><p>Removing predictors</p>
</li>
<li><p>Adding predictors</p>
</li>
<li><p>Binning predictors</p>
</li>
</ul>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Measuring-predictor-importance">Measuring predictor importance<a class="anchor-link" href="#Measuring-predictor-importance"> </a></h2><ul>
<li><p>Numeric outcomes</p>
</li>
<li><p>Categorical outcomes</p>
</li>
<li><p>Other approaches</p>
</li>
</ul>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Feature-selection">Feature selection<a class="anchor-link" href="#Feature-selection"> </a></h2><ul>
<li><p>Consequences of using non-informative predictors</p>
</li>
<li><p>Approaches for reducing the number of predictors</p>
</li>
<li><p>Wrapper methods</p>
</li>
<li><p>Filter methods</p>
</li>
<li><p>Selection bias</p>
</li>
</ul>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Factors-that-can-affect-model-performance">Factors that can affect model performance<a class="anchor-link" href="#Factors-that-can-affect-model-performance"> </a></h2><ul>
<li><p>Type III errors</p>
</li>
<li><p>Measurement errors in the outcome</p>
</li>
<li><p>Measurement errors in the predictors</p>
</li>
<li><p>Distretising continuous outcomes</p>
</li>
<li><p>When should you trust your model's prediction?</p>
</li>
<li><p>The impact of a large sample</p>
</li>
</ul>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Resources">Resources<a class="anchor-link" href="#Resources"> </a></h1><ul>
<li><a href="http://appliedpredictivemodeling.com">Applied predictive modeling</a></li>
<li><a href="https://www.youtube.com/watch?time_continue=109&amp;v=drUToKxEAUA&amp;feature=emb_logo">video</a></li>
<li>mlmastery <a href="https://machinelearningmastery.com/discover-feature-engineering-how-to-engineer-features-and-how-to-get-good-at-it/">article</a></li>
</ul>

</div>
</div>
</div>
</div>
 

