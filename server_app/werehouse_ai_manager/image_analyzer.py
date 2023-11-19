import cv2

image = cv2.imread("data_img/img1.jpg")

gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

_, thresh_image = cv2.threshold(gray_image,220,255,cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(thresh_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.imshow("windows",image)

cv2.waitKey()