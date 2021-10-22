import os
import json
from addict import Dict


class _ColorBase:
    mycolor = None

    @ classmethod
    def __truediv__(cls, colorval):
        return f"{cls.mycolor}-{colorval}00"

    @classmethod
    def evaluate(cls, colorval):
        return f"{cls.mycolor}-{colorval}00"
        pass

    @ classmethod
    def __pow__(cls, colorval):
        return f"{cls.mycolor}-{colorval}00"

    @classmethod
    def __repr__(cls):
        return f"{cls.mycolor}"


blueGray = coolGray = gray = trueGray = warmGray = red = orange = amber = yellow = lime = green = emerald = teal = cyan = lightBlue = blue = indigo = violet = purple = fuchsia = pink = rose = None

_tw_color_list = ["blueGray", "coolGray", "gray", "trueGray", "warmGray", "red", "orange", "amber", "yellow", "lime",
                  "green", "emerald", "teal", "cyan", "lightBlue", "blue", "indigo", "violet", "purple", "fuchsia", "pink", "rose"]

for color in _tw_color_list:
    globals()[color.capitalize()] = type(color.capitalize(), (_ColorBase,),

                                         {'mycolor': color})

    globals()[color] = globals()[color.capitalize()]()

onetonine = ["_", "i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix"]

with open(os.path.dirname(__file__) + "/palette-v2x.json", 'r') as fh:
    _twccd = json.load(fh)

twcc2hex = Dict()
for cc in _twccd.keys():
    if cc not in ['black', 'white']:
        for i in range(1, 10):
            rn = onetonine[i]
            twcc2hex[cc][rn] = _twccd[cc][f"{i}00"]
