class area:
    def __init__(self,radius):
        self.radius_circle=radius
        self.area_of_circle = 3.14*radius*radius
        
    def calculate_area(self):
        print("area of circle is : ",self.area_of_circle)
    
answer_obj = area(radius = 4)
answer_obj.calculate_area()

