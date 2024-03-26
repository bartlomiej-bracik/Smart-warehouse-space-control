import cv2
import learning_utils
import numpy as np
def analyzer(path):

    if(path == ''):
        image = cv2.imread("static/img/img2.jpg")
    else:
        image = cv2.imread(path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    blurred_img = cv2.GaussianBlur(image, (1, 1), 0)
    edges = cv2.Sobel(blurred_img, cv2.CV_64F, 1, 1, ksize=5)
    edges = np.uint8(np.absolute(edges))

    #_, threshold = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    _, threshold = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
    #edges = cv2.Canny(gray_image, 50, 150)
    contours, _ = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(image, contours, 1, (0, 255, 0), 12)

    contours_detected = []
    contours_area = 0
    space_area = 0

    count_of_counturs = 0
    img_coordinate = []
    #cv2.drawContours(image, contours, -1, (255, 255, 0), 10)
    for contour in contours:
        area = cv2.contourArea(contour)
        epsilon = 0.15 * cv2.arcLength(contour,True)
        approx = cv2.approxPolyDP(contour,epsilon,True)

        

        #Współrzedne elementów w magazynie
        if  len(approx) > 3 and len(approx) < 5 and area > 6000 and area < 100000   :
            contours_detected.append(approx)
            cv2.drawContours(image, [approx], 0, (0, 255, 0), 10)
            count_of_counturs += 1

            x,y,w,h = cv2.boundingRect(approx)
            x_mid = x+w/2
            y_mid = y + w/2
            cordin = learning_utils.Coordinate(x_mid,y_mid)
            contours_area = contours_area + area

            img_coordinate.append(cordin)
        #Współrzędne środka przestrzeni magazynowej
        if len(approx) > 3 and len(approx) < 5 and area > 100000 and area <2000000 :
            space_contures = approx
            cv2.drawContours(image, [approx], -1, (255, 255, 0), 10)

            x, y, w, h = cv2.boundingRect(space_contures)
            x_mid = x + w / 2
            y_mid = y + w / 2
            cordian_center = learning_utils.Coordinate(x_mid,y_mid)
            space_area = area


    textOutput = "Ilosc znalezionych elementow:" + str(count_of_counturs)
    coords = (200, 50)
    color = (1, 1, 1)
    font = cv2.FONT_HERSHEY_DUPLEX

    cv2.putText(image, textOutput, coords, font, 2, color, 1)

    cv2.namedWindow('Contours', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Contours', 1200, 800)

    image_with_contours = image.copy()
    cv2.imwrite("static/img/img1_con.jpg",image_with_contours)

    if(space_area > 0):
        percent_full = round(((contours_area/space_area)*100),2)
    else:
        percent_full = 0

    return [img_coordinate, percent_full]




