hide: true
layout: post
categories: [tools]
title: bash-scripts
---

# Notes from [Ryan's tutorial](https://ryanstutorials.net/bash-scripting-tutorial/)

Basics and variables
- A process is a running instance of a program.
- `'` interpret all content literally, `"` allow for variable substitution.
- `$( command )` saves command output into a variable.
- `export var` makes `var` available to child process.
- `/dev/stdin` reads input from pipe.

Arithmetic
- `let` assigns result of expression to a variable.
- `expr` prints result of expression.
- `$(( expression ))` returns the result of expression.
- `${#var}` returns the length of `var` in characters.

Functions
- `function_name () {
     <commands>
   }` 
   is the basic format (there is also `function function_name {`, but I prefer this.






