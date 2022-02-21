import sys
from tailwind_tags.common import TagBase


class _sw(TagBase):
    tagstr = "shadow-{val}"
    tagops = []
    taghelp = ""
    elabel = "shadow"


sw = _sw()


class _bd(TagBase):
    tagstr = "border-{val}"
    tagops = []
    taghelp = "border color"
    elabel = "border"


bd = _bd()


class _cc(TagBase):
    tagstr = ""
    tagops = []
    taghelp = "commnet out, tag does not appear in final tstr"


cc = _cc()


_tw_keywords = ["container", "inherit",
                "current", "transparent", "black", "white", "first", "full", "screen", "hidden", "last", "none", "scroll", "span", "text", "visible", "auto", "group"]

for kw in _tw_keywords:
    globals()[f"_{kw}"] = type(f"_{kw}", (TagBase,),

                               {'tagstr': kw, "tagops": [], "taghelp": "", "elabel": kw})

    globals()[kw] = globals()[f"_{kw}"]()


_tw_keywords_val = ["bg", "x", "y", "duration", "inset",
                    "max", "min", "offset", "opacity", "order", "ring", "row", "rows", "col", "cols", "space", "span", "stroke"]
for kw in _tw_keywords_val:
    globals()[f"_{kw}"] = type(f"_{kw}", (TagBase,),

                               {'tagstr': f"{kw}-{{val}}", "tagops": [], "taghelp": "", "elabel": kw})

    globals()[kw] = globals()[f"_{kw}"]()


class _end(TagBase):
    tagstr = "end{val}"
    tagops = []
    taghelp = ""
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
    taghelp = "grid attributes"
    elabel = "G"


G = _G()


class _H(TagBase):
    tagstr = "h-{val}"
    tagops = ['screen']
    taghelp = ""
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
    taghelp = "margin for x and y"
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
    taghelp = "bottom"
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
    taghelp = "right"
    elabel = "sr"


sr = _sr()


class _st(TagBase):
    tagstr = "t-{val}"
    tagops = []
    taghelp = "top"
    elabel = "st"


st = _st()


class _start(TagBase):
    tagstr = "start{val}"
    tagops = []
    taghelp = ""
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
    taghelp = ""
    elabel = "zo"


zo = _zo()


class _noop(TagBase):
    tagstr = "{val}"
    tagops = []
    taghelp = ""
    elabel = "noop"


noop = _noop()


current_module = sys.modules[__name__]
styTagDict = {}
for varName in dir():
    try:
        res = getattr(current_module, varName)
        styTagDict[varName] = res

    except:

        pass
