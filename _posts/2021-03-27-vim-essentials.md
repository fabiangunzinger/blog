---
toc: true
hide: false
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

# Approach to problem solving

- Don't solve a problem unless I come across it frequently.

- Check whether one of Tim Pope's plugins solves the problem (chances are oen
  of them does).



# Modes

## Normal mode

- Operators work as follows: operator + motion = action. E.g. `dl` deletes character to the right, `diw`
    the word under the cursor (without the surrounding whitespace), `dap` the current paragraph (including the surrounding whitespace). Similarly, `gUap`
    converts the current paragraph to uppercase.

Common operators:

Trigger   | Effect
`c`       | Change
`d`       | Delete
`y`       | Yank into register
`g~`      | Swap case
`gu`      | Make lowercase
`gU`      | Make uppercase
`>`       | Shift right
`<`       | Shift left
`=`       | Autoindent
`!`       | Filter {motion} lines through an external program

Move back and forth:

Forwards    | Backwards | Effect
/           | ?         | Seach for pattern
*           | #         | Search for word under cursor
n           | N         | Jump to next search match
$           | ^         | Jump to end of line
f{char}     | F{char}   | Position cursor on {char}
t{char}     | T{char}   | Position cursor before {char} (search till char)
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
`C` | `c$` (delete until end of line and start insert)
`D` | `d$` (delete until end of line)
`s` | `cl` (delete single character and start insert)
`S` | `^c` (delete entire line and start inster, synonym for `cc`)
`I` | `^i` (jump to beginning of line and start insert)
`A` | `$a` (jumpt to end of line and start insert)
`o` | `A<cr>`
`O` | `ko`

Miscellaneous:

Command             | Effect
`<C-a>`/ `<C-x>`    | Add / subtract from the next number
`<C-o>`/ `<C-l>`    | Move backwards to last / forward to previous location
`u`/`<C-r>`         | Undo / redo change
`ga`                | Reveal numeric representation of character under cursor


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

Keystroke            | action
`<c-h>`              | delete back one character (backspace)
`<c-w>`              | delete back one word
`<c-u>`              | delete back one line
`<c-o>`              | Enter insert normal mode to execute a single normal cmd
`<C-r>{register}`    | Paste content from address (use 0 for last yanked text)
`<C-r>=`             | Perform calculation in place
`r,` `R`             | Enter replace mode for single replacement or until exit
`<C-v>{123}`         | Insert character by decimal code 
`<C-v>u{1234}`       | Insert character by hexadecimal code 
`<C-v>{char1}{char2}`| Insert character by digraph


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


# Files

Setting the working directory:

Command             | Effect
`:pwd`              | Show current directory window
`:cd`               | Set directory for all windows
`:lcd`              | Set directory for current window
`:tcd`              | Set directory for current tab

## Buffers

- A buffer is an in-memory representation of a file.

- A hidden buffer is one that contains changes you haven't written to disk
  yet but switched away from. For a session with hidden buffers, quitting will
  raise error messages, and vim will automatically display the first hidden
  buffer. You now have the following options: `:w[rite]` to write the buffer's
  content to disk, `:e[dit]!` to reread the file from disk and thus revert all
  changes made, `:qa[ll]!` to discard all changes, and `:wa[ll]` to write all
  modified buffers to disk.

