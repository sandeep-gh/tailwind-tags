""" check if two tailwind class bg-green-100, bg-pink-100 belong to same tag (like bg)
"""


from tailwind_tags import *

# taglist = [bg/gray/1, fc/gray/6,  mr/sr/1, mr/sb/1, pd/x/4, pd/y/2, bold, bsw._, bsw.sm,
#           bdr.md, bold, *hover(noop/bsw.md, bg/gray/2)
# ]

taglist = [W/6, H/6, bg/gray /
          7, fc/pink/2, bdr.full, mr/x/2, *hover(noop/bds.double, noop/bt.bd, bg/gray/1, bd/gray/2)]


assert tstr(bg/gray/7) in tstr(*taglist)
res =   conc_twtags(*taglist, bg/pink/4)
assert tstr(bg/gray/7) not in tstr(*res)
assert tstr(bg/pink/4)  in tstr(*res)


src = outline/gray/4
des = outline/blue/4
taglist = [src]
assert tstr(src) in tstr(*taglist)
res = conc_twtags(*taglist, des)
assert tstr(src) not in tstr(*res)
assert tstr(des)  in tstr(*res)

def test_insert(src, des, taglist=[]):
    taglist.append(src)
    assert tstr(src) in tstr(*taglist)
    res = conc_twtags(*taglist, des)
    assert tstr(src) not in tstr(*res)
    assert tstr(des)  in tstr(*res)
    return res


res = test_insert(olsty.double, olsty.dotted)
print (tstr(*res))





taglist = [auto]
remove_from_twtag_list(taglist, auto)
print(taglist)
