import cv2
import numpy as np
from splite import splite_cude
from recognize import recognize_color


img = cv2.imread('cube2.png')
img1,img2=splite_cude(img,findboudaries=0)

cv2.imshow("img1",recognize_color(img1,name="img1"))
cv2.imshow("img2",recognize_color(img2,name="img2"))

cv2.waitKey(0)
cv2.destroyAllWindows()
