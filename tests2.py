from tailwind_tags import *
import tailwind_tags as tt
#res = get_styReport(text/gray/6, mr/sb/2, mr/x/auto, W/6, G/cols/6)
from addict import Dict
#from tests import styreport_resolve
import pickle
import json
res = get_styReport(pd/x/4, bold, fc/gray/1, mr/sb/2, Outline.n)
with open("styreport.json", "wb") as fh:
    pickle.dump(json.dumps(res), fh)

# print(res)
#k, v = list(res.items())[0]
enc = styreport_resolve(res)
print(enc)
