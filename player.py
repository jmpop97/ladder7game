import random
from monster import *
from item import *


class BaseCharacter:
    def __init__(self, name):
        self.name = name
        self.max_hp = 100
        self.hp = self.max_hp
        self.max_mp = 50
        self.mp = self.max_mp
        self._str = 20
        self.arm = 5
        self._int = 15
        self.spd = 5

    def status(self):
        print(f"{self.name}: Hp {self.hp}/{self.max_hp} MP {self.mp}/{self.max_mp}")

    def show_detail(self):
        print(f'{self.name} 직업:{type(self).__name__}  Hp {self.hp}/{self.max_hp} MP {self.mp}/{self.max_mp}')
        print(f'힘 {self._str} 방어력 {self.arm} 지능 {self._int} 속도 {self.spd}')

    def attack(self, other):
        damage = random.randint(int(self._str*0.3), int(self._str*0.5))
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 공격! {other.type}에게 {damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.type}이(가) 쓰러졌습니다.")


# 베이스 캐릭터


class Warrior(BaseCharacter):
    def __init__(self, name):
        super().__init__(name)
        self.max_hp += 20
        self.hp += 20
        self._str += 15
        self.arm += 5
        self.spd += - 2

    def power_attack(self, other):
        damage = random.randint(self._str*0.8, self._str*1.2)
        other.hp = max(other.hp - damage, 0)
        self.mp = max(self.mp - 5, 0)
        print(f"{self.name}의 파워 공격! {other.type}에게 {damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.type}이(가) 쓰러졌습니다.")


class Mage(BaseCharacter):
    def __init__(self, name):
        super().__init__(name)
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
        print(f"{self.name}의 화염 마법! {other.type}에게 {damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.type}이(가) 쓰러졌습니다.")

    def wind_magic(self, other):
        damage1 = random.randint(
            int((self._int)*0.3), int((self._int)*0.7))
        damage2 = random.randint(
            int((self._int)*0.3), int((self._int)*0.7))
        damage3 = random.randint(
            int((self._int)*0.3), int((self._int)*0.7))

        damage = damage1 + damage2 + damage3
        other.hp = max(other.hp - damage, 0)
        self.mp = max(self.mp - 5, 0)
        print(
            f"{self.name}의 바람 마법! {other.type}에게 {damage1}, {damage2}, {damage3}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.type}이(가) 쓰러졌습니다.")


class Thief(BaseCharacter):
    def __init__(self, name):
        super().__init__(name)
        self._str += 5
        self.arm += 2
        self.spd += 12
        self.hide = False

    def attack(self, other):
        if self.hide == True:
            print(f'{self.name}은 은신상태라서 공격을 할 수 없음')
        else:
            super().attack(other)

    def hiding(self):
        self.hide = True
        if self.hide == True:
            self.spd += 99
            self.arm += 99

        print(f"{self.name}은 은신했습니다. 무조건 선공함")

    def hide_attack(self, other):
        if self.hide == True:
            damage = random.randint(
                int((self._str + self.spd)*1.6), int((self._str + self.spd)*2.4))
            other.hp = max(other.hp - damage, 0)
            print(f"{self.name}의 은신공격! {other.type}에게 {damage}의 치명적인 데미지를 입혔습니다.")
            if other.hp == 0:
                print(f"{other.type}이(가) 쓰러졌습니다.")
            self.spd -= 99
            self.arm -= 99
            self.hide = False
        elif self.hide == False:
            print("은신 상태가 아니라서 쓸 수가 없고 당신의 행동은 무효가됨")


class Archer(BaseCharacter):
    def __init__(self, name):
        super().__init__(name)
        self.max_hp += 8
        self.hp += 8
        self._str += 7
        self.arm += 2
        self.spd += 7

    def silver_arrow_shot(self, other):
        damage = random.randint(
            int((self._str+self.spd)*1.8), int((self._str+self.spd)*2.2))
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 은화살공격! {other.type}은 {damage}의 치명적인 트루데미지를 입었습니다.")
        if other.hp == 0:
            print(f"{other.type}이(가) 쓰러졌습니다.")

