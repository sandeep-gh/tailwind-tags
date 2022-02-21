from tailwind_tags import *
import tailwind_tags as tt
# res = get_styReport(text/gray/6, mr/sb/2, mr/x/auto, W/6, G/cols/6)
from addict import Dict
# from tests import styreport_resolve
import pickle
import json
import jsbeautifier


# itm = hover(noop/fw.bold)
# print(itm[0].modifier_chain)
# print(tstr(*itm))
# hover: fc/gray/"5"
# print(tstr(*hover(fc/gray/"5", *variant(*placeholder(noop/fw.bold), rv='md'), auto)))
# for arg in hover(fc/gray/"5", *variant(*placeholder(fw.bold), rv='md'), auto):
#     print(arg)
#     print(arg.modifier_chain)


# print(hover(fc/gray/"5", *variant(*placeholder(fw.bold), rv='md'), auto), bg/green/5)
# res = tt.styClause.to_json(
#     *focus(*hover(*placeholder(fc/gray/5))))

# res = tt.styClause.to_json(
#     *hover(fc/gray/"5", *variant(*placeholder(noop/fw.bold), rv='md'), auto), bg/green/5)

#print(tstr(*hover(*focus(bg/green/400), *focus(*placeholder(noop/fw.bold), fc/pink/100))))
res = tt.styClause.to_json(
    *hover(*focus(bg/green/400), *focus(*placeholder(noop/fw.bold), fc/pink/100)))
#opts = jsbeautifier.default_options()
#print(jsbeautifier.beautify(json.dumps(res), opts))
# print(res)

claus = tt.styClause.to_clause(res)
print(tstr(*claus))

# print(tstr(*claus))
# print("tstr = ", tstr(pd/x/4, bold, fc/gray/"50",
#                       mr/sb/2, Outline.n, bsw.lg))
# res = tt.styClause.to_json(pd/x/4, bold, fc/gray/"50",
#                            mr/sb/2, Outline.n, bsw.lg)

# # res = tt.styClause.to_json(fc/gray/50
# #                           )
# print(res)
# print(tstr(*tt.styClause.to_clause(res)))
# res = get_styReport()
# with open("styreport.json", "wb") as fh:
#     pickle.dump(json.dumps(res), fh)

# # print(res)
# #k, v = list(res.items())[0]
# #enc = styreport_resolve(res)
# print(enc)
