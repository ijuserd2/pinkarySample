

def check(bg_color, border_radius):
    bg_color_set = ""
    border_radius_set = ""

    if(border_radius == "Square"):
        border_radius_set = "0"
    elif(border_radius == "Round"):
        border_radius_set = "10px"
    else:
        border_radius_set = "50px"

    if(bg_color == "b-r-s-1"):
        bg_color_set = "to right,red,blue"
    elif(bg_color == "b-r-s-2"):
        bg_color_set = "to right,yellow,green"
    elif (bg_color == "b-r-s-3"):
        bg_color_set = "to right,orange,blue"
    elif (bg_color == "b-r-s-4"):
        bg_color_set = "to right,green,blue"
    elif (bg_color == "b-r-s-5"):
        bg_color_set = "to right,red,orange"
    else:
        bg_color_set = "to right,purple,blue"

    return [bg_color_set, border_radius_set]