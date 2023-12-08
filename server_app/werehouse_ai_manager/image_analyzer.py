import cv2
import learning_utils
def analyzer(path):

    if(path == ''):
        image = cv2.imread("static/img/img2.jpg")
    else:
        image = cv2.imread(path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
    #_, threshold = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
    #edges = cv2.Canny(gray_image, 50, 150)
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    contours_detected = []
    count_of_counturs = 0
    img_coordinate = []

    for contour in contours:
        area = cv2.contourArea(contour)
        epsilon = 0.05 * cv2.arcLength(contour,True)
        approx = cv2.approxPolyDP(contour,epsilon,True)

        if  len(approx) > 3 and len(approx) < 5 and area > 6000:
            contours_detected.append(approx)
            cv2.drawContours(image, [approx], 0, (0, 255, 0), 10)
            count_of_counturs += 1

            x,y,w,h = cv2.boundingRect(approx)
            x_mid = x+w/2
            y_mid = y + w/2
            cordin = learning_utils.Coordinate(x_mid,y_mid)
            img_coordinate.append(cordin)

    #cv2.drawContours(image, contours, 0, (255, 255, 0), 20)
    textOutput = "Ilosc znalezionych elementow:" + str(count_of_counturs)
    coords = (200, 50)
    color = (1, 1, 1)
    font = cv2.FONT_HERSHEY_DUPLEX

    cv2.putText(image, textOutput, coords, font, 2, color, 1)

    cv2.namedWindow('Contours', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Contours', 1200, 800)

    image_with_contours = image.copy()
    cv2.imwrite("static/img/img1_con.jpg",image_with_contours)


    return img_coordinate




