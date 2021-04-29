---
hide: false
toc: true
layout: post
description: My data workflow
categories: [principles]
title: My data workflow 
---

# Conda

- I create a separate environment for each major project.

- For smaller projects, I use generic Python version environment that I create
  for each major Python update and name accordingly (e.g. `python3.9`). When I
  start a small project, I use the latest generic environment and export the
  `environment.yml` to the project folder so I can reproduce the repo in the
  future (e.g. after I've added/updated packages).


# GitHub

- For each dataset I work with, I have a separate GitHub repo (named
  `data-NAME`) which contains
  code to minimally clean the data so as to create a version of the data that I
  can then use for all projects in which I use the data, the data documentation,
  and any thoughts and notes pertaining to the data (e.g. known limitations,
  additional information from the data provider, etc.).