# 실험용


# 실험용 몬스터


def skills_that_have(player):
    skills = []
    if type(player) == Archer:
        skills.append("은화살")
    elif type(player) == Warrior:
        skills.append("파워공격")
    elif type(player) == Mage:
        skills.append("화염마법")
        skills.append("바람마법")
    elif type(player) == Thief:
        skills.append("은신")
        skills.append("은신공격")
    else:
        print("혹시 전직을 안했나?")
    return skills


jobs = ['Archer', 'Warrior', 'Mage', 'Thief']
job_dic = {"Archer": Archer,
           "Warrior": Warrior,
           "Mage": Mage,
           "Thief": Thief}


def skill_use(chara, skill, target_mon):
    if skill == '파워공격':
        try:
            chara.power_attack(target_mon)
        except:
            print(f'{chara.name}는 그런 스킬을 가지고 있지 않는데요?')
    elif skill == "포션먹기":
        print(target_mon)
        if target_mon == "빨간물약":
            red_portion.use(chara)
        if target_mon == "하얀물약":
            white_portion.use(chara)
        if target_mon == "파란물약":
            blue_portion.use(chara)

    elif skill == '공격':
        chara.attack(target_mon)
    elif skill == '은화살':
        try:
            chara.silver_arrow_shot(target_mon)
        except:
            print(f'{chara.name}는 그런 스킬을 가지고 있지 않는데요?')
    elif skill == '화염마법':
        try:
            chara.fire_magic(target_mon)
        except:
            print(f'{chara.name}는 그런 스킬을 가지고 있지 않는데요?')
    elif skill == '바람마법':
        chara.wind_magic(target_mon)
        # try:
        #     chara.wind_magic(target_mon)
        # except:
        #     print(f'{chara.name}는 그런 스킬을 가지고 있지 않는데요?')
    elif skill == '은신':
        chara.hiding()
        # try:
        #     chara.hiding()
        # except:
        #     print(f'{chara.name}는 그런 스킬을 가지고 있지 않는데요?')
    elif skill == '은신공격':
        try:
            chara.hide_attack(target_mon)
        except:
            print(f'{chara.name}는 그런 스킬을 가지고 있지 않는데요?')
    else:
        print(f'{chara.name}는 그런 스킬을 가지고 있지 않는데요?')


# mon1 = Monster(stage=1)

# a = Archer("Archer")
# b = Thief("Thief")
# d = Warrior("Warrior")
# c = Mage("Mage")

# skill_use(a, '화염마법', mon1)
# skill_use(c, '바람마법', mon1)
# skill_use(b, '은신', mon1)
# skill_use(b, '공격', mon1)


# 플레이어를 임력하면 가지고 있는 스킬목록을 리스트로 반환

# print(skills_that_have(a))
# print(skills_that_have(b))
# print(skills_that_have(c))
# print(skills_that_have(d))

# 테스트용 코드, a는 궁수, b는 도적
# skills_that_have(a) = ["은화살"]
# skills_that_have(b) = ["은신", "은신공격"]

# 출력

# 몬스터


# list = ['Thief', 'Archer', 'Mage', 'Warrior']

# def makingplayer(make_list):
#     players = ['player1', 'player2','player3','player4']
#     print(range(len(make_list)))
#     for i in range(len(make_list)):
#         if make_list[i] == 'Archer':
#             players[i] = Archer()
#             players
#         elif make_list[i] == 'Thief':
#             players[i] = Thief()
#         elif make_list[i] == 'Mage':
#             players[i] = Mage()
#         elif make_list[i] == 'Warrior':
#             players[i] = Warrior()
#         else:
#             print('잘못입력하셨습니다.')
#     return players

# makingplayer(list)


# print(players[3])

# players[1].silver_arrow_shot(mon1)

# print(type('archerkim').__name__)

# 메인에서 jobs = 'Archer' 보네면 ,
# ["포션1", "포션2", "포션3"]
# a = [1]
# b = []
# b.append(a)
# print(b)
# b.remove(a)
# print(b)
# print(len(b) == 0)
