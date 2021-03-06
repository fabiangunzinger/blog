---
hide: false
toc: true
layout: post
description: 
categories: [tools]
title: Coding principles
---

# Definitions

- A design pattern is a general repeatable solution to a frequently occuring
  problem.

- An idiom is the translation of a design pattern into code using the language
  clearly and correctly.


# Coding principles

## Stuff to remember

- Get to proof of concept asap.

- "You ain't gonna need it" (YAGNI). Don't add functionality before it's really
  necessary.


## Fundamentals

- A function should do one and only one thing (and -- as a rule of thumb --  be no longer than 50 lines of code).

- Don't reapeat yourself. (Don't copy and paste more than once.)


## SOLID

## Single-responsibility principle

- A module (usually source file) should only have one reason to change -- it should be responsible to a single actor that can demand changes.

- Example: an employee class that produces outputs for the finance and HR departments violates the principle, as both the CFO and the CHO might demand changes that then unintenionally affects the output seen by the other.

- Solution: Separate code that different actors depend on.

- Corollary: don't reuse a function for two different outputs because it does the same thing, but because it does the same thing is used in all instances for outputs used by the same actor. (Above, the CFO might want to tweak how regular hours are calculated. If the same function is used for HR, this will affect the calculations that HR gets.)









