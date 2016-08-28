# MIT License

# Copyright (c) 2016 Akshay Chavan

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import cv2


class Rect:
    x = None
    y = None
    w = None
    h = None

    def printit(self):
        print str(self.x) + ',' + str(self.y) + ',' + str(self.w) + ',' + str(self.h)


# endclass

class dragRect:
    # Limits on the canvas
    keepWithin = Rect()
    # To store rectangle
    outRect = Rect()
    # To store rectangle anchor point
    # Here the rect class object is used to store
    # the distance in the x and y direction from
    # the anchor point to the top-left and the bottom-right corner
    anchor = Rect()
    # Selection marker size
    sBlk = 4
    # Whether initialized or not
    initialized = False

    # Image
    image = None

    # Window Name
    wname = ""

    # Return flag
    returnflag = False

    # FLAGS
    # Rect already present
    active = False
    # Drag for rect resize in progress
    drag = False
    # Marker flags by positions
    TL = False
    TM = False
    TR = False
    LM = False
    RM = False
    BL = False
    BM = False
    BR = False
    hold = False


# endclass

def init(dragObj, Img, windowName, windowWidth, windowHeight):
    # Image
    dragObj.image = Img

    # Window name
    dragObj.wname = windowName

    # Limit the selection box to the canvas
    dragObj.keepWithin.x = 0
    dragObj.keepWithin.y = 0
    dragObj.keepWithin.w = windowWidth
    dragObj.keepWithin.h = windowHeight

    # Set rect to zero width and height
    dragObj.outRect.x = 0
    dragObj.outRect.y = 0
    dragObj.outRect.w = 0
    dragObj.outRect.h = 0


# enddef

def dragrect(event, x, y, flags, dragObj):
    if x < dragObj.keepWithin.x:
        x = dragObj.keepWithin.x
    # endif
    if y < dragObj.keepWithin.y:
        y = dragObj.keepWithin.y
    # endif
    if x > (dragObj.keepWithin.x + dragObj.keepWithin.w - 1):
        x = dragObj.keepWithin.x + dragObj.keepWithin.w - 1
    # endif
    if y > (dragObj.keepWithin.y + dragObj.keepWithin.h - 1):
        y = dragObj.keepWithin.y + dragObj.keepWithin.h - 1
    # endif

    if event == cv2.EVENT_LBUTTONDOWN:
        mouseDown(x, y, dragObj)
    # endif
    if event == cv2.EVENT_LBUTTONUP:
        mouseUp(x, y, dragObj)
    # endif
    if event == cv2.EVENT_MOUSEMOVE:
        mouseMove(x, y, dragObj)
    # endif
    if event == cv2.EVENT_LBUTTONDBLCLK:
        mouseDoubleClick(x, y, dragObj)
    # endif

# enddef

def pointInRect(pX, pY, rX, rY, rW, rH):
    if rX <= pX <= (rX + rW) and rY <= pY <= (rY + rH):
        return True
    else:
        return False
    # endelseif


# enddef

def mouseDoubleClick(eX, eY, dragObj):
    if dragObj.active:

        if pointInRect(eX, eY, dragObj.outRect.x, dragObj.outRect.y, dragObj.outRect.w, dragObj.outRect.h):
            dragObj.returnflag = True
            cv2.destroyWindow(dragObj.wname)
        # endif

    # endif


# enddef

def mouseDown(eX, eY, dragObj):
    if dragObj.active:

        if pointInRect(eX, eY, dragObj.outRect.x - dragObj.sBlk,
                       dragObj.outRect.y - dragObj.sBlk,
                       dragObj.sBlk * 2, dragObj.sBlk * 2):
            dragObj.TL = True
            return
        # endif
        if pointInRect(eX, eY, dragObj.outRect.x + dragObj.outRect.w - dragObj.sBlk,
                       dragObj.outRect.y - dragObj.sBlk,
                       dragObj.sBlk * 2, dragObj.sBlk * 2):
            dragObj.TR = True
            return
        # endif
        if pointInRect(eX, eY, dragObj.outRect.x - dragObj.sBlk,
                       dragObj.outRect.y + dragObj.outRect.h - dragObj.sBlk,
                       dragObj.sBlk * 2, dragObj.sBlk * 2):
            dragObj.BL = True
            return
        # endif
        if pointInRect(eX, eY, dragObj.outRect.x + dragObj.outRect.w - dragObj.sBlk,
                       dragObj.outRect.y + dragObj.outRect.h - dragObj.sBlk,
                       dragObj.sBlk * 2, dragObj.sBlk * 2):
            dragObj.BR = True
            return
        # endif

        if pointInRect(eX, eY, dragObj.outRect.x + dragObj.outRect.w / 2 - dragObj.sBlk,
                       dragObj.outRect.y - dragObj.sBlk,
                       dragObj.sBlk * 2, dragObj.sBlk * 2):
            dragObj.TM = True
            return
        # endif
        if pointInRect(eX, eY, dragObj.outRect.x + dragObj.outRect.w / 2 - dragObj.sBlk,
                       dragObj.outRect.y + dragObj.outRect.h - dragObj.sBlk,
                       dragObj.sBlk * 2, dragObj.sBlk * 2):
            dragObj.BM = True
            return
        # endif
        if pointInRect(eX, eY, dragObj.outRect.x - dragObj.sBlk,
                       dragObj.outRect.y + dragObj.outRect.h / 2 - dragObj.sBlk,
                       dragObj.sBlk * 2, dragObj.sBlk * 2):
            dragObj.LM = True
            return
        # endif
        if pointInRect(eX, eY, dragObj.outRect.x + dragObj.outRect.w - dragObj.sBlk,
                       dragObj.outRect.y + dragObj.outRect.h / 2 - dragObj.sBlk,
                       dragObj.sBlk * 2, dragObj.sBlk * 2):
            dragObj.RM = True
            return
        # endif

        # This has to be below all of the other conditions
        if pointInRect(eX, eY, dragObj.outRect.x, dragObj.outRect.y, dragObj.outRect.w, dragObj.outRect.h):
            dragObj.anchor.x = eX - dragObj.outRect.x
            dragObj.anchor.w = dragObj.outRect.w - dragObj.anchor.x
            dragObj.anchor.y = eY - dragObj.outRect.y
            dragObj.anchor.h = dragObj.outRect.h - dragObj.anchor.y
            dragObj.hold = True

            return
        # endif

    else:
        dragObj.outRect.x = eX
        dragObj.outRect.y = eY
        dragObj.drag = True
        dragObj.active = True
        return

    # endelseif


