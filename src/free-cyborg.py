def install_good_code(cyborg, code):
    cyborg = cyborg + code


def remove_bad_code(cyborg):
    for code in cyborg:
        if code is "bad":
            cyborg = cyborg - code
        else:
            continue