import cv2
import numpy as np

def recognize_color(image):
# 分割为2*3的6块
    h, w, c = image.shape
    w_block = w // 3
    h_block = h // 3
# 定义颜色范围
# 颜色范围为RGB，分别为：绿色、红色、蓝色、黄色、橙色、白色
    Green=np.array([91.0014, 162.282, 29.18])
    Yellow=np.array([96.2879, 180.9527, 173.1877])
    Blue=np.array([136.2344, 75.2489, 15.8998])
    Red=np.array([57.0416, 58.6351, 207.5908])
    Orange=np.array([64.7215, 104.9028, 209.4985])
    white=np.array([184.1095, 176.4267, 176.7913])
    
    Color1l=Green-np.array([20,20,20])
    Color1h=Green+np.array([20,20,20])
    Color2l=Red-np.array([20,20,20])
    Color2h=Red+np.array([20,20,20])
    Color3l=Blue-np.array([20,20,20])
    Color3h=Blue+np.array([20,20,20])
    Color4l=Yellow-np.array([20,20,20])
    Color4h=Yellow+np.array([20,20,20])
    Color5l=Orange-np.array([20,20,20])
    Color5h=Orange+np.array([20,20,20])
    Color6l=white-np.array([20,20,20])
    Color6h=white+np.array([20,20,20])

    for i in range(3):   # 遍历行
        for j in range(3):   # 遍历列
            # 计算边界
            x1 = j * w_block
            y1 = i * h_block
            x2 = (j + 1) * w_block
            y2 = (i + 1) * h_block
            # 绘制边界
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
            # 计算当前块的中间区域平均颜色
            x1c=x1+w_block//4
            y1c=y1+h_block//4
            x2c=x2-w_block//4
            y2c=y2-h_block//4
            block = image[y1c:y2c, x1c:x2c]#block 是中心区域
            cv2.rectangle(image, (x1c, y1c), (x2c, y2c), (0, 0, 255), 2)

            avg_color = np.mean(block, axis=(0, 1))
            # 打印当前block的平均颜色
            print(avg_color.tolist())
            def tell_color(avg_color):
                if np.all(avg_color >= Color1l) and np.all(avg_color <= Color1h):
                    cv2.putText(image, 'Green', (x1c, y1c), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2)
                elif np.all(avg_color >= Color2l) and np.all(avg_color <= Color2h):
                    cv2.putText(image, 'Red', (x1c, y1c), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2)
                elif np.all(avg_color >= Color3l) and np.all(avg_color <= Color3h):
                    cv2.putText(image, 'Blue', (x1c, y1c), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2)
                elif np.all(avg_color >= Color4l) and np.all(avg_color <= Color4h):
                    cv2.putText(image, 'Yellow', (x1c, y1c), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2)
                elif np.all(avg_color >= Color5l) and np.all(avg_color <= Color5h):
                    cv2.putText(image, 'Orange', (x1c, y1c), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2)
                elif np.all(avg_color >= Color6l) and np.all(avg_color <= Color6h):
                    cv2.putText(image, 'White', (x1c, y1c), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2)
                else:
                    # 寻找和哪个颜色最接近   
                    colors=[Green,Red,Blue,Yellow,Orange,white]
                    closest_color=0
                    closest_norm=np.linalg.norm(avg_color-colors[0])

                    for i in range(6):
                        norm=np.linalg.norm(avg_color-colors[i])
                        if norm<closest_norm:
                            closest_color=i
                            closest_norm=norm
                    cv2.putText(image, ['Green','Red','Blue','Yellow','Orange','White'][closest_color], (x1c, y1c), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

            # 判断当前块的颜色是否在颜色范围内
            tell_color(avg_color)

    cv2.imshow('image', image)
    cv2.imwrite('result2.jpg', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

