import random


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
        pass

    def status(self):
        print(f"{self.name}: Hp {self.hp}/{self.max_hp} MP {self.max_mp}/{self.max_mp}")

    def attack(self, other):
        damage = random.randint(self.str, self.str*)
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")


class Player(BaseCharacter):
    pass


class Monster(BaseCharacter):
    pass


# start game

# 직업선택

# output: charaters=[직업1,직업2,...]

# 몬스터 생성
stage_monster = {1: [""],
                 2: [""]}

# 스테이지 시작
stage_n = 1
stage(charaters, stage_monster[stage_n])
# 현재상태 출력
# 공격순서list
# 공격순서list순 공격
# 승리 시 보상
