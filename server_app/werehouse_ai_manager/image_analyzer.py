import cv2

def analyzer():
    image = cv2.imread("static/img/img1.jpg")
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

   
    count_of_counturs = 0
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 400:
            count_of_counturs += 1
            cv2.drawContours(image,contour, 0 ,(0,255,0),10)

    # Zliczenie konturów
    number_of_elements = len(contours)
    print("Ilość znalezionych elementów:", count_of_counturs)

    # Wyświetlenie obrazu z zaznaczonymi konturami (opcjonalne)
    cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

    textOutput = "Ilosc znalezionych elementow:" + str(count_of_counturs)
    coords = (200, 50)
    color = (1, 1, 1)
    font = cv2.FONT_HERSHEY_DUPLEX

    cv2.putText(image, textOutput, coords, font, 2, color, 1)

    cv2.namedWindow('Contours', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Contours', 1200, 800)
    #cv2.imshow('Contours', image)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    image_with_contours = image.copy()
    cv2.imwrite("static/img/img1_con.jpg",image_with_contours)

    return count_of_counturs