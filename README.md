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


## New: Modifiers can are applied using python functions
Tailwind modifiers are expressed using function of the corresponding name. See example for usage
```
print(tstr(*hover(*focus(bg/green/400), *focus(*placeholder(noop/fw.bold), fc/pink/100))))
```
will yield
```
hover:focus:bg-green-400 hover:focus:placeholder:font-bold hover:focus:text-pink-100
```

## New: From python expression to json and back
Tailwind directives can now be converted into json object and vice versa
### to json
```
res = tt.styClause.to_json(
    *hover(*focus(bg/green/400), *focus(*placeholder(noop/fw.bold), fc/pink/100)))
    
```


The `res` out:
```json
{
    "passthrough": [],
    "bg": {
        "_val": "green-400",
        "_modifier_chain": ["hover", "focus"]
    },
    "FontWeight": {
        "_val": "bold",
        "_modifier_chain": ["hover", "focus", "placeholder"]
    },
    "fc": {
        "_val": "pink-100",
        "_modifier_chain": ["hover", "focus"]
    }
}
```

### to clause

```
claus = tt.styClause.to_clause(res)
print(tstr(*claus))
```

Which outputs the original tailwind expression
```
hover:focus:bg-green-400 hover:focus:placeholder:font-bold hover:focus:text-pink-100
```

TBD: variants 

See (tailwind-tags.md) for constructs and valid expression. 

#TODOs
- inherit
Developed By: Monallabs.in
