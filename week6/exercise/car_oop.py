
class Car:
    def __init__(self, license, brand, color):
        self.license = license
        self.brand = brand
        self.color = color
        self.report = []
        self.current_payment = 0

    def __str__(self):
        return f"{self.license} - {self.color} {self.brand}"

    def __lt__(self, rhs):
        return self.license < rhs.license

    def add_report(self, new_report):
        self.report.append(new_report)
        self.current_payment += new_report[2]
    
    def total_payment(self):
        return self.current_payment

    def max_payment(self):
        self.report.sort(key = lambda report: report[2])
        return self.report[len(self.report)-1] if self.report else []

car_1 = Car('AA1234', 'Honda', 'White')
car_2 = Car('AA1235', 'Toyota', 'Black')

car_1.add_report(('25 May 2017', 'change tires', 1500))
car_1.add_report(('26 May 2017', 'change tires', 3000))
car_1.add_report(('30 May 2017', 'change choke', 2500))
car_1.add_report(('1 June 2017', 'change front hood', 5500))

print(car_1)
print(f"report {car_1.report}")
print(f"max payment {car_1.max_payment()}")
print(f"total payment {car_1.total_payment()}")

print(car_2 > car_1)