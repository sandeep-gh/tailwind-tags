from aenum import Enum, EnumMeta
from addict import Dict
import tailwind_style_tags.colors as colors
# https://stackoverflow.com/questions/33679930/how-to-extend-python-enum


class MetaClsEnumJoin(EnumMeta):
    """
    Metaclass that creates a new `enum.Enum` from multiple existing Enums.

    @code
        from enum import Enum

        ENUMA = Enum('ENUMA', {'a': 1, 'b': 2})
        ENUMB = Enum('ENUMB', {'c': 3, 'd': 4})
        class ENUMJOINED(Enum, metaclass=MetaClsEnumJoin, enums=(ENUMA, ENUMB)):
            pass

        print(ENUMJOINED.a)
        print(ENUMJOINED.b)
        print(ENUMJOINED.c)
        print(ENUMJOINED.d)
    @endcode
    """

    value_category_map = Dict()

    @classmethod
    def __prepare__(metacls, name, bases, enums=None, **kargs):
        """
        Generates the class's namespace.
        @param enums Iterable of `enum.Enum` classes to include in the new class.  Conflicts will
            be resolved by overriding existing values defined by Enums earlier in the iterable with
            values defined by Enums later in the iterable.
        """
        # kargs = {"myArg1": 1, "myArg2": 2}
        if enums is None:
            raise ValueError(
                'Class keyword argument `enums` must be defined to use this metaclass.')
        ret = super().__prepare__(name, bases, **kargs)
        for enm in enums:
            for item in enm:
                ret[item.name] = item.value  # Throws `TypeError` if conflict.
                MetaClsEnumJoin.value_category_map[item.name] = item
        return ret

    def __new__(metacls, name, bases, namespace, **kargs):
        return super().__new__(metacls, name, bases, namespace)
        # DO NOT send "**kargs" to "type.__new__".  It won't catch them and
        # you'll get a "TypeError: type() takes 1 or 3 arguments" exception.

    def __init__(cls, name, bases, namespace, **kargs):
        super().__init__(name, bases, namespace)
        # DO NOT send "**kargs" to "type.__init__" in Python 3.5 and older.  You'll get a
        # "TypeError: type.__init__() takes no keyword arguments" exception.


# TODO: top, bottom permutation combination missing
class BorderRadius(Enum):
    sm = "rounded-sm"
    md = "rounded-md"
    lg = "rounded-lg"
    full = "rounded-full"
    none = "rounded-none"
    pass


class FontWidth(Enum):
    thin = "font-thin"
    extralight = "font-extralight"
    light = "font-light"
    normal = "font-normal"
    medium = "font-medium"
    bold = "font-bold"
    extrabold = "font-extrabold"
    black = "font-black"
    pass


class FontScale(Enum):
    xs = "text-xs"
    sm = "text-sm"
    bs = "text-base"
    lg = "text-lg"
    xl = "text-xl"
    xl2 = "text-2xl"
    xl3 = "text-3xl"
    pass


class FontFamily(Enum):
    sans = "font-sans"
    serif = "font-serif"
    mono = "font-mono"
    pass


class TextAlign(Enum):
    left = "text-left"
    center = "text-center"
    right = "text-right"
    pass


# Layout
class BoxTopo(Enum):
    bd = "border"
    container = "container"
    pass

#################################################
# block	display: block;                         #
# inline-block	display: inline-block;          #
# inline	display: inline;                #
# flex	display: flex;                          #
# inline-flex	display: inline-flex;           #
# table                                         #
#################################################

###############################################################
# inline-table	display: inline-table;                        #
# table-caption	display: table-caption;                       #
# table-cell	display: table-cell;                          #
# table-column	display: table-column;                        #
# table-column-group	display: table-column-group;          #
# table-footer-group	display: table-footer-group;          #
# table-header-group	display: table-header-group;          #
# table-row-group	display: table-row-group;             #
# table-row	display: table-row;                           #
# flow-root	display: flow-root;                           #
# grid	display: grid;                                        #
# inline-grid	display: inline-grid;                         #
# contents	display: contents;                            #
# list-item	display: list-item;                           #
# hidden	display: none;                                #
###############################################################


class BoxLayout(Enum):
    b = "block"
    bi = "inline-block"
    i = "inline"
    f = "flex"
    fi = "inline-flex"
    t = "table"
    g = "grid"
    pass


class JustifyContent(Enum):
    start = "justify-start"
    end = "justify-end"
    center = "justify-center"
    between = "justify-between"
    evenly = "justify-evenly"
    around = "justify-around"


class JustifyItems(Enum):
    start = "items-start"
    end = "items-end"
    center = "items-center"
    bl = "items-baseline"
    stretch = "items-stretch"

    pass


class BoxShadow(Enum):
    sm = "shadow-sm"
    _ = "shadow"
    md = "shadow-md"
    lg = "shadow-lg"
    xl = "shadow-xl"
    xl2 = "shadow-2xl"
    none = "shadow-none"
    inner = "shadow-inner"
    pass


class FlexLayout(Enum):
    row = "flex-row"
    rrow = "flex-row-reverse"
    col = "flex-col"
    rcol = "flex-col-reverse"
    wrap = "flex-wrap"
    rwrap = "flex-wrap-reverse"
    nowrap = "flex-nowrap"
    one = "flex-1"
    auto = "flex-auto"
    initial = "flex-initial"
    none = "flex-none"
    grow = "flex-grow"
    nogrow = "flex-grow-0"
    shrink = "flex-shrink"
    noshrink = "flex-shrink-0"


class Common(Enum):
    pass


class SV(Enum, metaclass=MetaClsEnumJoin, enums=(FontWidth, FontScale)):
    pass


class TailwindValues(Enum):
    thin = FontWidth
    extralight = FontWidth
    light = FontWidth
    normal = FontWidth
    medium = FontWidth
    bold = FontWidth
    extrabold = FontWidth
    black = FontWidth
    sm = FontScale
    bs = FontScale
    lg = FontScale
    xl = FontScale
    xl2 = FontScale
    xl3 = FontScale


_v = TailwindValues
###################
# _fw = FontWidth #
# _fs = FontScale #
# _fc = FontColor #
# _ta = TextAlign #
# _bt = BoxTopo   #
###################
