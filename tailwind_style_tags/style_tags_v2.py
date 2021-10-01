from aenum import Enum, EnumMeta
from .colors import _ColorBase
# TODO: allow integer inputs

mr = pd = x = y = sl = st = sb = sr = fc = bg = bd = W = H = cc = None
G = col = cols = span = start = end = rows = row = None


class Tags:
    margin = ("m{val}", "mr",
              "margin for x and y",
              {}
              )

    padding = ("p{val}", "pd",
               "padding for x and y",
               {}
               )

    dirx = ("x{val}", "x", "x-dir", [])

    diry = ("y{val}", "y", "y-dir", [])

    side_left = ("l{val}", "sl", "left", [])

    side_top = ("t{val}", "st", "top", [])

    side_bottom = ("b{val}", "sb", "bottom", [])

    side_right = ("r{val}", "sr", "right", [])

    font_color = ("text{val}", "fc", "font color", [])

    background_color = ("bg{val}", "bg", "background color", [])

    border_attribute = ("border{val}", "bd", "border color", [])

    width = ("w{val}", "W", "element width",
             [])

    height = ("h{val}", "H", "", ["screen"])

    comment_out = (
        "", "cc", "commnet out, tag does not appear in final tstr", [])

    grid = ("grid{val}", "G", "grid attributes", [])

    cols = ("cols{val}", "cols", "", [])

    rows = ("rows{val}", "rows", "", [])

    col = ("col{val}", "col", "", [])

    row = ("row{val}", "row", "", [])

    span = ("span{val}", "span", "", [])

    start = ("start{val}", "start", "", [])

    end = ("end{val}", "end", "", [])

    gap = ("gap{val}", "gap", "", [])

    space = ("space{val}", "space", "", [])

    text = ("text{val}", "text", "", [])

    leading = ("leading{val}", "lh", "", [])

    placeholder = ("placeholder{val}", "ph", "", [])

    opacity = ("opacity{val}", "opacity", "", [])

    auto = ("auto", "auto", "", [])

    hidden = ("hidden", "hidden", "", [])

    visible = ("visible", "visible", "", [])

    scroll = ("scroll", "scroll", "", [])

    inset = ("inset-{val}", "inset", "", [])

    zorder = ("z-{val}", "zo", "", [])

    order = ("order-{val}", "order", "", [])

    first = ("first", "first", "", [])

    last = ("last", "last", "", [])

    none = ("none", "none", "", [])

    max = ("max{val}", "max", "", [])

    min = ("min{val}", "min", "", [])

    screen = ("screen", "screen", "", [])

    full = ("full", "full", "", [])
    duration = ("duration{val}", "duration", "", [])

    # TBD docs/border-radius
    # TBD docs/divide-width
    # TBD docs/divide-color
    # TBD docs/divide-opacity
    # TBD docs/divide-style
    # TBD docs/divide-width

    ring = ("ring{val}", "ring", "", [])

    offset = ("offset{val}", "offset", "", [])

    resize = ("resize{val}", "resize", "", [])

    pass


taglist = [attr for attr in dir(Tags) if not callable(
    getattr(Tags, attr)) and not attr.startswith("__")]


class _IDivExpr:
    def __init__(self, tagstr, arg2):
        self.tagstr = tagstr
        self.arg2 = arg2

    def evaluate(self, res):
        newres = self.arg2.__truediv__(res)
        if isinstance(self.tagstr, _IDivExpr):
            return self.tagstr.__truediv__(newres)
        elif isinstance(self.tagstr, str):
            val = "-"+newres
            frs =  self.tagstr.format(val=val)
            return frs


    def __truediv__(self, arg):
        #print(f"_IDivExpr.div:  {self}, exp={self.tagstr}  next={self.arg2} arg={arg}")
        if isinstance(arg, _ColorBase):
            res = _IDivExpr(self, arg)
            return res
        elif isinstance(arg, TagBase):
            return _IDivExpr(self, arg)
        else:
            if isinstance(self.arg2, _ColorBase):
                return self.evaluate(arg)
            elif isinstance(self.arg2, TagBase):
                return self.evaluate(arg)
                #res = self.arg2.__truediv__(arg)
                #print ('res = ', res)
                #return self.tagstr.evaluate(res)
            elif isinstance(self.arg2, _IDivExpr):
                return self.arg2.evaluate(arg)
                
            else:
                print ("not sure ", type(self.arg2))

class TagBase:
    tagstr = None
    tagops = None
    taghelp = None

    @classmethod
    def getval(cls, valprefix):
        '''
        tval is tailwind values
        '''
        
        val = str(valprefix)  # use valprefix if no match is found
        if not cls.tagops: #tagpos is outdate for now
            return "-"+val  # ignore option checking
        for _ in cls.tagops:
            if _.startswith(val):
                val = _
                break
        return "-"+val

    @classmethod
    def evaluate(cls, valprefix):
        val = cls.getval(valprefix)
        return cls.tagstr.format(val=val)

    @classmethod
    def __truediv__(cls, valprefix):
        if isinstance(valprefix, TagBase):
            return _IDivExpr(cls.tagstr, valprefix)

        if isinstance(valprefix, _ColorBase):
            return _IDivExpr(cls.tagstr, valprefix)
        val = cls.getval(valprefix)
        return cls.tagstr.format(val=val)


for _ in taglist:
    taginfo = getattr(Tags, _)
    globals()[taginfo[1]] = type(taginfo[1], (TagBase,), {'tagstr': taginfo[0], 'tagops': taginfo[3],
                                                          'taghelp': taginfo[2]})()


def tstr(*args):
    res = ""
    for arg in args:
        if isinstance(arg, Enum):
            res += " " + arg.value
        else:
            res += " " + arg
    return res


def hover(*args):
    res = ""
    for arg in args:
        if isinstance(arg, Enum):
            res += " hover:" + arg.value
        else:
            res += " hover:" + arg

    return res
    pass


def variant(rv, *args):
    """
    rv: responsive variant, sm, md, lg, xl, 2xl

    """
    res = ""
    for arg in args:
        if isinstance(arg, Enum):
            res += str(rv) + arg.value
        else:
            res += str(rv) + arg

    return res
