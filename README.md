# opencvdragrect

To drag a rectangle on an image window. Select the entire rectangle and move it around. Hold on to corner or a side and resize the rectangle.

![Preview gif](https://cdn.rawgit.com/arccoder/opencvdragrect/master/preview.gif "Preview Image")

## Usage

Import script
```python
import selectinwindow
windowName = 'named window'
rectI = selectinwindow.dragRect
```
Initialize the  drag object
```python
selectinwindow.init(rectI, image, windowName, imageWidth, imageHeight)
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
  *  [Capturing mouse click events with Python and OpenCV](http://www.pyimagesearch.com/2015/03/09/capturing-mouse-click-events-with-python-and-opencv/)
2. Mouse callback events documentation
  *  [OpenCV 3.1.0 High-level GUI](http://docs.opencv.org/3.1.0/d7/dfc/group__highgui.html)