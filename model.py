import numpy as np
import cv2

#path = input("Enter the location of men image :")
#shirt = input("Enter the location of shirt :")



frame = cv2.imread('red_shirt.jpg')
frame = cv2.resize(frame,(400,400))
#frame = cv2.imread('test.jpg')
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

color_hsv1 = input("Enter the color of men dress among these (red,green,black,yellow,pink,white,orange) : ")
color_hsv = color_hsv1.lower()

color = {'red': [[0, 50, 50], [10, 255, 255]], 'green': [[25, 52, 70], [102, 255, 255]],
         'black': [[0, 0, 0], [180, 255, 30]], 'yellow': [[30, 100, 250], [40, 255, 255]],
         'pink': [[160, 50, 50], [180, 255, 255]], 'white': [[0, 0, 231], [180, 18, 255]],
         'orange': [[10, 50, 70], [24, 255, 255]]}
if color_hsv in color.keys():
    lst = color[color_hsv]
    upper = lst[0]
    lower = lst[1]


else:
    print("There is no available of hsv value")
lower_green = np.array(upper)
upper_green = np.array(lower)





# define range of green color in HSV
#lower_green = np.array([25, 52, 72])
#upper_green = np.array([102, 255, 255])
# Threshold the HSV image to get only blue colors
mask_white = cv2.inRange(hsv,lower_green, upper_green)
mask_black = cv2.bitwise_not(mask_white)

#converting mask_black to 3 channels
W,L = mask_black.shape
mask_black_3CH = np.empty((W, L, 3), dtype=np.uint8)
mask_black_3CH[:, :, 0] = mask_black
mask_black_3CH[:, :, 1] = mask_black
mask_black_3CH[:, :, 2] = mask_black

cv2.imshow('orignal',frame)
cv2.imshow('mask_black',mask_black_3CH)

dst3 = cv2.bitwise_and(mask_black_3CH,frame)
cv2.imshow('Pic+mask_inverse',dst3)

#///////
W,L = mask_white.shape
mask_white_3CH = np.empty((W, L, 3), dtype=np.uint8)
mask_white_3CH[:, :, 0] = mask_white
mask_white_3CH[:, :, 1] = mask_white
mask_white_3CH[:, :, 2] = mask_white

cv2.imshow('Wh_mask',mask_white_3CH)
dst3_wh = cv2.bitwise_or(mask_white_3CH,dst3)
cv2.imshow('Pic+mask_wh',dst3_wh)

#/////////////////

# changing for design
design = cv2.imread('d_1.jpg')
design = cv2.resize(design, mask_black.shape[1::-1])
cv2.imshow('design resize',design)

design_mask_mixed = cv2.bitwise_or(mask_black_3CH,design)
cv2.imshow('design_mask_mixed',design_mask_mixed)

final_mask_black_3CH = cv2.bitwise_and(design_mask_mixed,dst3_wh)
cv2.imshow('final_out',final_mask_black_3CH)


cv2.waitKey()