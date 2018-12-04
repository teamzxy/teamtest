import cv2

#change
#feature 사용해서 바꿨당~ㄴ
#다시확인 
img_orign= cv2.imread('number2.jpg')
img_orign2 = img_orign

img = cv2.imread('number2.jpg',0)

blur = cv2.GaussianBlur(img,(3,3),0)

canny = cv2.Canny(blur,100,200)



box1=[]
f_count = 0
cnts,contours,hierarchy = cv2.findContours(canny,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for i in range(len(contours)):
    cnt = contours[i]
    area = cv2.contourArea(cnt)
    x,y,w,h = cv2.boundingRect(cnt)
    rect_area = w*h
    ratio = float(w)/h

    if(ratio>=0.2) and (ratio<=1.0) and (rect_area>=100) and (rect_area<=700):
        cv2.rectangle(img_orign2,(x,y),(x+w,y+h),(255,0,0),1)
        box1.append(cv2.boundingRect(cnt))
        

for i in range(len(box1)): # Bubble Sorting
    for j in range(len(box1)-(i+1)):
        if box1[j][0] > box1[j+1][0] :
            temp = box1[j]
            box1[j] = box1[j+1]
            box1[j+1] = temp

for m in range(len(box1)):
    CNT = 0

    for n in range(m+1,(len(box1)-1)):
        delta_x = abs(box1[n][0] - box1[m][0]) # x1 - x0
        if delta_x > 150:
            break
        delta_y = abs(box1[n][1] - box1[m][1]) # y1 - y0
        if delta_x ==0:
            delta_x=1
        if delta_y ==0:
            delta_y=1
        gradient = float(delta_y) / float(delta_x)
        if gradient < 0.25:
            CNT = CNT+1
    if CNT > f_count:
        select = m
        f_count = CNT
        plate_width = delta_x
        
img_orign3= cv2.imread('number2.jpg')

car_number = img_orign3[box1[select][1]-10:box1[select][3]+box1[select][1]+20,box1[select][0]-10:140+box1[select][0]]
cv2.imshow('num',car_number)
cv2.imshow('orign',img_orign)
cv2.waitKey(0)
cv2.destroyAllWindows()
#rsz_img = cv2.resize(img,(28,28),interpolation=cv2.INTER_AREA)
#image = cv2.adaptiveThreshold(rsz_img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)
