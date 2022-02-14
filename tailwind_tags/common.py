import sys
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
    def keyvaleval(cls, val=None):
        # fres = cls.tagstr.format(val=val)
        # key = cls.tagstr.replace("{val}", "")
        # key = key.replace("-", "")
        if val == None or val == "":
            return (cls.elabel,  cls.elabel)
        else:
            return (cls.elabel,  val)


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
        # print("eval = ", " ", type(self.tagstr),
        #       " ", type(self.arg2), " ", val)

        if isinstance(self.tagstr, str) and isinstance(self.arg2, _IDivExpr):
            return self.tagstr.format(val=self.arg2.evaluate(val))
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
        raise ValueError

    def keyvaleval(self, val=""):
        #print("eval = ", self, " ", self.tagstr, " ", self.arg2, " ", val)
        #print ("eval = ", self, " ", type(self.tagstr), " ", type(self.arg2), " ", val)
        #print("calling keyvaleval ", self)
        if isinstance(self.tagstr, _IDivExpr) and isinstance(self.arg2, TagBase):
            return self.tagstr.evaluate(self.arg2.keyvaleval(val))
        if isinstance(self.tagstr, _IDivExpr) and (isinstance(self.arg2, int) or isinstance(self.arg2, str)):
            return self.tagstr.keyvaleval(str(self.arg2))
        if isinstance(self.tagstr, _IDivExpr) and isinstance(self.arg2, _ColorBase):
            aval = self.arg2.__truediv__(val)
            return self.tagstr.evaluate(val=aval)
        if isinstance(self.tagstr, str) and isinstance(self.arg2, TagBase):
            return (self.elabel, self.arg2.keyvaleval(val))  # looks suspicious

        if isinstance(self.tagstr, str) and isinstance(self.arg2, _ColorBase):
            return (self.elabel, self.arg2.keyvaleval(val))  # looks suspicious

        if isinstance(self.tagstr, str) and (isinstance(self.arg2, int) or isinstance(self.arg2, str)):
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


def hover(*args):
    return tstr(*args, prefix="hover:")


def variant(rv, *args):
    """
    rv: responsive variant, sm, md, lg, xl, 2xl

    """
    return tstr(*args, str(rv))
