import cv2
import numpy as np
import os


img = cv2.imread(os.getcwd()+ '/images/pipes2.jpg',0)
equ = cv2.equalizeHist(img)
img = cv2.medianBlur(equ,5)
#output = img.copy()
cimg = cv2.cvtColor(equ, cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(equ, cv2.HOUGH_GRADIENT, 1 , 10,
                            param1=30,param2=50,  minRadius=5, maxRadius=30)

i=0
if circles is not None:
	# convert the (x, y) coordinates and radius of the circles to integers
	circles = np.round(circles[0, :]).astype("int")
	# loop over the (x, y) coordinates and radius of the circles
    
	for (x, y, r) in circles:
		i= i+1
        # draw the circle in the output image, then draw a rectangle
		# corresponding to the center of the circle
		cv2.circle(cimg, (x, y), r, (0, 255, 0), 1)
		cv2.rectangle(cimg, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
        
cv2.imshow('detected circles', cimg)
print (i)
cv2.waitKey(0)
cv2.destroyAllWindows()