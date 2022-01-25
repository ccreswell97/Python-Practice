# script used to get the colors from the picture

import colorgram

colors = [color.rgb for color in colorgram.extract('hirst-nucleohistone.png', 50)]
tuple_color_values = [(color.r, color.g, color.b) for color in colors]
print(len(tuple_color_values))