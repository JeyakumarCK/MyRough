import numpy as np
import cv2
import matplotlib.pyplot as plt


img = cv2.imread('IMG_JK1.jpg', cv2.IMREAD_COLOR)

print(img[55, 55])
img[55, 55] = [255, 255, 255]
print(img[55, 55])

# img[50:150, 350:450] = [255, 255, 255]

my_face = img[40:340, 400:700]
print(len(my_face))
img[0:300, 0:300] = my_face

# watch_face = img[37:111, 107:194]
# img[500:574, 300:387] = watch_face

cv2.imshow('Image', img)

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGBA), interpolation='bicubic')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()