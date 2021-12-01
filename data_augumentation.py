import cv2 
import numpy as np
import os

def rotate_image(image, angle):
    image_center = tuple(np.array(image.shape[1::-1]) / 2)
    rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
    result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
    return result

folders = ['negative','positive']
for folder in folders:
    images = os.listdir(folder)
    for image in images:
        img = cv2.imread(folder+'/'+image)
        for i in range(0,360,90):
            print(i)
            rot = rotate_image(img, i)
            cv2.imshow('ball',rot)
            cv2.imwrite('dataset/'+folder+'/'+str(i)+'__'+image[:-4]+'.png', rot)
            key = cv2.waitKey(2)
            if key == 'q':
                break
