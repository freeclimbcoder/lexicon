class Vehicle():
    def __init__(self, make: str, model: str, year: int, is_running = False) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.is_running = is_running

    def __str__(self) -> str:
        return f'Make = {self.make}, model = {self.model}, year = {self.year}, is running = {self.is_running}'

    def start(self):
        print(f'{self.make} {self.model} is running')
        self.is_running = True

    def stop(self):
        print(f'{self.make} {self.model} is stopped')
        self.is_running = False

class Car(Vehicle):
    def __init__(self, make: str, model: str, year: int, tank: int, num_doors: int) -> None:
        super().__init__(make, model, year, is_running = False)
        self.tank = tank
        self.num_doors = num_doors


    def __str__(self) -> str:
        return f'{super().__str__()}, has {self.num_doors} doors and {self.tank} liters of fuel in tank'
    
    def honk(self):
        print('Honk-honk!')
    
class Cycle(Vehicle):
    def __init__(self, make: str, model: str, year: int, num_gears: int, is_running=False) -> None:
        super().__init__(make, model, year, is_running)
        self.num_gears = num_gears

    def __str__(self) -> str:
        return f'{super().__str__()}, has {self.num_gears} gears'
    
    def shout(self):
        print('Jävla fotgängare!')

    def ring_the_bell(self):
        print('Ding-ding')


class Motorcycle(Vehicle):
    def __init__(self, make: str, model: str, year: int, tank: int, is_running=False) -> None:
        super().__init__(make, model, year, is_running)
        self.tank = tank

    def __str__(self) -> str:
        return f'{super().__str__()}, has {self.tank} liters of fuel in tank'
    
    def crach(self):
        print('It was a tough  day')
                
###########################################################################################################

cycle = Cycle('Marin', 'SDX', 2022, 11)
print(cycle)
cycle.start()
cycle.shout()
cycle.stop()

car = Car('WV', 'California', 2024, 90, 4)
print(car)

moto = Motorcycle('Honda', 'Africa twin', 2024, 'is this normal?') #<<<=======
print(moto)
moto.crach()