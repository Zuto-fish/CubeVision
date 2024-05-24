import cv2
import numpy as np
import _thread as thread



#TODO 优化 To get it better
def splite_cude(img,findboudaries,boundaries=[
            [[28,90],[254,24],[42,454],[260,495]],
            [[250,28],[546,81],[273,491],[532,441]]],width=600,height=600 ):    
        
    pts1 = np.float32(boundaries[0]) #划分第一张图的四个点
    pts2 = np.float32(boundaries[1]) #划分第二张图的四个点
    points = []
    if findboudaries:
        cv2.namedWindow('Image')
        def mouse_callback(event, x, y, flags, param):
            if event == cv2.EVENT_LBUTTONDOWN:
                points.append((x, y))
                print(f"Point recorded:=> ({x}, {y})")
        cv2.setMouseCallback('Image', mouse_callback)
        while len(points)<8:
            cv2.imshow('Image', img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        for pt in points[:4]:
                cv2.circle(img, pt, 5, (0, 0, 255), -1)
        for pt in points[4:8]:
                cv2.circle(img, pt, 5, (0, 255, 0), -1)
        print(np.float32(points))
        pts1=np.float32(points)[0:4]
        pts2=np.float32(points)[4:8]

    pts3 = np.float32([[0,0],[width,0],[0,height],[width,height]]) #转化为第一张图片
    pts4 = np.float32([[0,0],[width,0],[0,height],[width,height]]) #转化为第二张图片


    matrix1 = cv2.getPerspectiveTransform(pts1,pts3)
    imgOutput1 = cv2.warpPerspective(img,matrix1,(width,height)) #第一张图透视变换
    matrix2 = cv2.getPerspectiveTransform(pts2,pts4)
    imgOutput2 = cv2.warpPerspective(img,matrix2,(width,height)) #第二张图透视变换

    return imgOutput1,imgOutput2

