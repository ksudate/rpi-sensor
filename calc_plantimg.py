import numpy as np
import datetime
import sys
import cv2
import os

imgdir_path = '/home/pi/img/'
today = datetime.datetime.today().strftime('%Y-%m-%d-%H')
img_path = imgdir_path + today + '-00' + '.jpg'
if not os.path.exists(img_path):
    sys.exit()

img = cv2.imread(img_path)
hsv_min = np.array([30, 64, 0])
hsv_max = np.array([90,255,255])
HSV_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
mask = cv2.inRange(HSV_img, hsv_min, hsv_max)
masked_img = cv2.bitwise_and(img, img, mask=mask)
pixel = round(mask[np.nonzero(mask)].size / mask.size * 100)

path_pixel ='/home/pi/log/plantpixel.log'
today = datetime.datetime.today().strftime("%Y/%m/%d %H:%M")
with open(path_pixel, mode='a') as f:
    f.write(f'{today} {pixel}\n')

#np.set_printoptions(threshold=np.inf)
#print(np.max(mask, axis=0))
#cv2.imshow("image", masked_img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


