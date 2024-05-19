class Vehicle :
    def __init__(self,owner,numberOfWheels,type):
        self.numberOfWheels=numberOfWheels
        self.type=type
        self.owner=owner


class Car(Vehicle):
    def __init__(self,brand,model,owner):
        super().__init__(type='CAR',numberOfWheels=4,owner=owner)
        self.brand = brand
        self.model = model 
    
    def print(self):
        print(f"vehicle model : {self.model}")
        print(f"vehicle type : {self.type}")
        print(f"vehicle owner : {self.owner}")
        print(f"number of wheels : {self.numberOfWheels}")
        print(f"vehicle brand : {self.brand}")

        
