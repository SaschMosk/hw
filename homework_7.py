class Animals:
  habitat = "land"
  Lungs = True
  age = 0 #лет
  babys = 0 #количество потомков
  size = 0 #условный размер животного, в дециметрах
  weight = 0 #вес животного в кг
  def init_size(self):
    s = input('Введите размер животного, в дм:')
    self.size += int(s)
    return self.size
  def init_weight(self):
    w = input('Введите вес животного, в кг:')
    self.weight += int(w)
  def eat(self):
    float(self.age)
    self.age += 0.05
    self.weight += 0.2
    print('Теперь возраст: ', self.age)
  def sleep(self):
    float(self.age)
    self.age += 0.07
    self.size += 0.1
    print('Теперь возраст:', self.age)
class Birds (Animals):
  Legs = 2
  Wings = True
  Beak = True
  Eggs = 0
  def lay_an_egg(self):
    import random
    self.Eggs += random.randint(1, 7)
  def hatch_an_egg(self, Eggs):
    if self.Eggs != 0:
      self.babys += (Eggs - 2)
    else:
      print('Ещё не готова!')
class Mammals (Animals):
  Legs = 4
  Wings = False
  Beak = False
  def reproduction(self):
    self.babys += 1
class Cow(Mammals):
  color = 'black&white'
  def hear(self):
    return "Muuuu"
  def give_milk(self):
    print("Получено random.int(20, 40) литров молока")
class Goat(Mammals):
  color = 'gray'
  def hear_goat(self):
    return 'Meeee'
class Sheep(Mammals):
  color = 'white'
  def hear(self):
    return 'Beeee'
class Pig(Mammals):
  color = 'pink'
  def hear(self):
    return 'Chryu'
class Duck(Birds):
  color = 'green'
  def hear(self):
    return 'Krya'
  def swim_in_pond(self):
    print("Утка плавает в пруду...")
class Сhicken(Birds):
  color = 'brown'
  def hear(self):
    return'Kud-Kudach'
class Goose(Birds):
  color = 'gray&blu'
  def hear(self):
    return 'Ga-ga-ga'