- `:bufdo` executes an Ex command in all open buffers, `:argo` in all grouped
  ones (e.g. `:argdo %s/hello/world/g` substitutes `world` for `hello` in all
  buffers in `:args`, `:argdo edit!` reverts all changes, and `:argdo update`
  writes changed buffers to disk.

- `:[range]bd` deletes buffers in range, with `[range]` working as for other
  Ex-commands (see above).


## Windows 

- A window is a viewport onto a buffer. We can open different windows that all
  provide a (different) view onto the same buffer, or load multiple buffers into
  one window.

Command             | Effect
`<C-w>s`            | Split window horizontally
`<C-w>v`            | Split window vertically
`:sp[lit] {file}`   | Horizontally split window and load {file} into new buffer
`:vsp[lit] {file}`  | Vertically split window and load {file} into new buffer
`on[ly]`            | Close all but current window
`<C-w>=`            | Equalize width and height of all windows
`<C-w>r`            | Rorate windows
`<C-w>x`            | Exchange position of current window with its neighbour
`q[uit]`            | Close current window
`:vert sb N`        | Open buffer number N in vertical split


## Tabs

- A tab is a container of windows.

Command             | Effect
`:tabe[dit]{file}`  | Open new tab with {file} if specified or empty otherwise
`<C-w>T`            | Move current window into new tab
`:tabc[lose]`       | Close current tab with all its windows
`:tabo[nly]`        | Close all tabs but the current one
`{N}`gt             | Go to tab {N} if specified, or to next otherwise
`gT`                | Go to previous tab

## Opening files

- To easily open a new file from the same directory as the current buffer in a
  new window/split/vertical split/tab I use the mappings `<leader>ew/es/ev/et`,
  following [this](http://vimcasts.org/episodes/the-edit-command/) Vimcast.

- To navigate file trees, I use `netrw` and `vinegar`.

- Deleting folders: `netrw` uses `delete()` with the `d` flat to delete
  directories. As explained in `:h delete()`, this only removes empty
  directories. I leave this default for now.

`netrw` commands:

Command             | Effect
`e[dit].`           | Open file explorer for current working directory
`E[xplore]`         | Open file explorer for the directory of active buffer
`%`                 | Open new file in current directory
`d`                 | Create new directory in current one
`R`                 | Rename file or directory under cursor
`D`                 | Delete file or directory under cursor


# Moving

- Motions move within a file, jumps between files.

- Learn more motions by working your way through `:h motion.txt`


General:

Command             | Effect
`<C-g>`             | Shows current filepath and line number


Lines:

Command             | Effect
`g{line-motion}`    | Move by display rather than real line (e.g. `gj` vs `j`)
`j`/`k`             | Down/up one line (think of `j` as a down arrow)
`0`/`^`/`$`         | To first non-blank/first/last character of line.

Words:

Command             | Effect
Capital w/e/b below | Move WORD rather than word wise
`w`/`e`             | Forward to start/end of current or next word
`b`/`ge`            | Backward to start/end of current or previous word

Search:

Command             | Effect
`f{char}`\`F{char}` | Forward/backward to next occurrence of {char}
`t{char}`\`T{char}` | Forward/backward till (before) next occurrence of {char}
`f,dt.`             | Useful example: deletes the last clause of a sentence

Some sentence out of which I delete unneeded words without fuss.




# Extra functionality and awesome plugins

## vim-unimpaired

- Provides a set of normal mode commands to move between **next** (`]`) and **previous**
  (`[`), toggle **options**, and special **pasting**. Some commands I use often
  are listed below.

- `]<space>` adds [count] blank lines below the cursor; `[<space>`, above the
  cursor. Mnemonic: `]` is next, here the next line, which is the line below.

- `]e` exchanges the current line with the line below; `[e`, with the line above.

- `yob` toggles light background, `yoc` the cursor line, `yon` line numbers,
  `yor` relative line numbers, `yos` the spell checker.




## Python 

## Snippets

## Latex integration

No plugins:

- You can use `<C-N>` completion for words that already appear in one of the
  open buffers. This is especially useful for bibliography completion: just open
  the .bib file in another buffer and `<C-N>` will provide a list of
  available keys.

[vimtex](https://github.com/lervag/vimtex)

- Most shortcuts use `localleader`, which, by default, is set to `\`.
- I use `skim` as my viewer.

- `\ll` toggles continuous compilation using `latexmk`.

Command             | Effect
`\ll`               | Toggle continuous compilation using `latexmk`
`<C-x><C-o>/`       | Citation completion (inside `\cite{`)


# Sources

- [Practical
    Vim (PV)](https://pragprog.com/titles/dnvim2/practical-vim-second-edition/)
