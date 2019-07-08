
def createBuffer(m : int,n : int):
    """#creates buffer with size of m * n"""
    buff = [["  "] * m for i in range(n)]
    return buff

def printBuffer(buff):
    """#prints two demensional buffer to the console"""
    for row in buff: 
        print('|', end = '')
        for char in row:
            print(char, end = '')
        print("|", end = "\n")

def putPoint(buff, x, y):
    """ #puts ## line in x,y in two demensional buffer"""
    if(x < len(buff) and y <len(buff[x]) and x > -1 and y > -1):
        buff[x][y] = "##"
   

def __put_line_high(buff, x0 , y0 , x1 , y1 ):
    dx = x1 - x0
    dy = y1 - y0
    xi = 1

    if (dx< 0):
        xi = -1
        dx = -dx

    dErr = 2*dx - dy
    x = x0
    y = 0
    for y in range(int(y0), int(y1)):
        putPoint(buff, x, y)
        if (dErr >0 ):
            x += xi
            dErr -= 2*dy
        dErr += 2*dx


def __put_line_low(buff, x0 , y0 , x1 , y1 ):
    dx = x1 - x0
    dy = y1 - y0
    yi = 1

    if (dy < 0):
        yi = -1
        dy = -dy

    dErr = 2*dy - dx
    y = y0
    x = 0
    for x in range(int(x0), int(x1)):
        putPoint(buff, x, y)
        if (dErr >0 ):
            y += yi
            dErr -= 2*dx
        dErr += 2*dy



def putLine(buff, x0, y0, x1, y1):
    """#puts new line in two demensional buffer with beginig in x0, y0 and ending in x1, y1"""
    if(abs(y1 - y0) < abs(x1 - x0)):
        if(x0 > x1):
            __put_line_low(buff, x1, y1, x0, y0)
        else:
            __put_line_low(buff, x0, y0, x1, y1)
    else:
        if(y0 > y1):
            __put_line_high(buff, x1, y1, x0, y0)
        else:
            __put_line_high(buff, x0, y0, x1, y1)
    



def putTriangle(buff, x0, y0, x1, y1, x2, y2):
    """#puts in two demensional buffer a non filled triangle """
    putLine(buff, x0, y0, x1, y1)
    putLine(buff, x1, y1, x2, y2)
    putLine(buff, x2, y2, x0, y0)


def putFilledTriangle(buff, x0, y0, x1, y1, x2, y2):
    """#puts in two demensional buffer a filled triangle""" 
    if (y0 > y1):
        t = y0
        y0 = y1
        y1 = t

        t = x0
        x0 = x1
        x1 = t

    if (y0 > y2):
        t = y0
        y0 = y2
        y2 = t

        t = x0
        x0 = x2
        x2 = t

    if (y1 > y2):
        t = y1
        y1 = y2
        y2 = t

        t = x1
        x1 = x2
        x2 = t

        #im lazy to write normal sorting)))

    triangleHeight = y2 - y0

    if(triangleHeight > 0):
        pxA = 0
        pxB = 0
        segmentHeight = y1 - y0
        i = 0

        if(segmentHeight > 0):
            t = 0.0
            for py in range(y0, y1):
                pxA = (py - y0)/triangleHeight
                pxB = (py - y0)/segmentHeight

                pxA = x0 + (x2 - x0)*pxA
                pxB = x0 + (x1 - x0)*pxB
                if(pxA > pxB):
                     t = pxA
                     pxA = pxB
                     pxB = t
                for i in range(int(pxA), int(pxB)):
                    putPoint(buff, i, py)
        
        segmentHeight = y2 - y1

        if(segmentHeight > 0):
            t = 0.0

            for py in range(y1, y2):
                pxA = (py - y0)/triangleHeight
                pxB = (py - y1)/segmentHeight
                pxA = x0 + (x2 - x0)*pxA
                pxB = x1 + (x2 - x1)*pxB
                if(pxA > pxB):
                    t = pxA
                    pxA = pxB
                    pxB  = t

                for i in range(int(pxA), int(pxB)):
                    putPoint(buff, i, py)





    


if __name__ == "__main__":
    #start = Point(10,10)
    #end = Point(45, 56)

    buffer = createBuffer(48, 48)

    putPoint(buffer, 6, 16)

    putLine(buffer, 4, 56, 48, 16)

    # putLine(buffer, 2,2, 30,2)

    # putLine(buffer, 30,4, 2,4)

    # putLine(buffer, 2, 6, 2, 30)

    # putLine(buffer, 4, 30, 4, 6)

    # putLine(buffer, 8, 6, 30, 28)

    # putLine(buffer, 28, 30, 6, 8)

    # putLine(buffer, 27, 6, 6, 27)

    # putLine(buffer, 8, 29, 29, 8)
 
 

    putTriangle(buffer, 4, 4, 24, 6, 16, 24)

    putFilledTriangle(buffer, 16, 48, 48, 36, 24, 16)

    printBuffer(buffer)

