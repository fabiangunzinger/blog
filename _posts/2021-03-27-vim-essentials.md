---
hide: false
toc: true
layout: post
description: my collection of vim commands to remember
categories: [vim]
title: vim essentials
---

# Mental models

- One keystroke to move, one to execute: e.g. the dot-formula (PV p. 11)
- Chunk your undos; all changes in single insert-mode session count as a single
    change, so go in and out of insert mode strategically.


# Modes

## Normal mode

- `*` to highlight word under cursor. Use `n` and `N` to cycle forwards and
    backwards through matches.
- `<C-a>` and `<C-x>` to add and subtract from the next number.

### Operators

- Operator + motion = action. E.g. `dl` deletes character to the right, `diw`
    the word under the cursor, `dap` the current paragraph. Similarly, `gUap`
    converts the current paragraph to uppercase.


Trigger | Effect
c       | Change
d       | Delete
y       | Yank into register
g~      | Swap case
gu      | Make lowercase
gU      | Make uppercase
>       | Shift right
<       | Shift left
=       | Autoindent
!       | Filter {motion} lines through an external program


### Act, repeat, reverse

Intent                              | Act               | Repeat    | Reverse
Make a change                       | {edit}            | .         | u
Scan line for next character        | f{char}/t{char}   | ;         | ,
Scan line for previous character    | F{char}/T{char}   | ;         | ,
Scan document for next match        | /pattern<CR>      | n         | N
Scan document for previous match    | ?pattern<CR>      | n         | N
Perform substitution                | :s/old/new        | &         | u
Execute a sequence of changes       | qx{change}q       | @x        | u




### Compound commands

Compound command | Equivalent in longhand
C | c$
s | cl
S | ^C
I | ^i
A | $a
o | A<cr>
O | ko


## Insert mode

## Visual mode

## Command-line mode

### Ex commands

- basic syntax: [range]command


# Sources

- [Practical
    Vim (PV)](https://pragprog.com/titles/dnvim2/practical-vim-second-edition/)
