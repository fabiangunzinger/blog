---
hide: false
toc: true
layout: post
description: My collection of essential Git commands
categories: [git]
title: Git(Hub) essentials
---


# Workflow



- Create an [issue](https://guides.github.com/features/issues/) for each task.

- Close issues automatically by mentioning their number in the pull request that completes the
    task.

- Using `gh pr create --fill` from a topic branch that I want to merge
    automatically creates a pull request to main with the branch name as the
    title and all the commits to the branch as the body. Using commit messages
    meaningful and linking issues (I'm gonna use `Fixes #<number>` as a
    convention) makes this a super convenient way to track changes to the main
    branch in a transparent way.

- So, when I work on a new feature or issue, I create a branch with a meaningful
    name, write meaningful commits, add `Fixes #<number>` to the final commit,
    and then use `gh pr create --fill` and `gh pr merge` to create a pull
    request an merge it.



# CLI

- Use the [CLI](https://cli.github.com/manual/) to manage GitHub from the
    command line.

- Use the CLIs aliasing capability instead of defining aliases in my `.bashrc`.
    Type `gh help alias set` for help on how to set aliases, and `gh help alias`
    for help on aliasing functionality.







