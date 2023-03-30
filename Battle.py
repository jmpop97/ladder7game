from item import *
import random

# 전투
def battle(player, monsters):
    # 턴 수 초기화
    turn = 1

    # 모든 몬스터가 죽을 때까지 반복
    while monsters:
        print(f"\n=== Turn {turn} ===")

        # 플레이어의 공격 선택
        print("1. 일반공격")
        print("2. 스킬")
        print("3. 스킬2")
        attack_type = int(input("행동 선택"))

        # 플레이어가 공격
        if attack_type == 1:
            print(f"{player.name} 일반공격을 사용")
            damage = player.attack()
        elif attack_type == 2:
            skill = player.use_skill()
            print(f"{player.name} {skill.name} 사용")
            damage = skill.damage
        elif attack_type == 3:
            skill = player.use_skill()
            print(f"{player.name} {skill.name} 사용")
            damage = skill.damage

        # 랜덤으로 몬스터 선택 후 공격
        monster = random.choice(monsters)
        monster.hp -= damage
        print(f"{monster.name}에게 {damage}의 데미지")
        
        # 적이 죽었을 경우
        if monster.hp <= 0:
            print(f"{monster.name} 처치")
            monsters.remove(monster)

        # 모든 몬스터가 죽었을 경우
        if not monsters:
            print("모든 적을 처치")
            return True

        # 몬스터가 공격
        damage = monster.attack()
        player.hp -= damage
        print(f"{player.name}에게 {damage}의 데미지")

        # 플레이어가 죽었을 경우
        if player.hp <= 0:
            print(f"{player.name}이(가) 쓰러졌다.")
            return False

        turn += 1


# 스테이지 클리어 후 보상 지급 함수
def clear_stage(player, stage):
    print(f"스테이지 {stage} 클리어")
    reward = stage_clear_reward(stage)
    print(f"보상으로 {reward} 획득.")
    player.Items.append(reward)

    Items = (Item,Portion)
    reward = Items.get()

# 스테이지 클리어시 포션 1개 획득, 아이템 1개 선택해서 획득
# 스테이지 클리어 보상은 추가 예정

def stage_clear_reward(stage):
    if stage == 1:
        return HpPortion,1
    elif stage == 2:
        return 
    elif stage == 3:
        return 
    elif stage == 4:
        return 
    elif stage == 5:
        return 
    elif stage == 6:
        return 
    elif stage == 7:
        return 
    elif stage == 8:
        return 
    elif stage == 9:
        return 
    elif stage == 10:
        return 

