import cv2
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

def print_version():
    print ("OpenCV version ", cv2.__version__)
    print ("Numpy version ", np.__version__)
    print ("MatPlotLib version ", mpl.__version__)
    
print_version()

img = cv2.imread('IMG_JK1.jpg', cv2.IMREAD_GRAYSCALE)

#Image shown using CV
cv2.imshow('Showing Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#cv2.imwrite('Img_jk1.png', img)

#Image shown using matplotlib
# plt.imshow(img, cmap='gray', interpolation='bicubic')
# plt.plot([500, 2000], [1500, 1000], 'c', linewidth=5)
# plt.show()

print('Program ended gracefully')