"""styClause to json and vice versa
"""
from addict import Dict
from .style_tags import styTagDict
import sys
from aenum import Enum
from .colors import _ColorBase
from .common import _IDivExpr, TagBase
from .style_values import styValueDict
from .style_tags import styTagDict, x


def to_json(*args, prefix=""):
    """
    convert styClause from list of IDivExpr to json/dict
    """
    if len(args) > 0:
        if isinstance(args[0], list):
            raise ValueError("error in tstr argument passing")

    #print("=============begin tstr============")
    res = Dict()
    # keep all directives that are specified as string
    res.passthrough = []
    for arg in args:
        # print(arg)
        if isinstance(arg, Enum):
            # print("R")
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
            # print("G")
            kv = arg.keyvaleval()
            res[kv[0]]['_val'] = kv[1]
        if isinstance(arg, str):
            print("get_styReport:Warning: skipping sty attr = ", arg)
            res.passthrough.append(arg)
    return res


# ================================ end ===============================


# ============== from json styreport to tstr expression ==============

def to_clause(styreport):
    """
    builds styclause from styreport
    """
    def json_to_clause(key, val):
        """
        resolve json expression of type :'ObjectPosition': {'_val': 't'}}
        to styclause

        """
        if key in styValueDict:
            return getattr(styValueDict[key], val._val)

        elif '_val' in val:
            return styTagDict[key].__truediv__(val._val)

        elif '_color' in val:
            colstr = val._color._val
            cc, cv = colstr.replace("00", ""). split(
                "-")  # gray-400 --> gray, 400"
            return styTagDict[key].__truediv__(f"{cc}-{cv}00")
        elif len(val.items()) == 1:  # case: pd/x/4==> pd {'x': {'_val': '4'}}
            [k, v] = list(val.items())[0]
            x1 = styTagDict[k].__truediv__(v._val)
            x2 = styTagDict[key].__truediv__(x1)
            return x2
            # return styTagDict[k].__truediv__(v._val)
            # return styTagDict[key].__truediv__(styTagDict[k].__truediv__(v._val))

        else:

            print("unable to resolve ", key, val, len(val.items()))
            raise ValueError

    res = []
    for k, v in styreport.items():
        if k in ['hctype', 'spath']:
            continue

        if k == "passthrough":
            if v:
                [res.append(_) for _ in v]
        elif '_val' in v or '_color' in v or len(v.items()) == 1:
            res.append(json_to_clause(k, v))
        else:
            print("no resolved ", k, v)
            raise ValueError
    return res

# ================================ end ===============================
