generator = MonsterGenerator(10)
monsters = generator.monsters
count_dict = {}
for i, (level, name, monster) in enumerate(monsters):
    count_dict[name] = count_dict.get(name, 0) + 1
    count = count_dict[name]
    print(f"{i+1}. 몬스터 이름: {name}{count}, 등급: {level}, 레벨: {monster.level}, 체력: {monster.hp}, 공격력: {monster._str}")
