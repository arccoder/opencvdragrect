# opencvdragrect

To drag a rectangle on an image window. Select the entire rectangle and move it around. Hold on to corner or a side and resize the rectangle.

![Preview gif](https://cdn.rawgit.com/arccoder/opencvdragrect/master/preview.gif "Preview Image")

## Usage

Import script and Initialize the  drag object
```python
import selectinwindow
windowName = 'named window'
rectI = selectinwindow.DragRectangle(image, windowName, imageWidth, imageHeight))
```
Set mouse click callback function
```python
cv2.setMouseCallback(windowName, selectinwindow.dragrect, rectI)
```
**Double click** inside the dragged rectangle to finalize the location of the rect
The rectangle location can be accessed anytime through outRect
```python
rectI.outRect
``` 
Example of the usage can be found in ```script.py```

## Update - Jan 2021
- Modified code for Python 3.8.3 and OpenCV 4.5.1
- Renamed dragRect class to DragRectangle
- Moved init function into the DragRectangle class
- New preview gif
- Resolved a bug with the cv2.rectangle function call.  
    The function only takes whole numbers and not decimal numbers.
    Decimal numbers produce a error "Function takes 4 arguments, only 2 given"

## Note
You might get the following error
```
RuntimeError: maximum recursion depth exceeded
```
To avoid this error, you can add the following code.
```python
import sys
sys.setrecursionlimit(10 ** 9)
```
It would help, while holding the rectangle corner or edge for resizing the rectangle the dragging is done in increments by releasing the held corner or sides intermittently.

## References
1. Implementation on how to set callbacks and the infinite loop.
    
    [Capturing mouse click events with Python and OpenCV](http://www.pyimagesearch.com/2015/03/09/capturing-mouse-click-events-with-python-and-opencv/)
    
2. Mouse callback events documentation
    
    [OpenCV 4.5.0 High-level GUI](https://docs.opencv.org/4.5.1/d7/dfc/group__highgui.html)