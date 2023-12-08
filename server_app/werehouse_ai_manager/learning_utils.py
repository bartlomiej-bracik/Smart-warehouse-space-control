

class Coordinate:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Feature:
    avr_coordinateX = 0
    avr_coordinateY = 0
    avr_radius = 0
    avr_number_of_neighbors = 0
    def __init__(self,img_coordinate ,count_of_counturs,percent_full):
        self.percent_full = percent_full
        self.count_of_counturs = count_of_counturs
        self.img_coordinate = img_coordinate
        self.avr_coordinateX = self.calculate_avrX()
        self.avr_coordinateY = self.calculate_avrY()
        self.avr_radius = 0
        self.avr_number_of_neighbors = 0

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
        for n in numbers:
            c1 = 1

    def calculate_all(self):
        print("calculated")



    def getFeature(self):
        return [self.count_of_counturs, self.percent_full,self.avr_coordinateX,
                self.avr_coordinateY,self.avr_radius,self.avr_number_of_neighbors]




    def print_data(self):
        data = self.img_coordinate
        for d in data:
            print("Dane",d.x)

