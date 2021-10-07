# Tailwind Tags
Injects [tailwind](https://tailwindcss.com/)  constructs into python namespace. User should find little easier to 
write and manipulate tailwind style of your webpage. My primary use this module is with [JustPy](https://github.com/elimintz/justpy) library 
a python based web development library/framework. 

So instead of styling a component of with a long string such "bg-pink-400 ring-offset-red-200 justify-content-start text-black-800", using
this library you would instead write:
```python
tstr(bg/pink/4, ring/offset/red/2, jc.start, fc/black/8)
```

This make manipulation of styles (passing style directives to functions, substitution of style through variable assignment, etc) lot easier. 

A word of caution: 
This library does pollute the namespace of you python file/module, so be careful if using "from tailwind_tags import *". 
Also, not all construct of tailwind is available here. 

See (tailwind-tags.md) for constructs and valid expression. 

Developed By: Monallabs.in
