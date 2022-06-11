import sys
from tailwind_tags.common import TagBase


class _sw(TagBase):
    tagstr = "shadow-{val}"
    tagops = []
    taghelp = "shadow"
    elabel = "sw"


sw = _sw()


class _bd(TagBase):
    tagstr = "border-{val}"
    tagops = []
    taghelp = "border color"
    elabel = "bd"


bd = _bd()


class _cc(TagBase):
    tagstr = ""
    tagops = []
    taghelp = "commnet out, tag does not appear in final tstr"
    elabel = "cc"


cc = _cc()


_tw_keywords = ["container", "inherit",
                "current", "transparent", "black", "white", "first", "full", "screen", "hidden", "last", "none", "scroll", "span", "text", "visible", "auto", "group"]

for kw in _tw_keywords:
    globals()[f"_{kw}"] = type(f"_{kw}", (TagBase,),

                               {'tagstr': kw, "tagops": [], "taghelp": kw, "elabel": kw})

    globals()[kw] = globals()[f"_{kw}"]()


_tw_keywords_val = ["bg", "x", "y", "duration", "inset",
                    "max", "min", "offset", "opacity", "order", "ring", "row", "rows", "col", "cols", "space", "span", "stroke", "gap"]
for kw in _tw_keywords_val:
    globals()[f"_{kw}"] = type(f"_{kw}", (TagBase,),

                               {'tagstr': f"{kw}-{{val}}", "tagops": [], "taghelp": kw, "elabel": kw})

    globals()[kw] = globals()[f"_{kw}"]()


class _end(TagBase):
    tagstr = "end{val}"
    tagops = []
    taghelp = "end"
    elabel = "end"


end = _end()


class _fc(TagBase):
    tagstr = "text-{val}"
    tagops = []
    taghelp = "font color"
    elabel = "fc"


fc = _fc()


class _G(TagBase):
    tagstr = "grid-{val}"
    tagops = []
    taghelp = "grid"
    elabel = "G"


G = _G()


class _H(TagBase):
    tagstr = "h-{val}"
    tagops = ['screen']
    taghelp = "height"
    elabel = "H"


H = _H()
# TODO: limit H to its domain


class _lh(TagBase):
    tagstr = "leading-{val}"
    tagops = []
    taghelp = ""
    elabel = "lh"


lh = _lh()


class _mr(TagBase):
    tagstr = "m{val}"
    tagops = {}
    taghelp = "margin"
    elabel = "mr"


mr = _mr()


class _ovf(TagBase):
    tagstr = "overflow{val}"
    tagops = []
    taghelp = ""
    elabel = "ovf"


ovf = _ovf()


class _pd(TagBase):
    tagstr = "p{val}"
    tagops = {}
    taghelp = "padding for x and y"
    elabel = "pd"


pd = _pd()


class _ph(TagBase):
    tagstr = "placeholder-{val}"
    tagops = []
    taghelp = ""
    elabel = "ph"


ph = _ph()


class _resize(TagBase):
    tagstr = "resize-{val}"
    tagops = []
    taghelp = ""
    elabel = "resize"


resize = _resize()


class _sb(TagBase):
    tagstr = "b-{val}"
    tagops = []
    taghelp = "side bottom"
    elabel = "sb"


sb = _sb()


class _sl(TagBase):
    tagstr = "l-{val}"
    tagops = []
    taghelp = "left"
    elabel = "sl"


sl = _sl()


class _sr(TagBase):
    tagstr = "r-{val}"
    tagops = []
    taghelp = "side right"
    elabel = "sr"


sr = _sr()


class _st(TagBase):
    tagstr = "t-{val}"
    tagops = []
    taghelp = "side top"
    elabel = "st"


st = _st()

class _top(TagBase):
    tagstr = "top-{val}"
    tagops = []
    taghelp = "top"
    elabel = "top"


top = _top()


class _right(TagBase):
    tagstr = "right-{val}"
    tagops = []
    taghelp = "right"
    elabel = "right"


right = _right()

class _bottom(TagBase):
    tagstr = "bottom-{val}"
    tagops = []
    taghelp = "bottom"
    elabel = "bottom"


bottom = _bottom()


class _left(TagBase):
    tagstr = "left-{val}"
    tagops = []
    taghelp = "left"
    elabel = "left"


left = _left()

class _inset(TagBase):
    tagstr = "inset-{val}"
    tagops = []
    taghelp = "inset"
    elabel = "inset"


inset = _inset()



class _start(TagBase):
    tagstr = "start{val}"
    tagops = []
    taghelp = "start"
    elabel = "start"


start = _start()


class _W(TagBase):
    tagstr = "w-{val}"
    tagops = []
    taghelp = "element width"
    elabel = "W"


W = _W()


class _zo(TagBase):
    tagstr = "z-{val}"
    tagops = []
    taghelp = "z-order"
    elabel = "zo"


zo = _zo()


class _noop(TagBase):
    tagstr = "{val}"
    tagops = []
    taghelp = ""
    elabel = "noop"


noop = _noop()


# current_module = sys.modules[__name__]
# styTagDict = {}
# for varName in dir():
#     try:
#         res = getattr(current_module, varName)
#         styTagDict[varName] = res

#     except:

#         pass

current_module = sys.modules[__name__]
styTagDict = dict([(name, cls)
                   for name, cls in current_module.__dict__.items() if isinstance(cls, TagBase)])
