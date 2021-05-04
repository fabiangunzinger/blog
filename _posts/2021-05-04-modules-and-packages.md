---
hide: false
toc: true
layout: post
categories: [python]
title: Python modules and packages
---

# Modules

- A *module* is a file that contains definitions intended for reuse in a script
  or an interactive session.

- Calling `import module` for the first time does three things: 1) create a new
  namespace that acts as the global namespace for all objects defined in module,
  2) execute the entire module, 3) create a name -- identical to the module name -- within the caller namespace that references to the module. This can be used to access module objects in the caller namespace as `module.object`.

- Calling `from module import symbol` imports `symbol` into the current namespace. However, the global namespace for `symbol` (if it's a function) always remains the namespace in which it was defined, not the caller's namespace.

- One reason `from module import *` is generally discouraged is that it directly imports all the module's objects into the caller's namespace, which is often said to cluter it up. Especially when importing large modules this makes sense, as it's much cleaner to keep objects defined in imported modules in eponymous namespaces and accessing them via `module.object`, which immediately makes clear where object comes from and can help greatly with debugging.

- One implication of all the above is that as a developer, you don't have to
  worry about clashing variable names between modules, as they are each stored
  in their own namespace, and accessed via `moduleA.foo` and `moduleB.foo` in
  the caller namespace.

- When we import a module `foo`, the interpreter first searches for a built-in
  module and, if none is found, searches a list of directories given the
  variable `sys.path`. `sys.path` contains the directory of the input script,
  the variable `PYTHONPATH`, and installation-dependent defaults. I can
  manipulate `sys.path` using standard list operations; to add a directory, use
  `sys.path.append('dirname')`.

- A common usecase of the above for me is to make a package available to Jupyter
  Notebooks. By default, a notebook's `sys.path` contains the folder the noteook
  is located in and a bunch of conda managed directories linked to my running
  Conda environment. To make available a package that lives in the project root
  directory, just do
  `sys.path.append('/Users/fgu/dev/projectname/packagename')`. I can then
  reference modules from the package using `from packagename import module`.

- Use `dir(modulename)` to list all names defined in `modulname`, or `dir()` to
  list all names that are currently defined.

# Packages

- Packages are collections of modules. They help structure Python's module namespace by using dotted module
  names. E.g. `a.b` refers to submodule `b` in package `a`. Thus, just as the
  use of modules alleviates worries about clashing global variable names between
  modules, using a package alleviates worries about clashing module between
  multi-module packages.



# Sources

- [Python docs -
  Modules](https://docs.python.org/3/tutorial/modules.html#executing-modules-as-scripts)



