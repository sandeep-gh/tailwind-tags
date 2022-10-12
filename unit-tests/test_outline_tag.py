from tailwind_tags import *
tags = [outline/black, outline/2, outline/double, outline/offset/2]
print (tstr(*tags))
        
twlist = []
add_to_twtag_list(twlist, outline/black)
add_to_twtag_list(twlist, outline/2)

print(twlist)
