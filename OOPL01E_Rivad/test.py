class Car:
    def __init__(self, brand, model, year, engine):
        self.brand = brand
        self.model = model
        self.year = year
        self.engine = engine

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Engine: {self.engine}")

#initialize object for class Car
car1 = Car("Toyota", "Fortuner", 2025, "Hybrid")
car2 = Car("Lamborgini", "Gallardo", 2023, "V10")
car3 = Car("Ferrari", "Roma Spider", 2022, "V12")
car4 = Car("Chevrolet", "Camero", 2019, "V8")

#call the method display_info()
car1.display_info()
car2.display_info()
car3.display_info()
car4.display_info()