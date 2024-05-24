import cv2
import numpy as np

from splite import splite_cude
from recognize import recognize_color

def video_demo():
    capture = cv2.VideoCapture(0)
    while(True):
        ret, frame = capture.read()
        frame = cv2.flip(frame, 1)
        cv2.imshow("video", frame)
        c = cv2.waitKey(50)
        if c == 27:
            img1,img2=splite_cude(frame,findboudaries=1)
            cv2.imshow("img1",recognize_color(img1,name="img1"))
            cv2.imshow("img2",recognize_color(img2,name="img2"))
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            break

video_demo()
cv2.destroyAllWindows()