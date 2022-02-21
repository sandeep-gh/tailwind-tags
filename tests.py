from tailwind_tags import *
import tailwind_tags as tt
#res = get_styReport(text/gray/6, mr/sb/2, mr/x/auto, W/6, G/cols/6)
from addict import Dict
#res = get_styReport(mr/4)
res = tstr(sw/pink/"600/80")

# r = fw.normal #pd/5  # resize/x/5
# res = r.keyvaleval()
print(res)
# dictionary from class name to abbrv used in
# styval_dict = Dict()

# for varn in dir():
#     try:
#         module = getattr(tt, varn)
#         styval_dict[module.__name__] = varn
#     except:

#         pass


# def styreport_resolvekv(key, val):
#     """
#     resolve json expression of type : key'ObjectPosition': {'_val': 't'}}

#     """
#     if key in styval_dict:
#         abbrv = styval_dict[key]
#         return f"{abbrv}.{val['_val']}"

#     elif '_val' in val:
#         return f"{key}/{val['_val']}"
#     elif '_color' in val:
#         colstr = val._color._val
#         cc, cv = colstr.replace("00", ""). split(
#             "-")  # gray-400 --> gray, 400"

#         return f"{key}/{cc}/{cv}"
#     elif len(val.items()) == 1:  # case: pd/x/4==> pd {'x': {'_val': '4'}}
#         [k, v] = list(val.items())[0]
#         return f"{key}/{k}/{v._val}"
#     else:

#         print("unable to resolve ", key, val, len(val.items()))
#         raise ValueError


# def styreport_resolve(styreport):
#     """
#     styreport: a dictionary
#     """
#     res = []
#     for k, v in styreport.items():
#         if '_val' in v or '_color' in v or len(v.items()) == 1:
#             res.append(styreport_resolvekv(k, v))
#         else:
#             print("no resolved ", k, v)
#             raise ValueError
#     res.append(*res.passthrough)
#     return res

# clss = tstr(tbl.fixed, bds.collapse, bds.separate)
# print(clss)

# print(tstr(opacity/40))

# print(tstr(pink/4))
# print(tstr(offset/pink/4))

# clss = tstr(ring/offset/pink/4)
# print(clss)
# exp = mr/x/auto
# res = exp.evaluate()
# print(res)
# clss = tstr(ring/offset/pink/4, duration/5, resize/5, ring/5)
# print(clss)
# clss = tstr(bd/st/5, bg/pink/5, ph/opacity/5, text/opacity/5)
# print(clss)

# clss = tstr(min/H/5)
# print(clss)

# print(tstr(container))

# print(tstr(W/5))

# print("scale = ", tstr(space/5, space/x/5))

# print("spacing = ", tstr(mr/x/5))
# print("spacing = ", tstr(mr/5))
# print(tstr(space/5))

# print(tstr(mr/sl/4))

# print(tstr(*[fz.xl, bg/gray/8,  fc/gray/6, ta.center, bt.bd,
#              bdr.md,   pd/1, shdw.md, mr/2, js.center, hover(bg/pink/4)]))

# print(tstr(bg/"transparent"))
# print(tstr(bd/2))
