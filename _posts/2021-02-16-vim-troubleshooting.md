---
hide: false
title: Vim troubleshooting
---

# Vim troubleshooting

## CSS indent not working
- Vim recognised css files, but used my global indent of 4 spaces rather than
    a file-type specific indent of 2 spaces.
- `h: filetype` notes that filetype detection files are located in the
    runtime path. Going there, I found the `ftplugins` folder that contains the
    default file settings. Looking at `css.vim` makes clear that it doesn't set
    any tabstop settings, which explains why the defaults were used.
- Googling something along the lines of "custom filetype indent vim" let me to
    [this](https://stackoverflow.com/a/159066) SO answer, which helpfully links
    to `h: filetype-plugins`. Once there, it was easy to find the relevant
    section, `ftplugin-overrule` that documents how to add custom filetype
    settings. This is what I did, and it worked like a charm.
