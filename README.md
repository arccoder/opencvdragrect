# opencvdragrect

To drag a rectangle on an image window. Select the entire rectangle and move it around. Hold on to corner or a side and resize the rectangle.

![Preview gif](https://cdn.rawgit.com/arccoder/opencvdragrect/master/preview.gif "Preview Image")

## Usage

Import script
```python
import selectinwindow
rectI = selectinwindow.dragRect
```
Initialize the  drag object
```python
selectinwindow.init(rectI, image, imageWidth, imageHeight)
```
Set mouse click callback function
```python
cv2.setMouseCallback("image", selectinwindow.dragrect, rectI)
```

## Note
You might get the following error
```
RuntimeError: maximum recursion depth exceeded
```
To avoid this error, you might want to add the following code.
```python
import sys
sys.setrecursionlimit(10 ** 9)
```
It would help while holding the rectangle corner or edge for resizing the rectangle the dragging is done in increments by releasing the held corner or sides.

## References
1. Implementation on how to set callbacks and the infinite loop.
  *  [Capturing mouse click events with Python and OpenCV](http://www.pyimagesearch.com/2015/03/09/capturing-mouse-click-events-with-python-and-opencv/)