# enddef

def mouseMove(eX, eY, dragObj):
    if dragObj.drag & dragObj.active:
        dragObj.outRect.w = eX - dragObj.outRect.x
        dragObj.outRect.h = eY - dragObj.outRect.y
        clearCanvasNDraw(dragObj)
        return
    # endif

    if dragObj.hold:
        dragObj.outRect.x = eX - dragObj.anchor.x
        dragObj.outRect.y = eY - dragObj.anchor.y

        if dragObj.outRect.x < dragObj.keepWithin.x:
            dragObj.outRect.x = dragObj.keepWithin.x
        # endif
        if dragObj.outRect.y < dragObj.keepWithin.y:
            dragObj.outRect.y = dragObj.keepWithin.y
        # endif
        if (dragObj.outRect.x + dragObj.outRect.w) > (dragObj.keepWithin.x + dragObj.keepWithin.w - 1):
            dragObj.outRect.x = dragObj.keepWithin.x + dragObj.keepWithin.w - 1 - dragObj.outRect.w
        # endif
        if (dragObj.outRect.y + dragObj.outRect.h) > (dragObj.keepWithin.y + dragObj.keepWithin.h - 1):
            dragObj.outRect.y = dragObj.keepWithin.y + dragObj.keepWithin.h - 1 - dragObj.outRect.h
        # endif

        clearCanvasNDraw(dragObj)
        return
    # endif

    if dragObj.TL:
        dragObj.outRect.w = (dragObj.outRect.x + dragObj.outRect.w) - eX
        dragObj.outRect.h = (dragObj.outRect.y + dragObj.outRect.h) - eY
        dragObj.outRect.x = eX
        dragObj.outRect.y = eY
        clearCanvasNDraw(dragObj)
        return
    # endif
    if dragObj.BR:
        dragObj.outRect.w = eX - dragObj.outRect.x
        dragObj.outRect.h = eY - dragObj.outRect.y
        clearCanvasNDraw(dragObj)
        return
    # endif
    if dragObj.TR:
        dragObj.outRect.h = (dragObj.outRect.y + dragObj.outRect.h) - eY
        dragObj.outRect.y = eY
        dragObj.outRect.w = eX - dragObj.outRect.x
        clearCanvasNDraw(dragObj)
        return
    # endif
    if dragObj.BL:
        dragObj.outRect.w = (dragObj.outRect.x + dragObj.outRect.w) - eX
        dragObj.outRect.x = eX
        dragObj.outRect.h = eY - dragObj.outRect.y
        clearCanvasNDraw(dragObj)
        return
    # endif

    if dragObj.TM:
        dragObj.outRect.h = (dragObj.outRect.y + dragObj.outRect.h) - eY
        dragObj.outRect.y = eY
        clearCanvasNDraw(dragObj)
        return
    # endif
    if dragObj.BM:
        dragObj.outRect.h = eY - dragObj.outRect.y
        clearCanvasNDraw(dragObj)
        return
    # endif
    if dragObj.LM:
        dragObj.outRect.w = (dragObj.outRect.x + dragObj.outRect.w) - eX
        dragObj.outRect.x = eX
        clearCanvasNDraw(dragObj)
        return
    # endif
    if dragObj.RM:
        dragObj.outRect.w = eX - dragObj.outRect.x
        clearCanvasNDraw(dragObj)
        return
    # endif


# enddef

def mouseUp(eX, eY, dragObj):
    dragObj.drag = False
    disableResizeButtons(dragObj)
    straightenUpRect(dragObj)
    if dragObj.outRect.w == 0 or dragObj.outRect.h == 0:
        dragObj.active = False
    # endif

    clearCanvasNDraw(dragObj)


