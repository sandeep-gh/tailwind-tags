from tailwind_tags.common import TagBase


class _auto(TagBase):
    tagstr = "auto"
    tagops = []
    taghelp = ""


auto = _auto()


class _bg(TagBase):
    tagstr = "bg-{val}"
    tagops = []
    taghelp = "background color"


bg = _bg()


class _bd(TagBase):
    tagstr = "border-{val}"
    tagops = []
    taghelp = "border color"


bd = _bd()


class _col(TagBase):
    tagstr = "col-{val}"
    tagops = []
    taghelp = ""


col = _col()


class _cols(TagBase):
    tagstr = "cols-{val}"
    tagops = []
    taghelp = ""


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


container = _container()


class _x(TagBase):
    tagstr = "x-{val}"
    tagops = []
    taghelp = "x-dir"


x = _x()


class _y(TagBase):
    tagstr = "y-{val}"
    tagops = []
    taghelp = "y-dir"


y = _y()


class _duration(TagBase):
    tagstr = "duration-{val}"
    tagops = []
    taghelp = ""


duration = _duration()


class _end(TagBase):
    tagstr = "end{val}"
    tagops = []
    taghelp = ""


end = _end()


class _first(TagBase):
    tagstr = "first"
    tagops = []
    taghelp = ""


first = _first()


class _fc(TagBase):
    tagstr = "text-{val}"
    tagops = []
    taghelp = "font color"


fc = _fc()


class _full(TagBase):
    tagstr = "full"
    tagops = []
    taghelp = ""


full = _full()


class _gap(TagBase):
    tagstr = "gap-{val}"
    tagops = []
    taghelp = ""


gap = _gap()


class _G(TagBase):
    tagstr = "grid-{val}"
    tagops = []
    taghelp = "grid attributes"


G = _G()


class _H(TagBase):
    tagstr = "h-{val}"
    tagops = ['screen']
    taghelp = ""


H = _H()


class _hidden(TagBase):
    tagstr = "hidden"
    tagops = []
    taghelp = ""


hidden = _hidden()


class _inset(TagBase):
    tagstr = "inset-{val}"
    tagops = []
    taghelp = ""


inset = _inset()


class _last(TagBase):
    tagstr = "last"
    tagops = []
    taghelp = ""


last = _last()


class _lh(TagBase):
    tagstr = "leading-{val}"
    tagops = []
    taghelp = ""


lh = _lh()


class _mr(TagBase):
    tagstr = "m{val}"
    tagops = {}
    taghelp = "margin for x and y"


mr = _mr()


class _max(TagBase):
    tagstr = "max-{val}"
    tagops = []
    taghelp = ""


max = _max()


class _min(TagBase):
    tagstr = "min-{val}"
    tagops = []
    taghelp = ""


min = _min()


class _none(TagBase):
    tagstr = "none"
    tagops = []
    taghelp = ""


none = _none()


class _offset(TagBase):
    tagstr = "offset-{val}"
    tagops = []
    taghelp = ""


offset = _offset()


class _opacity(TagBase):
    tagstr = "opacity-{val}"
    tagops = []
    taghelp = ""


opacity = _opacity()


class _order(TagBase):
    tagstr = "order-{val}"
    tagops = []
    taghelp = ""


order = _order()


class _ovf(TagBase):
    tagstr = "overflow{val}"
    tagops = []
    taghelp = ""


ovf = _ovf()


class _pd(TagBase):
    tagstr = "p{val}"
    tagops = {}
    taghelp = "padding for x and y"


pd = _pd()


class _ph(TagBase):
    tagstr = "placeholder-{val}"
    tagops = []
    taghelp = ""


ph = _ph()


class _resize(TagBase):
    tagstr = "resize-{val}"
    tagops = []
    taghelp = ""


resize = _resize()


class _ring(TagBase):
    tagstr = "ring-{val}"
    tagops = []
    taghelp = ""


ring = _ring()


class _row(TagBase):
    tagstr = "row-{val}"
    tagops = []
    taghelp = ""


row = _row()


class _rows(TagBase):
    tagstr = "rows-{val}"
    tagops = []
    taghelp = ""


rows = _rows()


class _screen(TagBase):
    tagstr = "screen"
    tagops = []
    taghelp = ""


screen = _screen()


class _scroll(TagBase):
    tagstr = "scroll"
    tagops = []
    taghelp = ""


scroll = _scroll()


class _sb(TagBase):
    tagstr = "b{val}"
    tagops = []
    taghelp = "bottom"


sb = _sb()


class _sl(TagBase):
    tagstr = "left-{val}"
    tagops = []
    taghelp = "left"


sl = _sl()


class _sr(TagBase):
    tagstr = "r{val}"
    tagops = []
    taghelp = "right"


sr = _sr()


class _st(TagBase):
    tagstr = "top-{val}"
    tagops = []
    taghelp = "top"


st = _st()


class _space(TagBase):
    tagstr = "space-{val}"
    tagops = []
    taghelp = ""


space = _space()


class _span(TagBase):
    tagstr = "span-{val}"
    tagops = []
    taghelp = ""


span = _span()


class _start(TagBase):
    tagstr = "start{val}"
    tagops = []
    taghelp = ""


start = _start()


class _text(TagBase):
    tagstr = "text-{val}"
    tagops = []
    taghelp = ""


text = _text()


class _visible(TagBase):
    tagstr = "visible"
    tagops = []
    taghelp = ""


visible = _visible()


class _W(TagBase):
    tagstr = "w-{val}"
    tagops = []
    taghelp = "element width"


W = _W()


class _zo(TagBase):
    tagstr = "z-{val}"
    tagops = []
    taghelp = ""


zo = _zo()
