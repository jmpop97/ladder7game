import random


class BaseCharacter:
    def __init__(self):
        self.name = 'defaultCharacterName'
        self.max_hp = 100
        self.hp = 100
        self.max_mp = 50
        self.mp = 50
        self._str = 20
        self.arm = 5
        self._int = 15
        self.spd = 5

    def status(self):
        print(f"{self.name}: Hp {self.hp}/{self.max_hp} MP {self.max_mp}/{self.max_mp}")

    def show_detail(self):
        print(f'{self.name} 직업:{type(self).__name__}  Hp {self.hp}/{self.max_hp} MP {self.max_mp}/{self.max_mp}')
        print(f'힘 {self._str} 방어력 {self.arm} 지능 {self._int} 속도 {self.spd}')

    def attack(self, other):
        damage = random.randint(self._str, self._str)
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")

# 베이스 캐릭터


class Warrior(BaseCharacter):
    def __init__(self):
        super().__init__()
        self.max_hp += 20
        self.hp += 20
        self._str += 15
        self.arm += 5
        self.spd += - 2

    def power_attack(self, other):
        damage = random.randint(self._str*0.8, self._str*1.2)
        other.hp = max(other.hp - damage, 0)
        self.mp = max(self.mp - 5, 0)
        print(f"{self.name}의 파워 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")


class Mage(BaseCharacter):
    def __init__(self):
        super().__init__()
        self.max_hp += 10
        self.hp += 10
        self._str += -5
        self.arm += -1
        self.spd += 2
        self.max_mp += 40
        self.mp += 40
        self._int += 25

    def fire_magic(self, other):
        damage = random.randint(self._int*0.8, self._int*1.2)
        other.hp = max(other.hp - damage, 0)
        self.mp = max(self.mp - 5, 0)
        print(f"{self.name}의 화염 마법! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")

    def wind_magic(self, other):
        damage1 = random.randint(
            int((self._int - other.arm)*0.3), int((self._int - other.arm)*0.7))
        damage2 = random.randint(
            int((self._int - other.arm)*0.3), int((self._int - other.arm)*0.7))
        damage3 = random.randint(
            int((self._int - other.arm)*0.3), int((self._int - other.arm)*0.7))

        damage = damage1 + damage2 + damage3
        other.hp = max(other.hp - damage, 0)
        self.mp = max(self.mp - 5, 0)
        print(
            f"{self.name}의 바람 마법! {other.name}에게 {damage1}, {damage2}, {damage3}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")


class Thief(BaseCharacter):
    def __init__(self):
        super().__init__()
        self._str += 5
        self.arm += 2
        self.spd += 12
        self.hide = False
        if self.hide == True:
            self.spd == 99
            print(f"{self.name}은 은신했습니다. 무조건 선공함")

    def attack(self, other):
        super().attack()

    def hide(self):
        self.hide = True

    def hide_attack(self, other):
        damage = random.randint(
            int((self._str + self.spd)*1.6), int((self._str + self.spd)*2.4))
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 은신공격! {other.name}에게 {damage}의 치명적인 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")
        self.hide = False


class Archer(BaseCharacter):
    def __init__(self):
        super().__init__()
        self.max_hp += 8
        self.hp += 8
        self._str += 7
        self.arm += 2
        self.spd += 7

    def silver_arrow_shot(self, other):
        damage = random.randint(int(self._str+self.spd)
                                * 1.8, int(self._str+self.spd)*2.2)
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 은화살공격! {other.name}은 {damage}의 치명적인 트루데미지를 입었습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")


jobs = ['Archer', 'Warrior', 'Mage', 'Thief']


# for i in [0, 1, 2, 3]:
# if jobs[i] == 'Archer':
#        jobs_data[i] = Archer('archer', 100, 100, 20, 5, 10, 5)
#    elif jobs[i] == 'Warrior':
#        jobs_data[i] = Warrior('Warrior', 100, 100, 20, 5, 10, 5)
#    elif jobs[i] == 'Mage':
#     jobs_data[i] = Mage('Mage', 100, 100, 20, 5, 10, 5)
# elif jobs[i] == 'Thief':
#     jobs_data[i] = Thief('Thief', 100, 100, 20, 5, 10, 5)

job_dic = {"Archer": Archer,
           "Warrior": Warrior,
           "Mage": Mage,
           "Thief": Thief}

# job_dic["Archer"]().show_detail()
