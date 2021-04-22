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

- If you hit cursor keys more than 2 or 3 times, there is a better way. If you press backspace more than a couple times, there is a better way. If you perform the same change on several lines, there is a better way.


# Modes

## Normal mode

- Operators work as follows: operator + motion = action. E.g. `dl` deletes character to the right, `diw`
    the word under the cursor (without the surrounding whitespace), `dap` the current paragraph (including the surrounding whitespace). Similarly, `gUap`
    converts the current paragraph to uppercase.

Common operators:
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

Move back and forth:
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

Act, repeat, reverse:
Intent                              | Act               | Repeat    | Reverse
Make a change                       | {edit}            | .         | u
Scan line for next character        | f{char}/t{char}   | ;         | ,
Scan line for previous character    | F{char}/T{char}   | ;         | ,
Scan document for next match        | /pattern<CR>      | n         | N
Scan document for previous match    | ?pattern<CR>      | n         | N
Perform substitution                | :s/old/new        | &         | u
Execute a sequence of changes       | qx{change}q       | @x        | u

Compound commands:
Compound command | Equivalent in longhand
C | c$
s | cl
S | ^C
I | ^i
A | $a
o | `A<cr>`
O | ko

Miscellaneous:
Command             | Effect
`<C-a>`/ `<C-x>`    | Add / subtract from the next number
`<C-o>`/ `<C-l>`    | Move backwards to last / forward to previous location
`u`/`<C-r>`         | Undo / redo change
`ga`                | Reveal decimal, octal, hex representation of character
under cursor.


## Insert mode

- To enter insert mode to replace existing text, use `cc` to replace the
  current line, or `cc{motion}` as needed (e.g. `ci"` to replace text inside
  quotes).

- `<C-w>` to delete last few words without leaving insert mode

- `<C-o>zz` to move current line to middle of screen without leaving insert mode

Entering insert mode:
Trigger | Effect
i       | Insert before cursor
a       | Insert after cursor
I       | Insert at beginning of current line
A       | Insert at end of current line
o       | Insert in a new line below the current one
O       | Insert in a new line above the current one

Useful commands:
Keystroke               | Action
`<C-h>`                 | Delete back one character (backspace)
`<C-w>`                 | Delete back one word
`<C-u>`                 | Delete back one line
`<C-o>`                 | Switch to Insert Normal mode (to execute a single Normal
Mode command)
`<C-r>{register}`       | Paste content from address (use 0 for last yanked text)
`<C-r>=`                | Perform calculation in place
`r,` `R`                | Enter replace mode for single replacement or until exit
`<C-v>{123}`            | Insert character by decimal code 
`<C-v>u{1234}`          | Insert character by hexadecimal code 
`<C-v>{char1}{char2}`   | Insert character by digraph


## Visual mode

Entering visual mode:
Command  | Effect
v        | Enter character-wise visual mode
V        | Enter line-wise visual mode
`<C-v>`  | Enter block-wise visual mode
gv       | Reselect last visual selection
o        | Toggle the free end of a selection


## Command-line mode

- Ex-commands allow you to make changes (in multiple places) anywhere in
  the file without moving the cursor -- they strike far and wide.

- The general syntax for Ex-commands is `:[range]{command}`, where `[range]` is
either a single address or a range of addresses of the form `{start},{stop}`. There are three types of addresses: line numbers, visual selections, and
patterns.

- To execute a command on all selected lines, use visual mode to make the
selection and press `:`. This will start the command prompt with `'<, '>:`, to
which you can then add the command.

- We can also specify offsets. For example, `:/<tag>/+1<\/tag>/-1{cmd}` would
operate on the lines inside the html tag but not the lines containing the tag
marks.

- To wrap all elements in the first column of a table in quotes, I could
  use `:{start},{stop}normal ysaW'`.

- `<C-r><C-w>` inserts the word under the cursor in the command prompt. Can be
  useful for substitution (cursor to word, `*`, `cw{new}<Esc>`,
  `:%s//<C-r><C-w>/g`) or to get vim help for word under cursor (`:h
  <C-r><C-w>`).

- `<C-z>` puts vim in the background and returns to bash, `fg` returns back to
  vim.

Types of addresses:
Command                     | Effect
`:4{cmd}`                   | execute command on line 4
`:4,8{cmd}`                 | execute command on lines 4 to 8 (inclusive)
`:/#/{cmd}`                 | execute command on next line with an `#`
`:/<tag>/<\/tag>/{cmd}`     | Execute command inside next occurring html tag
`:'<,'>{cmd}`               | Execute command on selected lines

Useful address/range characters:
Symobol | Address
`1`       | First line of the file
`$`       | Last line of the file
`0`       | Virtual line above first line (e.g. to paste to top of file)
`.`       | Line of cursor
`'m`      | Line containing mark m
`'<`      | Start of visual selection
`'>`      | End of visual selection
`%`       | The entire file (short for :1,$)

Common Ex-commands: 
Command       | Effect
p[rint]       | Print
d[elete]      | Delete
j[oin]        | Join lines
s[ubstitute]  | Substitute (e.g. `s/old/new`)
n[ormal]      | Execute normal mode command
m[ove]        | Move to `{address}`, (e.g. `:1,5m$` moves lines to end of file)
copy (or t)   | Copy to `{address}`, (e.g. `:6t.` copies line 6 to current line)


# Extra functionality

## Python 

## Snippets

## Latex integration

- You can use `<C-N>` completion for words that already appear in one of the
  open buffers. This is especially useful for bibliography completion: just open
  the .bib file in another buffer and `<C-N>` will provide a list of
  available keys.


# Sources

- [Practical
    Vim (PV)](https://pragprog.com/titles/dnvim2/practical-vim-second-edition/)
