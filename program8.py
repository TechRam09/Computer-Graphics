import cv2
import numpy as np

image_path = ('./gojo.png')
img = cv2.imread(image_path)

height,width,_ = img.shape

rotation_matrix = cv2.getRotationMatrix2D((width/2,height/2),45,1)
translation_matrix = np.float32([[1,0,100],[0,1,50]])
scaling_matrix = np.float32([[1.5,0,0],[0,1.5,0]])

rotation_img = cv2.warpAffine(img,rotation_matrix,(width,height))
translation_img = cv2.warpAffine(img,translation_matrix,(width,height))
scaling_img = cv2.warpAffine(img,scaling_matrix,(int(width*1.5),int(height*1.5)))

cv2.imshow('OG',img)
cv2.imshow('RM', rotation_img)
cv2.imshow('TM', translation_img)
cv2.imshow('SM', scaling_img)

cv2.waitKey(0)
cv2.destroyAllWindows()