# enddef

def disableResizeButtons(dragObj):
    dragObj.TL = dragObj.TM = dragObj.TR = False
    dragObj.LM = dragObj.RM = False
    dragObj.BL = dragObj.BM = dragObj.BR = False
    dragObj.hold = False


# enddef

def straightenUpRect(dragObj):
    if dragObj.outRect.w < 0:
        dragObj.outRect.x = dragObj.outRect.x + dragObj.outRect.w
        dragObj.outRect.w = -dragObj.outRect.w
    # endif
    if dragObj.outRect.h < 0:
        dragObj.outRect.y = dragObj.outRect.y + dragObj.outRect.h
        dragObj.outRect.h = -dragObj.outRect.h
    # endif


# enddef

def clearCanvasNDraw(dragObj):
    # Draw
    tmp = dragObj.image.copy()
    cv2.rectangle(tmp, (dragObj.outRect.x, dragObj.outRect.y),
                  (dragObj.outRect.x + dragObj.outRect.w,
                   dragObj.outRect.y + dragObj.outRect.h), (0, 255, 0), 2)
    drawSelectMarkers(tmp, dragObj)
    cv2.imshow(dragObj.wname, tmp)
    cv2.waitKey()


# enddef

def drawSelectMarkers(image, dragObj):
    # Top-Left
    cv2.rectangle(image, (dragObj.outRect.x - dragObj.sBlk,
                          dragObj.outRect.y - dragObj.sBlk),
                  (dragObj.outRect.x - dragObj.sBlk + dragObj.sBlk * 2,
                   dragObj.outRect.y - dragObj.sBlk + dragObj.sBlk * 2),
                  (0, 255, 0), 2)
    # Top-Rigth
    cv2.rectangle(image, (dragObj.outRect.x + dragObj.outRect.w - dragObj.sBlk,
                          dragObj.outRect.y - dragObj.sBlk),
                  (dragObj.outRect.x + dragObj.outRect.w - dragObj.sBlk + dragObj.sBlk * 2,
                   dragObj.outRect.y - dragObj.sBlk + dragObj.sBlk * 2),
                  (0, 255, 0), 2)
    # Bottom-Left
    cv2.rectangle(image, (dragObj.outRect.x - dragObj.sBlk,
                          dragObj.outRect.y + dragObj.outRect.h - dragObj.sBlk),
                  (dragObj.outRect.x - dragObj.sBlk + dragObj.sBlk * 2,
                   dragObj.outRect.y + dragObj.outRect.h - dragObj.sBlk + dragObj.sBlk * 2),
                  (0, 255, 0), 2)
    # Bottom-Right
    cv2.rectangle(image, (dragObj.outRect.x + dragObj.outRect.w - dragObj.sBlk,
                          dragObj.outRect.y + dragObj.outRect.h - dragObj.sBlk),
                  (dragObj.outRect.x + dragObj.outRect.w - dragObj.sBlk + dragObj.sBlk * 2,
                   dragObj.outRect.y + dragObj.outRect.h - dragObj.sBlk + dragObj.sBlk * 2),
                  (0, 255, 0), 2)

    # Top-Mid
    cv2.rectangle(image, (dragObj.outRect.x + dragObj.outRect.w / 2 - dragObj.sBlk,
                          dragObj.outRect.y - dragObj.sBlk),
                  (dragObj.outRect.x + dragObj.outRect.w / 2 - dragObj.sBlk + dragObj.sBlk * 2,
                   dragObj.outRect.y - dragObj.sBlk + dragObj.sBlk * 2),
                  (0, 255, 0), 2)
    # Bottom-Mid
    cv2.rectangle(image, (dragObj.outRect.x + dragObj.outRect.w / 2 - dragObj.sBlk,
                          dragObj.outRect.y + dragObj.outRect.h - dragObj.sBlk),
                  (dragObj.outRect.x + dragObj.outRect.w / 2 - dragObj.sBlk + dragObj.sBlk * 2,
                   dragObj.outRect.y + dragObj.outRect.h - dragObj.sBlk + dragObj.sBlk * 2),
                  (0, 255, 0), 2)
    # Left-Mid
    cv2.rectangle(image, (dragObj.outRect.x - dragObj.sBlk,
                          dragObj.outRect.y + dragObj.outRect.h / 2 - dragObj.sBlk),
                  (dragObj.outRect.x - dragObj.sBlk + dragObj.sBlk * 2,
                   dragObj.outRect.y + dragObj.outRect.h / 2 - dragObj.sBlk + dragObj.sBlk * 2),
                  (0, 255, 0), 2)
    # Right-Mid
    cv2.rectangle(image, (dragObj.outRect.x + dragObj.outRect.w - dragObj.sBlk,
                          dragObj.outRect.y + dragObj.outRect.h / 2 - dragObj.sBlk),
                  (dragObj.outRect.x + dragObj.outRect.w - dragObj.sBlk + dragObj.sBlk * 2,
                   dragObj.outRect.y + dragObj.outRect.h / 2 - dragObj.sBlk + dragObj.sBlk * 2),
                  (0, 255, 0), 2)

# enddef