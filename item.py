from player import *


# 물약 공통 클래스


class Portion:
    def __init__(self, name, effect):
        # 물약 이름, 효과, 양 지정
        self.name = name
        self.effect = effect
        self.amount = 0

# 체력 물약 클래스


class HpPortion(Portion):
    # .get 메소드로 물약 획득 시, 수량 1 씩 증가
    def get(self):
        print(f"{self.name}을 획득했습니다.")
        self.amount += 1
    # .use 메소드로 물약 사용 시, self.effect 만큼 체력 회복

    def use(self, owner):
        if self.amount < 1:
            print(f"{self.name}이 부족합니다.")
            return False
        else:
            if owner.hp >= owner.max_hp:
                print(f"{owner.name}의 HP가 최대입니다.")
                return False
            else:
                print(
                    f"{self.name}을 사용 하셨습니다. {owner.name}의 HP를 {self.effect}만큼 회복합니다.")
                owner.hp = min(owner.hp+self.effect, owner.max_hp)
                self.amount -= 1
                return True

# 마력 물약 클래스


class MpPortion(Portion):
    # .get 메소드로 물약 획득 시, 수량 1 씩 증가
    def get(self):
        print(f"{self.name}을 획득했습니다.")
        self.amount += 1
    # .use 메소드로 물약 사용 시, self.effect 만큼 체력 회복

    def use(self, owner):
        if self.amount < 1:
            print(f"{self.name}이 부족합니다.")
            return False
        else:
            print(f"{self.name}을 사용 하셨습니다. {owner.name}의 MP를 {self.effect}만큼 회복합니다.")
            owner.mp += self.effect
            self.amount -= 1


class Item:
    # 아이템 이름과 능력을 이닛으로 받음
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect

# _str 능력치를 올려주는 아이템


class StrItem(Item):
    # .get 메소드로 소유자 지정해서 장착 가능! self.effect만큼 능력치 증가
    def get(self, owner):
        print(f"{owner.name}에게 {self.name}을(를) 장착했습니다.")
        owner._str += self.effect

# arm 능력치를 올려주는 아이템


class ArmItem(Item):
    # .get 메소드로 소유자 지정해서 장착 가능! self.effect만큼 능력치 증가
    def get(self, owner):
        print(f"{owner.name}에게 {self.name}을(를) 장착했습니다.")
        owner.arm += self.effect

# int 능력치를 올려주는 아이템


class IntItem(Item):
    # .get 메소드로 소유자 지정해서 장착 가능! self.effect만큼 능력치 증가
    def get(self, owner):
        print(f"{owner.name}에게 {self.name}을(를) 장착했습니다.")
        owner._int += self.effect

# spd 능력치를 올려주는 아이템


class SpdItem(Item):
    # .get 메소드로 소유자 지정해서 장착 가능! self.effect만큼 능력치 증가
    def get(self, owner):
        print(f"{owner.name}에게 {self.name}을(를) 장착했습니다.")
        owner.spd += self.effect

# 최대 hp를 올려주는 아이템


class HpItem(Item):
    # .get 메소드로 소유자 지정해서 장착 가능! self.effect만큼 능력치 증가
    def get(self, owner):
        print(f"{owner.name}에게 {self.name}을(를) 장착했습니다.")
        owner.max_hp += self.effect

# 최대 mp를 올려주는 아이템


class MpItem(Item):
    # .get 메소드로 소유자 지정해서 장착 가능! self.effect만큼 능력치 증가
    def get(self, owner):
        print(f"{owner.name}에게 {self.name}을(를) 장착했습니다.")
        owner.max_mp += self.effect


red_portion = HpPortion("빨간물약", 10)
white_portion = HpPortion("하얀물약", 50)
blue_portion = MpPortion("파란물약", 10)
sword = StrItem("검", 10)
shield = ArmItem("방패", 10)
staff = IntItem("지팡이", 10)
shoe = SpdItem("신발", 10)
necklace = HpItem("목걸이", 10)
ring = MpItem("반지", 10)

# --물약 사용법--
# 체력 물약 종류: 빨간물약(체력 10 회복), 하얀물약(체력 50 회복)
# 마력 물약 종류: 파란물약(마력 10 회복)
# 체력 물약 획득: red_portion.get() /빨간물약 획득/   white_portion.get() /하얀물약 획득/
# 체력 물약 사용: red_portion.use("사용자") /"사용자"에게 빨간물약 사용/   white_portion.use("사용자") /"사용자"에게 하얀물약 사용/
# 마력 물약 획득: blue_portion.get() /파란물약 획득/
# 마력 물약 사용: blue_portion.use("사용자")  /"사용자"에게 파란물약 사용/


# --아이템 사용법---
# 아이템 종류: 검(힘 10 증가), 방패(방어력 10 증가), 지팡이(지능 10 증가), 신발(스피드 10 증가), 목걸이(최대 체력 10 증가), 반지(최대 마력 10 증가)
# 아이템 착용: 검 = sword.get("착용자") 방패 = shield.get("착용자") 지팡이 = staff.get("착용자") 신발 = shoe.get("착용자") 목걸이 = necklace.get("착용자") 반지 = ring.get("착용자")

ar = Archer()
ar.hp -= 8
ar.status
red_portion.get()
red_portion.use(ar)
ar.show_detail
red_portion.get()
red_portion.use(ar)
ar.show_detail
