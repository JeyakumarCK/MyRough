import cv2
import numpy as np

img = cv2.imread('IMG_JK2.jpg', cv2.IMREAD_COLOR)

cv2.line(img, (50,50), (150, 300), (255,0,0), 15)
cv2.rectangle(img, (100, 100), (300,300), (0,0,255), 5)
cv2.circle(img, (400, 400), 100, (0, 255, 0), -1)

pts = np.array([[180, 180],[250,200],[600, 40],[650,100],[300, 300]], np.int32)
cv2.polylines(img, [pts], True, (0,255,255), 5)

fnt = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'JK Sample Text', (650,50), fnt, 1, (200,255,255), 2, cv2.LINE_AA)

px = img[500,500]
print('Pixel color at 500,500', px)

blue = img[255,0,0]
print('Blue color pixels', blue)

# for i in range(400, 500):
#     for j in range(100, 200):
#         img[i,j] = np.subtract(img[i,j], [20,20,20])
#         print('Pixels written at 100,100', img[i,j])

cv2.imshow('Photo', img)
#cv2.imwrite('kiruk_img_jk.png', img)
cv2.waitKey(0)
cv2.destroyAllWindows()