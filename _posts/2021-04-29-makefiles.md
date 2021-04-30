---
hide: false
toc: true
layout: post
description: Basics of writing makefiles
categories: [tools]
title: Makefiles
---

- A makefile is a data base that tells the `make` utilit how to recompile a
  system. In the default use case, `$: make` recompiles any changed files and
  any files that depend on them. In the way I use makefiles, `$: make <rule>`
  executes a predefined rule to accomplish a certain task like cleaning a
  particular dataset.
  
- Rules consist of a target (the name of a file to be modified), prerequisits
  (other files on which the target depends on), and commands to be run in order
  to update the traget based on changes in the prerequisits.

- A rule tells `make` when a target is out of date and how to update it. A
  target is out of date if it doesn't exist or is older then one of its
  prerequisite files.

- If a target is an action to be performed rather than a file to be updated,
  then it's called a `phony target`.

- A normal prerequisite makes both an *order statement* and a *dependency statement*:
  the order statement ensures that all commands needed to produce the
  prerequisete are fully executed before any commands to produce the target,
  while the dependency statement ensures that target updated every time a
  prerequisite changes. Occasionally, we want a prerequisite to invoke the order without the
  dependency statement (i.e. target is not udpated when the prerequisite
  changes, but when target is being updated, then the prerequisite commandas are
  run first). We can do this by writing the rule as `target:
  normal-prerequisites | order-only-prerequisites`.

- Variables are defined using `<varname> = <content>` and called using
  `$(varname)`.

- `make` does its work in two phases: during the *read-in* phase, it reads the
  makefile and internalises variables and rules to construct a dependency graph
  of all targets and their prerequisies; during the *target-update* phase, it
  determines what rules to update in what order and executes the commandas to do
  so.

- As a result, variable and function expansion can happen either *immediately*
  (during the read-in phase) or *deferred* (after the read-in phase). Variables
  defined as `varname := value` get parsed immediately, for those defined as
  `varname = value` parsing is deferred. 

- To define a variable containing all csv files in a directory, do `csvs :=
  $(wildcard *.csv)`. The `wildcard` function is needed here so that the
  wildcard gets expanded during funciton creation (as opposed to creating the
  variable with value `*.csv`). Based on `csvs`, I could also create a list
  containing the same files but with a parquet extensions like so: `parqs :=
  $(patsubst %.csv,%.parquet,$(wildcard *.csv)). 

- Automatic variables: `$^` is a list of all prerequisites, `$@` is the target,
  `$<` the first prerequisite.

