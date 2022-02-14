import sys
from tailwind_tags.common import TagBase


class _auto(TagBase):
    tagstr = "auto"
    tagops = []
    taghelp = ""
    elabel = "auto"


auto = _auto()


class _bg(TagBase):
    tagstr = "bg-{val}"
    tagops = []
    taghelp = "background color"
    elabel = "bg"


bg = _bg()


class _bd(TagBase):
    tagstr = "border-{val}"
    tagops = []
    taghelp = "border color"
    elabel = "border"


bd = _bd()


class _col(TagBase):
    tagstr = "col-{val}"
    tagops = []
    taghelp = ""
    elabel = "col"


col = _col()


class _cols(TagBase):
    tagstr = "cols-{val}"
    tagops = []
    taghelp = ""
    elabel = "cols"


cols = _cols()


class _cc(TagBase):
    tagstr = ""
    tagops = []
    taghelp = "commnet out, tag does not appear in final tstr"


cc = _cc()


class _container(TagBase):
    tagstr = "container"
    tagops = []
    taghelp = ""
    elabel = "container"


container = _container()


class _x(TagBase):
    tagstr = "x-{val}"
    tagops = []
    taghelp = "x-dir"
    elabel = "x"


x = _x()


class _y(TagBase):
    tagstr = "y-{val}"
    tagops = []
    taghelp = "y-dir"
    elabel = "y"


y = _y()


class _duration(TagBase):
    tagstr = "duration-{val}"
    tagops = []
    taghelp = ""
    elabel = "duration"


duration = _duration()


class _end(TagBase):
    tagstr = "end{val}"
    tagops = []
    taghelp = ""
    elabel = "end"


end = _end()


class _first(TagBase):
    tagstr = "first"
    tagops = []
    taghelp = ""
    elabel = "first"


first = _first()


class _fc(TagBase):
    tagstr = "text-{val}"
    tagops = []
    taghelp = "font color"
    elabel = "fc"


fc = _fc()


class _full(TagBase):
    tagstr = "full"
    tagops = []
    taghelp = ""
    elabel = "full"


full = _full()


class _gap(TagBase):
    tagstr = "gap-{val}"
    tagops = []
    taghelp = ""
    elabel = "gap"


gap = _gap()


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


class _hidden(TagBase):
    tagstr = "hidden"
    tagops = []
    taghelp = ""
    elabel = "hidden"


hidden = _hidden()


class _inset(TagBase):
    tagstr = "inset-{val}"
    tagops = []
    taghelp = ""
    elabel = "inset"


inset = _inset()


class _last(TagBase):
    tagstr = "last"
    tagops = []
    taghelp = ""
    elabel = "last"


last = _last()


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


class _max(TagBase):
    tagstr = "max-{val}"
    tagops = []
    taghelp = ""
    elabel = "max"


max = _max()


class _min(TagBase):
    tagstr = "min-{val}"
    tagops = []
    taghelp = ""
    elabel = "min"


min = _min()


class _none(TagBase):
    tagstr = "none"
    tagops = []
    taghelp = ""
    elabel = "none"


none = _none()


class _offset(TagBase):
    tagstr = "offset-{val}"
    tagops = []
    taghelp = ""
    elabel = "offset"


offset = _offset()


class _opacity(TagBase):
    tagstr = "opacity-{val}"
    tagops = []
    taghelp = ""
    elabel = "opacity"


opacity = _opacity()


class _order(TagBase):
    tagstr = "order-{val}"
    tagops = []
    taghelp = ""
    elabel = "order"


order = _order()


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


class _ring(TagBase):
    tagstr = "ring-{val}"
    tagops = []
    taghelp = ""
    elabel = "ring"


ring = _ring()


class _row(TagBase):
    tagstr = "row-{val}"
    tagops = []
    taghelp = ""
    elabel = "row"


row = _row()


class _rows(TagBase):
    tagstr = "rows-{val}"
    tagops = []
    taghelp = ""
    elabel = "rows"


rows = _rows()


class _screen(TagBase):
    tagstr = "screen"
    tagops = []
    taghelp = ""
    elabel = "screen"


screen = _screen()


class _scroll(TagBase):
    tagstr = "scroll"
    tagops = []
    taghelp = ""
    elabel = "scroll"


scroll = _scroll()


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


class _space(TagBase):
    tagstr = "space-{val}"
    tagops = []
    taghelp = ""
    elabel = "space"


space = _space()


class _span(TagBase):
    tagstr = "span-{val}"
    tagops = []
    taghelp = ""
    elabel = "span"


span = _span()


class _start(TagBase):
    tagstr = "start{val}"
    tagops = []
    taghelp = ""
    elabel = "start"


start = _start()


class _text(TagBase):
    tagstr = "text-{val}"
    tagops = []
    taghelp = ""
    elabel = "text"


text = _text()


class _visible(TagBase):
    tagstr = "visible"
    tagops = []
    taghelp = ""
    elabel = "visible"


visible = _visible()


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


current_module = sys.modules[__name__]
styTagDict = {}
for varName in dir():
    try:
        res = getattr(current_module, varName)
        styTagDict[varName] = res

    except:

        pass
