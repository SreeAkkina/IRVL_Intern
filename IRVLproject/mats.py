import cv2 
import matplotlib.pyplot as mp
import matplotlib.image as im 
import numpy as np

count = 0
list_x = [650, 658, 660, 663, 668, 674, 681, 691, 702, 710, 717, 725, 731, 739, 742]
list_y = [460, 453, 451, 450, 452, 457, 458, 468, 478, 494, 507, 518, 529, 541, 550]
for n in range(15):
    
    name = "color_" + str(count) + ".jpg"
    img = cv2.imread(name)
    x = list_x[count]
    y = list_y[count]
    cv2.rectangle(img,(x-90,y-90),(x+90,y+90),(0,255,0),2)
    cv2.line(img,(x-10,y),(x+10,y),(0,0,255),2)
    cv2.line(img,(x,y-10),(x,y+10),(0,0,255),2)
    mp.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    mp.show()
    directory = "/home/irvl/Documents/IRVLproject/BindedBoxImages/binding_box" + str(count) + ".jpg"
    status = cv2.imwrite(directory, img)
    count=count+1