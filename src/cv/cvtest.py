import cv2 as cv
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

def print_version():
    print ("OpenCV version ", cv.__version__)
    print ("Numpy version ", np.__version__)
    print ("MatPlotLib version ", mpl.__version__)
    
print_version()

img = cv.imread('IMG_JK1.jpg', cv.IMREAD_GRAYSCALE)

#Image shown using CV
cv.imshow('Showing Image', img)
cv.imshow('Showing Image - Gray', gray_img)

cv.waitKey(0)
cv.destroyAllWindows()
#cv.imwrite('Img_jk1.png', img)

#Image shown using matplotlib
# plt.imshow(img, cmap='gray', interpolation='bicubic')
# plt.plot([500, 2000], [1500, 1000], 'c', linewidth=5)
# plt.show()




print('Program ended gracefully')