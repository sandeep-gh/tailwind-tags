from aenum import Enum
from .colors import _ColorBase
from addict import Dict


class TagBase:
    tagstr = None
    tagops = None
    taghelp = None
    elabel = None  # the label that ends up in the style expression

    @classmethod
    def __truediv__(cls, valprefix):
        tt = _IDivExpr(cls.tagstr, cls.elabel, valprefix)
        return tt
        # if isinstance(valprefix, TagBase) or isinstance(valprefix, _ColorBase):
        #     return _IDivExpr(cls.tagstr, valprefix)
        # return _IDivExpr(cls, valprefix)

    @classmethod
    def evaluate(cls, val):
        fres = cls.tagstr.format(val=val)
        return cls.tagstr.format(val=val)

    @classmethod
    def keyvaleval(cls):
        # fres = cls.tagstr.format(val=val)
        # key = cls.tagstr.replace("{val}", "")
        # key = key.replace("-", "")
        return (cls.elabel,  cls.elabel)


class _IDivExpr:
    def __init__(self, tagstr, elabel, arg2):
        self.tagstr = tagstr
        self.arg2 = arg2
        self.elabel = elabel

    def __truediv__(self, arg):
        #print(f"_IDivExpr.div:  {self}, exp={self.tagstr}  next={self.arg2} arg={arg}")
        tt = _IDivExpr(self, self.elabel, arg)
        return tt
        # if isinstance(arg, _ColorBase):
        #     res = _IDivExpr(self, arg)
        #     return res
        # elif isinstance(arg, TagBase):
        #     return _IDivExpr(self, arg)
        # return _IDivExpr(self, arg)

    def evaluate(self, val=""):
        #print("eval = ", self, " ", self.tagstr, " ", self.arg2, " ", val)
        #print ("eval = ", self, " ", type(self.tagstr), " ", type(self.arg2), " ", val)

        if isinstance(self.tagstr, _IDivExpr) and isinstance(self.arg2, TagBase):
            return self.tagstr.evaluate(self.arg2.evaluate(val))
        if isinstance(self.tagstr, _IDivExpr) and (isinstance(self.arg2, int) or isinstance(self.arg2, str)):
            return self.tagstr.evaluate(str(self.arg2))
        if isinstance(self.tagstr, _IDivExpr) and isinstance(self.arg2, _ColorBase):
            aval = self.arg2.__truediv__(val)
            return self.tagstr.evaluate(val=aval)
        if isinstance(self.tagstr, str) and (isinstance(self.arg2, TagBase) or isinstance(self.arg2, _ColorBase)):
            ares = self.arg2.evaluate(val)
            #print ("phere = ", ares, self.tagstr)
            op = self.tagstr.format(val=ares)
            return self.tagstr.format(val=ares)

        if isinstance(self.tagstr, str) and (isinstance(self.arg2, int) or isinstance(self.arg2, str)):
            # this can introduce double ; need a more logicial strategy
            tmp = self.tagstr.format(val="-" + str(self.arg2))
            return tmp.replace("--", "-")

        print("evaluate: unkown case ", type(
            self.tagstr), " ", type(self.arg2), " ", val)
        print("evaluate: unkown case ", self.tagstr, " ", self.arg2, " ", val)
        assert(0)

    def keyvaleval(self, val=""):
        #print("eval = ", self, " ", self.tagstr, " ", self.arg2, " ", val)
        #print ("eval = ", self, " ", type(self.tagstr), " ", type(self.arg2), " ", val)

        if isinstance(self.tagstr, _IDivExpr) and isinstance(self.arg2, TagBase):
            # print("A")
            return self.tagstr.evaluate(self.arg2.evaluate(val))
        if isinstance(self.tagstr, _IDivExpr) and (isinstance(self.arg2, int) or isinstance(self.arg2, str)):
            # print("B")
            return self.tagstr.keyvaleval(str(self.arg2))
        if isinstance(self.tagstr, _IDivExpr) and isinstance(self.arg2, _ColorBase):
            # print("C")
            aval = self.arg2.__truediv__(val)
            return self.tagstr.evaluate(val=aval)
        if isinstance(self.tagstr, str) and isinstance(self.arg2, TagBase):
            # print("D")
            return (self.elabel, self.arg2.keyvaleval())  # looks suspicious

        if isinstance(self.tagstr, str) and isinstance(self.arg2, _ColorBase):
            # print("D")
            return (self.elabel, self.arg2.keyvaleval(val))  # looks suspicious

        if isinstance(self.tagstr, str) and (isinstance(self.arg2, int) or isinstance(self.arg2, str)):
            # this can introduce double ; need a more logicial strategy
            return (self.elabel, self.arg2)

        print("evaluate: unkown case ", type(
            self.tagstr), " ", type(self.arg2), " ", val)
        print("evaluate: unkown case ", self.tagstr, " ", self.arg2, " ", val)
        assert(0)

    # def __repr__(self):
    #     rstr = self.evaluate()
    #     if rstr[-1] == "-":
    #         rstr = rstr[0:-1]
    #     return rstr


def tstr(*args, prefix=""):
    if len(args) > 0:
        if isinstance(args[0], list):
            raise ValueError("error in tstr argument passing")

    #print("=============begin tstr============")
    res = ""
    for arg in args:
        # print(arg)
        if isinstance(arg, Enum):
            res += f"{prefix}" + arg.value + " "
        if isinstance(arg, _IDivExpr):
            res += f"{prefix}" + arg.evaluate() + " "
        if isinstance(arg, TagBase):
            res += f"{prefix}" + arg.tagstr + " "
        if isinstance(arg, str):
            res += f"{prefix}" + arg + " "
    #print("=============begin tstr============")
    return res.strip()


def get_styReport(*args, prefix=""):
    if len(args) > 0:
        if isinstance(args[0], list):
            raise ValueError("error in tstr argument passing")

    #print("=============begin tstr============")
    res = Dict()
    for arg in args:
        # print(arg)
        if isinstance(arg, Enum):
            res[arg.__class__.__name__]['_val'] = arg.name
        if isinstance(arg, _IDivExpr):
            kv = arg.keyvaleval()
            if isinstance(kv[1], tuple):
                if isinstance(kv[1][1], tuple):
                    print("get_styReport:Warning: too many nested tuple = ", arg)
                    raise ValueError
                else:
                    res[kv[0]][kv[1][0]]['_val'] = kv[1][1]
            else:
                res[kv[0]]['_val'] = kv[1]
        if isinstance(arg, TagBase):
            kv = arg.keyvaleval()
            res[kv[0]]['_val'] = kv[1]
        if isinstance(arg, str):
            print("get_styReport:Warning: skipping sty attr = ", arg)
    #print("=============begin tstr============")
    return res


def hover(*args):
    return tstr(*args, prefix="hover:")


def variant(rv, *args):
    """
    rv: responsive variant, sm, md, lg, xl, 2xl

    """
    return tstr(*args, str(rv))
