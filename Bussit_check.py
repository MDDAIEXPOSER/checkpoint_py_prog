class Busssit:
    def __init__ (self, speed, capacity, maxSpeed, passengers_names, hasEmptySeats, passengers)
    self.speed = speed
    self.capacity = capacity
    self.passengers = passengers
    self.maxSpeed = maxSpeed
    self.passengers = passengers

    def set_que_passengers(self, passengers, capacity):
        print('Взять попутчиков?')
        print('Да/нет')
        choice = str(input())
        if choice.lower() == 'да':
            print('Сколько попутчиков?')
            que_new = int(input())
            if  self.capacity - self.passengers == 0:
                print('Мест нет')
                self.hasEmptySeats = False
            else:
                self.passengers += que_new
                self.hasEmptySeats = True
        else:
            print('Едем дальше...')

    def gaz_v_pol(self, speed):
        if self.speed == self.maxSpeed:
            print('Maximum')
        else:
            print('Газ в пол до?:')
            new_speed = int(input())
            if self.speed + new_speed <= self.maxSpeed:
                self.speed += new_speed
            else:
                print('Nope')

    def gaz_v_wall(self, speed):
        print('На сколько сбавить газ?')
        tormoz = int(input())
        self.speed -= tormoz
        if self.speed < 0:
            print('Never stand')
            self.speed += 1

    def get_out_que_passengers(self, passengers, hasEmptySeats):
        print('Сколько пассажиров выкинуть?')
        gets_passengers = int(input())
        if gets_passengers > self.passengers:
            print('Nope')
            self.hasEmptySeats = True
        else:
            self.passengers -= gets_passengers

    def find_passenger(self, passengers_names):
        places_for_persons = [i for i in range(1, 3)]
        names_for_persons = [input() for _ in range(1, 3)]
        self.passengers_names = dict(zip(places_for_persons, names_for_persons))
        print('Кого высадим?')
        name = input()
        get_names = self.passengers_names.get(name)
        if name in self.passengers_names:
            self.passengers_names.pop(name)
            print(name,'выкинули из окна')
        else:
            print('Такого пассажира нет')

    def plus_passenger(self, passengers_names):
        places_for_persons = [i for i in range(1, 3)]
        names_for_persons = [input() for _ in range(1, 3)]
        self.passengers_names = dict(zip(places_for_persons, names_for_persons))
        print('Кого посадим?')
        new_name = input()
        if new_name in self.passengers_names:
            print('Он уже в автобусе')
        else:
            self.passengers_names['4'] = new_name

    def main():
        bus = Busssit(12, 300, 1800, 230)
        bus.find_passenger()
        bus.plus_passenger()
        bus.get_out_que_passengers()
        bus.gaz_v_pol()
        bus.gaz_v_wall()
        bus.set_que_passengers()
        print(bus.speed)

main()
