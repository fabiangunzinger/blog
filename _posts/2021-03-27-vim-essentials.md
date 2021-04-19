---
hide: false
toc: true
layout: post
description: my collection of vim commands to remember
categories: [vim]
title: vim essentials
---

# Setup

- I've remaped the Caps Look key to <Ctrl>.


# Mental models and reminders

- One keystroke to move, one to execute: e.g. the dot-formula (PV p. 11)
- Chunk your undos; all changes in single insert-mode session count as a single
    change, so go in and out of insert mode strategically.


- If you hit cursor keys more than 2 or 3 times, there is a better way.

- If you press backspace more than a couple times, there is a better way.

- If you perform the same change on several lines, there is a better way.



# Modes

## Normal mode


### Useful stuff

- `*` to highlight word under cursor. Use `n` and `N` to cycle forwards and
    backwards through matches.

- `<C-a>` and `<C-x>` to add and subtract from the next number.

- `<C-o>` to move backwards to the last location, `<C-l>` to move forward to next
  location.


### Move back and forth

Forwards    | Backwards | Effect
/           | ?         | Seach for pattern
*           | #         | Search for word under cursor
n           | N         | Jump to next search match
$           | ^         | Jump to end of line
f{char}     | F{char}   | Position cursor on {char}
t{char}     | T{char}   | Position cursor before {char}
;           | ,         | Repeat the last r, F, t, or T
w           | b         | Move to the start of the next word
W           | B         | Move to the start of the next WORD
}           | {         | Move down one (blank-line-separated) paragraph
gg                      | Jump to the first line of the document
G                       | Jump to the last line of the document





### Operators

- Operator + motion = action. E.g. `dl` deletes character to the right, `diw`
    the word under the cursor (without the surrounding whitespace), `dap` the current paragraph (including the surrounding whitespace). Similarly, `gUap`
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


### Entering insert mode

Trigger | Effect
i       | Insert before cursor
a       | Insert after cursor
I       | Insert at beginning of current line
A       | Insert at end of current line
o       | Insert in a new line below the current one
O       | Insert in a new line above the current one

- To enter insert mode to replace existing text, use `cc` to replace the
  current line, or `cc{motion}` as needed (e.g. `ci"` to replace text inside
  quotes).

## Insert mode

Useful keystrokes:
- `<C-w>` to delete last few words without leaving insert mode
- `<C-o>zz` to move current line to middle of screen without leaving insert mode

Keystroke           | Action
<C-h>               | Delete back one character (backspace)
<C-w>               | Delete back one word
<C-u>               | Delete back one line
<C-o>               | Switch to Insert Normal mode (to execute a single Normal
Mode command)
<C-r>{register}     | Paste content from address (use 0 for last yanked text)
<C-r>=              | Perform calculation in place
r, R                | Enter replace mode for single replacement or until exit





## Visual mode

## Command-line mode

### Ex commands

- basic syntax: [range]command


# Sources

- [Practical
    Vim (PV)](https://pragprog.com/titles/dnvim2/practical-vim-second-edition/)
