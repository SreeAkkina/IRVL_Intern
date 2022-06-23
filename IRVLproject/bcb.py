import cv2 
import matplotlib.pyplot as mp
import matplotlib.image as im 
import numpy as np
count = 6
move_x = 5
x = 650
move_y = 5
y = 460
for n in range(9):
    if(count>=6):
        move_y=4
    name = "color_" + str(count) + ".jpg"
    img = cv2.imread(name)
    x = x + move_x
    y = y + move_y
    cv2.rectangle(img,(x-90,y-90),(x+90,y+90),(0,255,0),2)
    mp.imshow(img)
    mp.show()
    #cv2.waitKey(4000)
    #cv2.destroyAllWindows()
    #directory = "/home/irvl/Documents/IRVLproject/cropped_image" + str(count) + ".jpg"
    #status = cv2.imwrite(directory, cropped_image)
    #print(status)
    count=count+1