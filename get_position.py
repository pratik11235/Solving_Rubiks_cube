def get_position_corner(object, color1, color2, color3):
    color1 = color1.upper()
    color2 = color2.upper()
    color3 = color3.upper()
    #check color1 at corner 1
    if object.t1 == color1 or object.ba7 == color1 or object.l3 == color1:
        # then color2
        if object.t1 == color2 or object.ba7 == color2 or object.l3 == color2:
            # and then color3
            if object.t1 == color3 or object.ba7 == color3 or object.l3 == color3:
                return 1
    if object.t3 == color1 or object.ba9 == color1 or object.r1 == color1:
        if object.t3 == color2 or object.ba9 == color2 or object.r1 == color2:
            if object.t3 == color3 or object.ba9 == color3 or object.r1 == color3:
                return 2
    if object.t7 == color1 or object.l9 == color1 or object.f1 == color1:
        if object.t7 == color2 or object.l9 == color2 or object.f1 == color2:
            if object.t7 == color3 or object.l9 == color3 or object.f1 == color3:
                return 3
    if object.r7 == color1 or object.t9 == color1 or object.f3 == color1:
        if object.r7 == color2 or object.t9 == color2 or object.f3 == color2:
            if object.r7 == color3 or object.t9 == color3 or object.f3 == color3:
                return 4
    if object.b7 == color1 or object.l1 == color1 or object.ba1 == color1:
        if object.b7 == color2 or object.l1 == color2 or object.ba1 == color2:
            if object.b7 == color3 or object.l1 == color3 or object.ba1 == color3:
                return 5
    if object.ba3 == color1 or object.r3 == color1 or object.b9 == color1:
        if object.ba3 == color2 or object.r3 == color2 or object.b9 == color2:
            if object.ba3 == color3 or object.r3 == color3 or object.b9 == color3:
                return 6
    if object.l7 == color1 or object.f7 == color1 or object.b1 == color1:
        if object.l7 == color2 or object.f7 == color2 or object.b1 == color2:
            if object.l7 == color3 or object.f7 == color3 or object.b1 == color3:
                return 7
    if object.f9 == color1 or object.r9 == color1 or object.b3 == color1:
        if object.f9 == color2 or object.r9 == color2 or object.b3 == color2:
            if object.f9 == color3 or object.r9 == color3 or object.b3 == color3:
                return 8
    return -1
    
def get_position_edge(object, color1, color2):
    if object.l2 == color1 or object.ba4 == color1:
        if object.l2 == color2 or object.ba4 == color2:
            return 1
    if object.r2 == color1 or object.ba6 == color1:
        if object.r2 == color2 or object.ba6 == color2:
            return 2
    if object.l8 == color1 or object.f4 == color1:
        if object.l8 == color2 or object.f4 == color2:
            return 3
    if object.f6 == color1 or object.r8 == color1:
        if object.f6 == color2 or object.r8 == color2:
            return 4
    if object.ba2 == color1 or object.b8 == color1:
        if object.ba2 == color2 or object.b8 == color2:
            return 5
    if object.l4 == color1 or object.b4 == color1:
        if object.l4 == color2 or object.b4 == color2:
            return 6
    if object.r6 == color1 or object.b6 == color1:
        if object.r6 == color2 or object.b6 == color2:
            return 7
    if object.f8 == color1 or object.b2 == color1:
        if object.f8 == color2 or object.b2 == color2:
            return 8
    return -1
    