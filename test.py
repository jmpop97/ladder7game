import random
import itertools


class Monster:

    monster_types = {
        "초급": ["고블린", "스켈레톤", "좀비", "오크", "슬라임"],
        "중급": ["트롤", "웨어울프", "마미라", "미노타우르스", "하피"],
        "고급": ["뱀파이어", "걸렘", "데몬", "드래곤", "벨벳"]
    }

    monster_stats = {
        "고블린": {"hp": 20, "str": 2},
        "스켈레톤": {"hp": 25, "str": 3},
        "좀비": {"hp": 30, "str": 4},
        "오크": {"hp": 35, "str": 5},
        "슬라임": {"hp": 40, "str": 6},
        "트롤": {"hp": 50, "str": 7},
        "웨어울프": {"hp": 55, "str": 8},
        "마미라": {"hp": 60, "str": 9},
        "미노타우르스": {"hp": 65, "str": 10},
        "하피": {"hp": 70, "str": 11},
        "뱀파이어": {"hp": 80, "str": 12},
        "걸렘": {"hp": 85, "str": 13},
        "데몬": {"hp": 90, "str": 14},
        "드래곤": {"hp": 100, "str": 15},
        "벨벳": {"hp": 110, "str": 16}
    }

    def __init__(self, stage, type):
        self.stage = stage
        self.type = type
        self.hp = Monster.monster_stats[type]["hp"] + 5 * (stage // 3)
        self._str = Monster.monster_stats[type]["str"] + 2 * (stage // 3)
        self.level = stage

    def get_monster_type(self):
        # 스테이지에 맞는 몬스터 등급을 선정하고, 해당 등급에서 랜덤한 몬스터 선택
        if self.stage < 5:
            monster_level = "초급"
        elif self.stage < 8:
            monster_level = "중급"
        else:
            monster_level = "고급"

        return random.choice(Monster.monster_types[monster_level])

    def attack_player(self, player):
        damage = self._str - player.defense
        if damage < 0:
            damage = 0
        player.hp -= damage
        print(f"{self.type}이(가) {player.name}에게 {damage}의 피해를 입혔습니다.")


class MonsterGenerator:
    def __init__(self, stage):
        self.stage = stage
        self.monsters = self.generate_monsters()

    def generate_monsters(self):
        # 스테이지별 몬스터 수 범위 설정
        min_monsters = max(1, self.stage - 2)
        max_monsters = min(10, self.stage + 2)

        monster_levels = []
        if self.stage < 4:
            monster_levels = itertools.repeat("초급", max_monsters)
        elif self.stage < 8:
            monster_levels = itertools.chain.from_iterable(
                itertools.repeat(x, 2) for x in ["중급"])
            monster_levels = itertools.chain(
                monster_levels, itertools.repeat("중급", max_monsters - 4))
        else:
            monster_levels = itertools.chain.from_iterable(
                itertools.repeat(x, 3) for x in ["고급"])
            monster_levels = itertools.chain(
                monster_levels, itertools.repeat("고급", max_monsters - 3))

        monsters = []
        for i, level in enumerate(itertools.islice(monster_levels, max_monsters)):
            name = random.choice(list(Monster.monster_types[level]))
            monster = Monster(self.stage, name)
            monsters.append((level, name, monster))

        return monsters


# 스테이지 10 몬스터 출력
generator = MonsterGenerator(10)
monsters = generator.monsters
count_dict = {}
for i, (level, name, monster) in enumerate(monsters):
    count_dict[name] = count_dict.get(name, 0) + 1
    count = count_dict[name]
    print(f"{i+1}. 몬스터 이름: {name}{count}, 등급: {level}, 레벨: {monster.level}, 체력: {monster.hp}, 공격력: {monster._str}")

generator = MonsterGenerator(10)
monsters = generator.monsters
for monster in monsters:
    print(repr(monster[2]))
