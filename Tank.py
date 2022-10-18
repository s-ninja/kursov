from random import *
class Tank:
    def __init__(self, model , armor, min_damage, max_damage, health,
                 enemy_model, enemy_armor, enemy_min_damage, enemy_max_damage, enemy_health):
        self.model = model
        self.armor = armor
        self.damage = randrange(min_damage, max_damage)
        self.health = health
        self.enemy = enemy_model
        self.enemy_health = health
        self.enemy_model = enemy_model
        self.enemy_armor = enemy_armor
        self.enemy_damage = randrange(enemy_min_damage, enemy_max_damage)
        self.enemy_health = enemy_health
        self.enemy_enemy = enemy_model
        self.enemy_health = health


    def print_info(self):
        print(f'{self.model} имеет лобовую броню {self.armor}мм. при {self.health} '
                f'ед. здоровья и урон в {self.damage} единиц')


    def healt_down(self,num_shot):
        if num_shot % 2 == 0:
            self.enemy_health = self.enemy_health - self.damage/self.enemy_armor
            num_shot += 1
        else:
            self.health = self.health - self.enemy_damage/self.armor
            print(f'{self.model}: Командир, по экипажу {self.model} попали,'
                  f' у нас осталось {self.health} очков здовроья')
            num_shot += 1


    def shot(self, num_shot):
        while self.health > 0 and self.enemy_health > 0:
            self.healt_down(num_shot)

            if self.enemy_health <= 0:

                print(f'Экипаж танка {self.enemy} уничтожен')

            else:
                print(f'{self.model}: Точно в цель, у противника осталось {self.enemy} осталось {self.enemy_health} единиц здоровья. ')


m = input('Введите модель танка ')
a = int(input('Ведите очки брони '))
min_d = int(input('Введите минимальный урон вашего танка '))
max_d = int(input('Введите максимальный урон вашего танка '))
h = int(input('Введите очки здоровья '))
num_shot = 0
tank = Tank(m, a, min_d, max_d, h, 'Тигр', 100, 1, 50, 100)
tank.print_info()
tank.shot(num_shot)
