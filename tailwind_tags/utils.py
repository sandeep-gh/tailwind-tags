from .style_tags import bg, from_, to_, via_

def gradient(from_color_idvexpr, to_color_idivexpr, via_color_idivexpr=None):
    """
    for now only considering bg gradient
    """
    
    return [bg/"gradient-to-r",  from_/from_color_idvexpr, to_/to_color_idivexpr, via_/via_color_idivexpr]
