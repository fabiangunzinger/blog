---
toc: true
hide: false
layout: post
description: my collection of vim commands to remember
categories: [vim]
title: vim essentials
---

# Intro

## Acknowledgements

This cheat sheet started out as a summary of Drew Neil's phenomenal [Practical
Vim](https://pragprog.com/titles/dnvim2/practical-vim-second-edition/), which I
can't recommend enough as a start to learning Vim seriously.


## Vim setup

- I've remaped the Caps Look key to <Ctrl>.


## Mental models and reminders

- One keystroke to move, one to execute: e.g. the dot-formula (PV p. 11)

- Chunk your undos; all changes in single insert-mode session count as a single
    change, so go in and out of insert mode strategically.

- If you hit cursor keys more than 2 or 3 times, there is a better way. If you press backspace more than a couple times, there is a better way. If you perform the same change on several lines, there is a better way.


## Approach to problem solving

- Don't solve a problem unless I come across it frequently.

- Check whether one of Tim Pope's plugins solves the problem (chances are oen
  of them does).


# Miscellaneous

Command             | Effect
`set: {cmd}?`       | Show present setting for {cmd}



# Modes

## Normal mode

- Operators work as follows: operator + motion = action. E.g. `dl` deletes character to the right, `diw`
    the word under the cursor (without the surrounding whitespace), `dap` the current paragraph (including the surrounding whitespace). Similarly, `gUap`
    converts the current paragraph to uppercase.

Common operators:

Trigger   | Effect
`c`       | Change
`d`       | Delete into register
`y`       | Yank into register
`p`       | Paste after cursor
`P`       | Paste before cursor
`~`       | Swap case of character under cursor and move right
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
`C` | `c$` (delete from cursor until end of line and start insert)
`D` | `d$` (delete from cursor until end of line)
`Y` | `y$` (similar to above, but has to be manually mapped, see `h: Y`)
`s` | `cl` (delete single character and start insert)
`S` | `^c` (delete entire line and start inster, synonym for `cc`)
`x` | `dl` (delete one character to the right)
`X` | `dh` (delete one character to the left)
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


# Navigation

- Motions move within a file, jumps between files.

- Each motion can be prepended by a count (`5l` moves five characters to the
  right).


## Within files

General:

Command             | Effect
`<C-g>`             | Shows current filepath and line number
`zz`                | Redraw current line in middle of window
`zt`                | Redraw current line at top of window

Left-right and up-down:

- `f,dt` deletes the last clause of a sentence
- You can use search after an operator to great effect. For instance: typing
  `d\to g<CR>` when the cursor is at the beginning of `after` in the previous
  sentence turns it into "You can use search to greate effect". This works
  because `d` is an exclusive operator (`h: exclusive`) and doesn't apply the
  operation on the endpoint of the selection.

Command             | Effect
`h`/`l`             | Move left/right 
`j`/`k`             | Down/up one line (think of `j` as a down arrow)
`gj`/`gk`           | Down/up by display rather than real lines
`0`/`^`/`$`         | To first non-blank/first/last character of line
`G`                 | Goto line `[count]`, default is last line
`gg`                | Goto line `[count]`, default is first line
`f{char}`\`F{char}` | Forward/backward to next occurrence of {char}
`t{char}`\`T{char}` | Forward/backward till (before) next occurrence of {char}
`H`/`M`/`L`         | Jump to the top/middle/bottom of the screen
`<C-e>`/`<C-y>`     | Scroll down/up linewise
`<C-d>`/`<C-u>`     | Scroll down/up half-screen-wise 


Words:

Command             | Effect
`w`/`e`             | Forward to start/end of current or next word
`b`/`ge`            | Backward to start/end of current or previous word
Capital w/e/b       | Move WORD rather than word wise


Text objects:

- Text objects come in two types: those within a pair of delimiters (e.g. text
  inside parentheses) and chucks of text (Vim calls them "block" and "non-block"
  objects).

- They can be moved over or selected.

- Text object selection start with `i` (inside) or `a` (around). For example: `vi)`
  highlights text inside parentheses but not the parentheses themselves, while `va)`
  highlights the parentheses as well.

Command             | Effect
`)`/`(`             | Move [count] sentences forward/backward
`}`/`{`             | Move [count] paragraphs forward/backward


Command             | Select inside or around...
`w`/`W`             | word/WORD
`s`                 | sentence
`p`                 | paragraph
`]`                 | a [] block
`)` or `b`          | a () block
`}` or `B`          | a {} block
`<`                 | a <> block
`t`                 | a tag block
`` ` ``/`'`/`"`     | a ``` `` ```/''/"" block

Marks:

Command             | Effect
`m{a-zA-Z}`         | Set lowercase (local) or uppercase (global) mark
`` `{mark} ``       | Jump to mark
``` `` ```          | Go to position before last jump
`` `. ``            | Go to position of last change
`%`                 | Go to matching bracket


## Between files

Traversing the jumps and changes lists

- A jump is a long-range motion (which, roughly, means moving faster than
  WORD-wise).

Command             | Effect
`:jumps`            | Show the jump list
`<C-o>` / `<C-i`>   | Traverse jump history backwards/forwards
`:changes`          | Show the change list
`g;`/`g,`           | Traverse change list backwards/forwards
`gf`                | Jump to file under cursor
`<C-]>`             | Jump to definition of keyword under cursor


# Registers

## Copy and paste

- A register is a container that holds text. By default, Vim deletes, yanks and
  puts to and from the `unnamed` register `"`. We can set the register with with
  a command interacts by prepending the command with `"{register}{cmd}` (e.g. to
  explicitly state that we want to delete the current line to the unnamed register, we'd use
  `""dd`; to put the just copied text, `""p`. But theser are equivalent to `dd`
  and `p`, so we'd probably not do that.)

- Transposing characters and lines: to correct "Thi sis", starting from the last letter, use `F<space>xp`; to swap the current with the subsequent line, use `ddp`. (As an alternative to `ddp`, which is useful to move lines up and down more flexibly, use `]e` from `vim-unimpaired` (see below).

- Expression register: when we fetch the content of the expression register, Vim drops into
  command-line mode with a `=` prompt. When we enter Vim script and press
  `<CR>`, Vim will coerce the result into a string if possible and use it.


Command             | Effect
`"{reg}{cmd}`       | Make {cmd} interact with register {reg}
`""`                | The unnamed register (redundant, as it's the default)
`"o`                | The yank register
`"_`                | The black hole register (nothing returns from it)
`"{a-z}`            | Named registers (replace with {a-z}, append with {A-Z})
`"+`                | The system clipboard
`"%`                | Name of current file (e.g. `"%p`)
`"#`                | Name of alternate file
`".`                | Last inserted text
`":`                | Last Ex command
`"/`                | Last search pattern
`:reg "0`           | List content of unnamed and yank register
`<C-r>{reg}`        | Paste content of {reg} in insert mode


## Macros

Command             | Effect
`q{a-z}`            | Start recording macro to register
`q`                 | End recording
`[count]@{a-z}`     | Invoke macro in register [count] times
`@@`                | Replay last invoked macro
`q{A-Z}`            | Append to macro (e.g. if I forgot something)


- We can execute macros *in sequence* (e.g. `22@a`) or *in parallel* (`jVG:normal
  @a`). The former can be useful as it aborts on failure, which could be what we
  want (e.g. replace all search results). But if it's not, then the latter approach is more useful (example: you
  want to repeat a change in a line for all lines that follow a certain pattern,
  e.g. are list items, but not other lines). See examples below.


Useful patterns:

- Macro `q` hits its target with `n`; invoke it quickly for all 12 search
  results in the document. Solution: `22@q`. Explanation: Because `q` uses `n`
  to hit its targets, it will automatically abort once there are no more
  results. We can thus avoid counting matches and simply use a number that's
  comfortably above the number of matches. 22 is convenient because, on my
  keyboard, it's the same key as @.

- Repeate a `;.`-pattern 7 times. Solution: `qq;.q22@q`. Explanation: `22;.` or
  `:22.` wouldn't work because they would each repeat the immediately following
  step only, so we need to store the whole pattern as a macro, which we can then
  invoke mutiple Times (logic of 22 is same as above).

- In the list below, change `.` to `)` and words to uppercase. Solution: start
  with cursor anywhere on first line; `qq0`; `f.`; `r)`; `w~`; `jq`; `j@q`.

1. ho
2. hi
12. he

- Do the same but for the new list below. Solution: start anywhere on first
  line; `qq0f.r)w~q`; `jV}`; `:normal @q`. Explanation: while above solution
  executes macro *in series*, this one executes it *in parallel*, which is
  required here because the serial approach would abort execution at the
  comment.

1) ho
2. hi
// a comment
12. he

- Turn the below lines into a numbered list. Solution: start anywhere on the
  first line; `let i=1`; `qq0cl<C-r>=i<CR>)<Esc>`; `let i+=1`; `q`; `jVj:normal
  @q`.

- first
- second
- third


# Patterns

## Matching patterns and literals

- In my `.vimrv`, I use `set: ignorecase` and `set: smartcase` to set the
  default search to be case insensitive except when I use an uppercase character
  in my pattern.

- You can use pattern swtiches anywhere in the search pattern. 

- Use `\v` for regex search, `\V` for verbatim search.


Pattern switch      | Effect
`\c`                | Force case insensitive search
`\C`                | Force case sensitive search
`\v` (very magic)   | All characters assume special meaning (regex-like)
`\V` (very nomagic) | No character (except `\`) has special meaning
`%`                 | When prepending `()`, don't capture submatch
`<`/`>`             | Word boundaries when used with `\v` switch
`\zs`/`\ze`         | Start and end of match


Useful patterns:

- Find `the` but not words it is a part of (e.g. `these`). Solution:
  `/\v<the><CR>`.

- In a CSS file, find all hex colour codes. Solution: `/\v#(\x{6}|\x{3})`.
  Explanation: use `\v` for regex search and `\x` to capture hexadecimal
  characters (equivalent to `[0-9a-fA-F]`).

- Find "a.k.a." in a file. Solution: `/\Va.k.a.`. Explanation: we need `\V`
  or else `.` matches any character and we'd also find words like "backwards".

- Check for words that occurr twice in a row. Solution: `/\v(\w+)\_s+\1`.
  Explanation: `(\w+)` captures any word, `\_s` matches a linebreak or a space
  (see `h: /\_`), and `\1` is the reference to the previously captured word.

- Reverse the order of all occurrences of `Fab Gunzinger` and `Fabian
  Gunzinger`. Solution: `/(Fa%(b|bian)) (Gunzinger)`; `:%s//\2, \1/g`.
  Explanation: the first bit captures the short and full version of my first
  name, and my my last name, without capturing the `b` or `bian` fragments.
  First and last name can now be references using `\1` and `\2`, respectively.
  The substitution command finds the last search pattern (since we leave pattern
  blank) and replaces it with my first and last names reversed.

- Find all occurences of "Vim" that are part of "Practical Vim". Solution:
  `/Practical \zsVim<CR>`.

- Find all quoted text. Solution: `/\v"\zs[^"]+\ze"`. Explanation: `"[^"]+"`
  matches quotes followed by one or more occurances of anything but quotes
  followed by quotes (this is a useful regex idiom). `\zs` and `\ze` exclude the
  quotes from the match.

- Find `http://someurl.com/search?=\//`. Solution: Yank pattern into a register,
  `u` for url, say; `/\V<C-r>=escape(@u, getcmdtype().'\')<CR>`. Explanation:
  see tip 79 in PV.

## Search

Command             | Effect
`/<CR>`             | Search previous pattern forward
`?<CR>`             | Search previous pattern backwards
`/<UP>`             | Access search history (similar for backward search)





## Substitution

## Global commans



# Common patterns

- Replace firstword with secondword. Solution 1: cursor at beginning of
  secondword;
  `ye`; `bb`; `ve`; `p`. Solution 2: cursor at beginning of secondword; `ye`;
  `bb`; `cw`; `<C-r>0`. Has advantage that `.` now replaces current word with
  `firstword`. 

- Swap firstword and secondword. Solution: cursor at beginning of firstword;
  `de`; `mm`; `ww`; `ve`; `p`; `` `m ``; `P`. Explanation: this exploits a quirk
  in the behaviour or `p` in visual mode. When we paste in visual mode, we put
  the content of the default register in place of the highlighted text, and the
  highlighted text into the default register.

- Complete the statement 27 * 45 = x. Solution: cursor at x and in insert
  mode; `<C-r>=27*45<CR>`.


# Common issues

- I want to open a file and get an `E325: ATTENTION Found a swap file` warning.
  What happened? For me, it's most likely I accidentally closed a terminal
  window while still editing the file. What to do? First, check that I'm not already editing the file elsewhere. Second, recover the file, save it under a new name (`:w filename2`), force quit the session, compare the original and the new file (`diff filename filename2`), use the file with the content I need and delete the other one and the swap file. (Based on [this](https://superuser.com/a/498658) great SE answer.)


# Extra functionality and awesome plugins

## vim-unimpaired

- Provides a set of normal mode commands to move between **next** (`]`) and **previous**
  (`[`), toggle **options**, and special **pasting**. Some commands I use often
  are listed below.

- The mnemonic is that `]` is next in general and "next line" here.

Command                 | Effect
`]<space>`/`[<space>`   | Add [count] blank lines below/above the cursor
`]e`/`[e`               | Exchanges the current line with the one below/above
`yob`                   | Toggle light background
`yoc`                   | Toggle cursor line highlighting
`yon`                   | Toggle line numbers
`yor`                   | Toggle relative line numbers
`yos`                   | Toggle the spell checker


## vim-surround

## Python 

- Look into using `matchit` or something similar for faster code navigation.

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
