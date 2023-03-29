class BaseCharacter:
    def __init__(self, name, hp, mp, str, arm, int, spd):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.str = str
        self.arm = arm
        self.int = int
        self.spd = spd


class Portion:
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability
        self.amount = 0


class HpPortion(Portion):
    def get(self):
        print(f"{self.name}을 획득했습니다.")
        self.amount += 1

    def use(self, owner):
        if self.amount < 1:
            print(f"{self.name}이 부족합니다.")
            return False
        else:
            print(f"{self.name}을 사용 하셨습니다. {owner.name}의 HP를 {self.ability}만큼 회복합니다.")
            owner.hp += self.ability
            self.amount -= 1


class MpPortion(Portion):
    def get(self):
        print(f"{self.name}을 획득했습니다.")
        self.amount += 1

    def use(self, owner):
        if self.amount < 1:
            print(f"{self.name}이 부족합니다.")
            return False
        else:
            print(f"{self.name}을 사용 하셨습니다. {owner.name}의 MP를 {self.ability}만큼 회복합니다.")
            owner.mp += self.ability
            self.amount -= 1


class Item:
    # 아이템 이름과 능력을 이닛으로 받음
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability


class StrItem(Item):
    def get(self, owner):
        print(f"{owner.name}에게 {self.name}을(를) 장착했습니다.")
        owner.str += self.ability


player = BaseCharacter("이름", 100, 50, 10, 10, 10, 10)
red_portion = HpPortion("빨간물약", 10)
white_portion = HpPortion("하얀물약", 50)
sword = StrItem("롱소드", 10)

print(player.hp)
print(red_portion.amount)
a = red_portion

a.get()
white_portion.get()
print(player.hp)
print(a.amount)

a.use(player)
print(player.hp)
print(a.amount)

a.use(player)
print(player.hp)
print(a.amount)

print(player.str)

sword.get(player)
print(player.str)
