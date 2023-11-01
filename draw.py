import numpy as np
import cv2 as cv

img = cv.imread('/home/paniz/Downloads/cityscape.jpeg' , cv.IMREAD_COLOR)

cv.line(img, (5,5) , (200,150) , (255,100,0),10)


cv.imshow('city' , img)
cv.waitKey(0)
cv.destroyAllWindows()