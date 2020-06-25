class Animal:
    status_hungry = 'голодное'
    status_feeding = 'принимает пищу'
    status_enough = 'сытое'
    state = Noneanimal_type = None
    weight = 0
    animal_type = None
    voice = None

    def get_name(self):
        pass

    def get_weight(self):
        pass

    def get_voice(self):
        pass


class Cattle(Animal):
    def __init__(self, animal_name, animal_weight):
        self.name = animal_name
        self.weight = animal_weight
        self.data = {self.name: self.weight}

    def get_name(self):
        return self.name

    def get_weight(self):
        return self.weight

    def get_voice(self):
        print(f'{self.animal_type.capitalize()} говорит {self.voice}')
        return self.voice

    def get_animal_type(self):
        return self.animal_type

    def get_food(self):
        self.animal_status = self.status_hungry
        print(f'Животное {self.animal_type} "{self.name}" {self.status_hungry}')
        self.animal_status = self.status_feeding
        print(f'Животное {self.animal_type} "{self.name}" {self.status_feeding}')
        self.animal_status = self.status_enough
        print(f'Животное {self.animal_type} "{self.name}" {self.status_enough}')
        return


class Small_cattle(Animal):
    def __init__(self, animal_name, animal_weight):
        self.name = animal_name
        self.weight = animal_weight
        self.data = {self.name: self.weight}

    def get_name(self):
        return self.name

    def get_weight(self):
        return self.weight

    def get_voice(self):
        print(f'{self.animal_type.capitalize()} говорит {self.voice}')
        return self.voice

    def get_animal_type(self):
        return self.animal_type

    def get_food(self):
        self.animal_status = self.status_hungry
        print(f'Животное {self.animal_type} "{self.name}" {self.status_hungry}')
        self.animal_status = self.status_feeding
        print(f'Животное {self.animal_type} "{self.name}" {self.status_feeding}')
        self.animal_status = self.status_enough
        print(f'Животное {self.animal_type} "{self.name}" {self.status_enough}')
        return


class Poultry(Animal):
    def __init__(self, animal_name, animal_weight):
        self.name = animal_name
        self.weight = animal_weight
        self.data = {self.name: self.weight}

    def get_name(self):
        return self.name

    def get_weight(self):
        return self.weight

    def get_voice(self):
        print(f'{self.animal_type.capitalize()} говорит {self.voice}')
        return self.voice

    def get_animal_type(self):
        return self.animal_type

    def get_food(self):
        self.animal_status = self.status_hungry
        print(f'Животное {self.animal_type} "{self.name}" {self.status_hungry}')
        self.animal_status = self.status_feeding
        print(f'Животное {self.animal_type} "{self.name}" {self.status_feeding}')
        self.animal_status = self.status_enough
        print(f'Животное {self.animal_type} "{self.name}" {self.status_enough}')
        return

    def get_eggs(self):
        self.state = 'Сбор яиц'
        return self.state


class Goose(Poultry):
    animal_type = 'гусь'
    voice = 'Га-га-га'


class Cow(Cattle):
    animal_type = 'корова'
    voice = 'Му-у-у'

    def get_milk(self):
        self.state = 'Сбор молока'
        return self.state


class Sheep(Small_cattle):
    animal_type = 'овца'
    voice = 'Бе-е-е'

    def to_shear(self):
        self.state = "Стрижка"
        return self.state


class Chicken(Poultry):
    animal_type = 'курица'
    voice = 'Ко-ко-ко'


class Goat(Small_cattle):
    animal_type = 'коза'
    voice = 'Ме-е-е'

    def get_milk(self):
        self.state = 'Сбор козьего молока'
        return self.state


class Duck(Poultry):
    animal_type = 'утка'
    voice = 'Кря-кря'

all_animal = []

grey_goose = Goose("grey", 4)
white_goose = Goose("white", 5)
gooses = [grey_goose, white_goose]
print('-------------------------')
print('Взаимодействие с гусями')
print('-------------------------')
for goose in gooses:
    goose.get_voice()
    goose.get_food()
    print(goose.get_eggs())
    all_animal.append(goose.data)
    print()

cow = Cow("Манька", 100)
print('-------------------------')
print('Взаимодействие с коровой')
print('-------------------------')
cow.get_voice()
cow.get_food()
print(cow.get_milk())
all_animal.append(cow.data)
print()

sheep1 = Sheep("Барашек", 10)
sheep2 = Sheep("Кудрявый", 12)
sheeps = [sheep1, sheep2]
print('-------------------------')
print('Взаимодействие с овцами')
print('-------------------------')
for sheep in sheeps:
    sheep.get_voice()
    sheep.get_food()
    print(sheep.to_shear())
    all_animal.append(sheep.data)
    print()

chicken1 = Chicken("Ко-Ко", 1)
chicken2 = Chicken("Кукареку", 2)
chickens = [chicken1, chicken2]
print('-------------------------')
print('Взаимодействие с курами')
print('-------------------------')
for chicken in chickens:
    chicken.get_voice()
    chicken.get_food()
    print(chicken.get_eggs())
    all_animal.append(chicken.data)
    print()

goat1 = Goat("Рога", 15)
goat2 = Goat("Копыта", 17)
goats = [goat1, goat2]
print('-------------------------')
print('Взаимодействие с козами')
print('-------------------------')
for goat in goats:
    goat.get_voice()
    goat.get_food()
    print(goat.get_milk())
    all_animal.append(goat.data)
    print()

duck = Duck("Кряква", 8)
print('-------------------------')
print('Взаимодействие с уткой')
print('-------------------------')
duck.get_voice()
duck.get_food()
print(duck.get_eggs())
all_animal.append(duck.data)
print()
# print(all_animal)

# общий вес
total_weight = 0
max_weight = 0
max_animal = 0
for animal in all_animal:
    for name, weight in animal.items():
        total_weight += weight
        if max_weight < weight:
            max_weight = weight
            max_animal = name
# print(total_weight)
print(f'Общий вес животных {total_weight} кг.')
print(f'Самое тяжелое животное это {max_animal}')
