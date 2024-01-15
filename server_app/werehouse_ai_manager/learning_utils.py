import math

class Coordinate:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Feature:
    avr_coordinateX = 0
    avr_coordinateY = 0
    avr_radius = 0
    avr_number_of_neighbors = 0
    count_of_counturs = 0
    def __init__(self,img_coordinate ,center_cordian,space_areaa):
        self.img_coordinate = img_coordinate

        self.percent_full = percent_full
        self.count_of_counturs = self.calculate_count_of_contures()
        self.avr_coordinateX = self.calculate_avrX()
        self.avr_coordinateY = self.calculate_avrY()
        self.avr_radius = self.calculate_radius()
        self.avr_number_of_neighbors = self.calculate_avr_number_of_neighbors()

    def calculate_count_of_contures(self):
        numbers = self.img_coordinate
        return len(numbers)
    def calculate_avrX(self):
        numbers = self.img_coordinate
        sum = 0
        for n in numbers:
            sum = sum + n.x
        avr = sum/len(numbers)
        return avr
    def calculate_avrY(self):
        numbers = self.img_coordinate
        sum = 0
        for n in numbers:
            sum = sum + n.y
        avr = sum/len(numbers)
        return avr
    def calculate_radius(self):
        numbers = self.img_coordinate
        c = []
        center = [0,0]
        sum =0
        avr = 0
        for n in numbers:
            c1 = math.sqrt((center[0] -n.x)*(center[0] -n.x) + (center[1] -n.y)*(center[1] -n.y))
            sum = sum +c1
        avr = sum/len(numbers)
        return avr

    def calculate_avr_number_of_neighbors(self):
        numbers = self.img_coordinate
        neighbors_distance = 2000
        positionXY  = 0
        positionXY2 = 0
        counter = 0
        for n in numbers:
            positionXY = math.sqrt(pow(n.x,2)+pow(n.y,2))
            for n1 in numbers:
                positionXY = math.sqrt(pow(n1.x, 2) + pow(n1.y, 2))
                if abs(positionXY2-positionXY) <= neighbors_distance:
                    counter = counter+1
        #counter = counter - len(numbers)
        avr = counter/len(numbers)
        return avr


    def calculate_all(self):
        print("calculated")



    def getFeature(self):
        return [self.count_of_counturs, self.percent_full,self.avr_coordinateX,
                self.avr_coordinateY,self.avr_radius,self.avr_number_of_neighbors]




    def print_data(self):
        data = self.img_coordinate
        for d in data:
            print("Dane",d.x)

