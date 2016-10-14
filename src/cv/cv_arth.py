import numpy as np
import cv2

img1 = cv2.imread('img1.jpg', cv2.IMREAD_COLOR)
img2 = cv2.imread('logo2.jpg', cv2.IMREAD_COLOR)

rows, cols, channels = img2.shape
print("rows, cols, channels are ", rows, cols, channels)
roi = img1[0:rows, 0:cols]
cv2.imshow('roi', roi)

img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask1 = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)
mask_inv = cv2.bitwise_not(mask1)

img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
img2_fg = cv2.bitwise_and(img2, img2, mask=mask1)
dst = cv2.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst

cv2.imshow('img2gray', img2gray)
cv2.imshow('mask1', mask1)
cv2.imshow('mask_inv', mask_inv)
cv2.imshow('img1_bg', img1_bg)
cv2.imshow('img2_fg', img2_fg)
cv2.imshow('dst', dst)
cv2.imshow('img1', img1)


# add = img1 + img2
# print(add)
# print("-----------------------------")
# addn = cv2.add(img1, img2)
# addn = cv2.subtract(img1, img2)

# weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0) 

# cv2.imshow('Added image', add)
# cv2.imshow('Added image', weighted)


cv2.waitKey(0)
cv2.destroyAllWindows()