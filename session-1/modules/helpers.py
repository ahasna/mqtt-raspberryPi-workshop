def color_it(text, color):
    red = "\033[1;31;40m"
    green = "\033[1;32;40m"
    yellow = "\033[1;33;40m"
    cyan = "\033[1;36;40m"
    purple = "\033[1;35;40m"
    normal = "\033[0;37;40m"

    if color == "red":
        return "{}{}{}".format(red, text, normal)
    elif color == "green":
        return "{}{}{}".format(green, text, normal)
    elif color == "yellow":
        return "{}{}{}".format(yellow, text, normal)
    elif color == "cyan":
        return "{}{}{}".format(cyan, text, normal)
    elif color == "purple":
        return "{}{}{}".format(purple, text, normal)
    elif color == "white":
        return "{}{}{}".format(normal, text, normal)
    else:
        return text
