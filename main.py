print('Welcome to GC Bikes & Trucks!')

class Vehicle:

    def __init__(self, make, miles, price):
        self.make = make
        self.miles = miles
        self.price = price
        self.engine_on = False

    def start_engine(self):
        print('Starting engine...')
        self.engine_on = True

    def make_noise(self):
        print('Beep beep!')


class Truck(Vehicle):
    trucks = []

    def __init__(self, make, miles, price):
        Vehicle.__init__(self, make, miles, price)
        self.cargo = False
        Truck.trucks.append(self)

    def load_cargo(self):
        print('Loading the truck bed...')
        self.cargo = True

    def __str__(self):
        return f'{self.make}: with {self.miles} miles costs ${self.price}'



class Motorcycle(Vehicle):
    bikes = []

    def __init__(self, make, miles, price, top_speed):
        Vehicle.__init__(self, make, miles, price)
        self.top_speed = top_speed
        Motorcycle.bikes.append(self)

    def how_fast(self):
        print(f'This bike has a top speed of {self.top_speed}.')

    def make_noise(self):
        print('Vroom vroom!')

    def __str__(self):
        return f'{self.make}: with {self.miles} miles and a top speed of {self.top_speed} mph costs ${self.price}'


toyota = Truck('Toyota', 175000, 7000)
ford = Truck('Ford', 9000, 35000)
chevy = Truck('Chevy', 800, 45000)


harley = Motorcycle('Harley', 0, 50000, 300)
ducati = Motorcycle('Ducati', 1000, 55000, 250)
honda = Motorcycle('Honda', 20000, 12000, 240)


def show_vehicles(vehicles_list):
    for i, vehicle in enumerate(vehicles_list, 1):
        print(f"{i}. {vehicle}")


vehicles_to_compare = []

cont_flag = True

while cont_flag:
    selection = input('Would you like to view bikes or trucks? (b or t) \n> ')

    while True:
        if selection == 'b':
            show_vehicles(Motorcycle.bikes)
            choice_list = Motorcycle.bikes
            break
        elif selection == 't':
            show_vehicles(Truck.trucks)
            choice_list = Truck.trucks
            break
        else:
            print('That entry is invalid, please try again.')

    compare_now = input('Would you like to compare one of these vehicles today? (y or n) \n> ')

    while True:
        if compare_now == 'y':
            pick_vehicle = int(input('Which vehicle would you like to compare? (please list number) \n> '))

            if 0 < pick_vehicle <= len(choice_list):
                chosen_vehicle = choice_list[pick_vehicle - 1]
                vehicles_to_compare.append(chosen_vehicle)
                print(f'{chosen_vehicle.make} added!')
                break

        elif compare_now == 'n':
            break

        else:
            print('That entry is invalid, please try again.')

    compare_all = input('Would you like to compare your vehicles now? (y or n) \n> ')

    while True:
        if compare_all == 'n':
            break

        elif compare_all == 'y':
            print('Here are your vehicles to compare:')
            for vehicle in vehicles_to_compare:
                print(f'- {chosen_vehicle.make}: with {chosen_vehicle.miles} miles costs ${chosen_vehicle.price}')
                chosen_vehicle.make_noise

            print('Thank you and have a nice day!')
            break
            cont_flag = False

        else:
            print('That entry is invalid, please try again.')
