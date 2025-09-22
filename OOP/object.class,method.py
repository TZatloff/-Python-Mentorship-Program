class Build:
    __year = None
    __city = None

    def __init__(self, year, city):
        self.year = year
        self.city = city

    def get_info(self):
        print(f"Year: {self.year}, City: {self.city}", sep='')


class School(Build):
    def __init__(self, year, city, students_qty=500):
        super().__init__(year, city)
        self.students_qty = students_qty

    def get_info(self):
        super().get_info()
        print("Students quantity:", self.students_qty)


class House(Build):
    pass


class Shop(Build):
    pass


school = School(1990, "Seattle", 800)
school.get_info()

house = House(2020, "New York")
house.get_info()

shop = Shop(2010, "Los Angeles")


