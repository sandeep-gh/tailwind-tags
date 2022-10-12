from tailwind_tags import *

res  = ovf/y/auto
print (tstr(res))
assert tstr(res) == "overflow-y-auto"

all_exprs = [ovf/auto, ovf/hidden, ovf/clip, ovf/visible/ ovf/scroll, ovf/x/auto, ovf/y/auto, ovf/y/hidden, ovf/x/clip, ovf/y/scroll]

for _ in all_exprs:
    print(tstr(_))
