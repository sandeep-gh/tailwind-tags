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

    dirx = ("x{val}", "x", "x-dir", ["auto"])

    diry = ("y{val}", "y", "y-dir", ["auto"])

    side_left = ("l{val}", "sl", "left", [])

    side_top = ("t{val}", "st", "top", [])

    side_bottom = ("b{val}", "sb", "bottom", [])

    side_right = ("r{val}", "sr", "right", [])

    font_color = ("text-{val}", "fc", "font color", [])

    background_color = ("bg-{val}", "bg", "background color", [])

    border_attribute = ("border-{val}", "bd", "border color", [])

    width = ("w{val}", "W", "element width",
             [])

    height = ("h{val}", "H", "", ["screen"])

    comment_out = (
        "", "cc", "commnet out, tag does not appear in final tstr", [])

    grid = ("grid-{val}", "G", "grid attributes", [])

    cols = ("cols{val}", "cols", "", [])

    rows = ("rows{val}", "rows", "", [])

    col = ("col-{val}", "col", "", [])

    row = ("row-{val}", "row", "", [])

    span = ("span{val}", "span", "", [])

    start = ("start{val}", "start", "", [])

    end = ("end{val}", "end", "", [])

    gap = ("gap{val}", "gap", "", [])

    text = ("text{val}", "text", "", [])

    pass


taglist = [attr for attr in dir(Tags) if not callable(
    getattr(Tags, attr)) and not attr.startswith("__")]


class _twStr:
    def __init__(self, tagstr, arg2):
        self.tagstr = tagstr
        self.arg2 = arg2

    def __truediv__(self, size):
        return self.tagstr.format(val=self.arg2.__truediv__(size))


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

        if not cls.tagops:
            return "-"+val  # ignore option checking
        for _ in cls.tagops:
            if _.startswith(val):
                val = _
                break
        return "-"+val

    @classmethod
    def __truediv__(cls, valprefix):
        if isinstance(valprefix, TagBase):

            return _twStr(cls.tagstr, valprefix)

        if isinstance(valprefix, _ColorBase):

            return _twStr(cls.tagstr, valprefix)

        val = cls.getval(valprefix)
        return cls.tagstr.format(val=val)

    @classmethod
    def __pow__(cls, valprefix):
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
