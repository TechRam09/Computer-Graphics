import cv2
# import numpy as np

image_path = ('./blocks.webp')
img = cv2.imread(image_path)



gaussian_blur = cv2.GaussianBlur(img,(5,5),0)

median_blur = cv2.medianBlur(img,5)

bilateral_filter = cv2.bilateralFilter(img,9,75,75)

cv2.imshow('og',img)
cv2.imshow('gb', gaussian_blur)
cv2.imshow('mb', median_blur)
cv2.imshow('bf', bilateral_filter)

cv2.waitKey(0)
cv2.destroyAllWindows()