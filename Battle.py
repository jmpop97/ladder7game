# import random
# # from player import *

# class Player:
#     def __init__(self, hp, atk):
#         self.name = "Player"
#         self.hp = hp
#         self.max_hp = hp
#         self.attack = atk
#         self.normal_attack = "1"

#     def get_damage(self, damage):
#         self.health -= damage
#         if self.health < 0:
#             self.health = 0
#         print(f"{self.name}의 체력이 {self.health}가 되었습니다.")

# class Monster:
#     def __init__(self):
#         self.name = f"Monster {random.randint(1, 10)}"
#         self.health = random.randint(50, 80)
#         self.attack = random.randint(5, 15)

#     def get_damage(self, damage):
#         self.health -= damage
#         if self.health < 0:
#             self.health = 0
#         print(f"{self.name}의 체력이 {self.health}가 되었습니다.")

#     def attack_player(self, player):
#         damage = self.attack
#         print(f"{self.name}가 {player.name}을 공격했습니다. 데미지: {damage}")
#         player.get_damage(damage)


# def battle(player, monsters):
#     print(f"{player.name} vs. Monsters")
#     print("=========")

#     for i, monster in enumerate(monsters):
#         print(f"Stage {i+1}: {monster.name} vs. {player.name}")
#         print("---------")


#     while True:
#         attack_type = input("공격 = 1 던지기 = 2")
#         attack_power = player.attack(attack_type)
#         monster.hp -= attack_power
#         print(f"{player.name}의 {monster.name}에게 {attack_power}의 데미지")
#         if attack_power:
#             break

#     monster.attack_player(player)
#         if player.health <= 0:
#         break

#     if player.health <= 0:
#         print(f"{player.name}이 패배하였습니다.")
#         break
#     elif monster.health <= 0:
#         print(f"{monster.name}을 처치하였습니다.")
#         print("")

#     if player.health > 0:
#         print(f"{player.name}이 모든 몬스터를 처치하였습니다.")

# player = Player()
# monsters = [Monster() for i in range(3)]
# battle(player, monsters)



#     if len(monster_count) == 0:
#         print(f"==========전투 승리!==========")
#         print(f"보상으로 {reward}을/를 획득했다")

# reward = random.randint(Portion).get() sword.get(input)
# print(reward)


# if len(self) == 0:     / 몬스터의 수 0 이 되면 승리 출력
# print("전투 승리")
# 
# player1 .get(reward) 보상 -- 아이템 획득 아이템은 장비 아이템(스테이터스 증가(영구적)) or 회복물약(HP or MP)
# stage() += 1 스테이지 클리어시 스테이지 단계 1증가 다음 스테이지로 속행

import random

# 플레이어 클래스
class Player:
    def __init__(self, name, job):
        self.name = name
        self.job = job
        self.max_hp = 100
        self.hp = self.max_hp
        self.atk = 10
        self.gold = 0
        self.skills = {"치유": 20, "불꽃세례": 30} if self.job == "성기사" else {"돌격": 20, "발차기": 30} if self.job == "격투가" else {"화염구": 20, "번개벼락": 30} if self.job == "마법사" else {}

    def attack(self, target):
        damage = self.atk
        target.hp -= damage
        print(f"{self.name}이(가) {target.name}에게 {damage}의 데미지를 입혔습니다.")
        if target.hp <= 0:
            target.hp = 0
            target.alive = False
            print(f"{target.name}을(를) 물리쳤습니다!")
    
    def use_skill(self, target, skill_name):
        if skill_name in self.skills:
            damage = self.skills[skill_name]
            target.hp -= damage
            print(f"{self.name}이(가) {target.name}에게 {skill_name} 스킬로 {damage}의 데미지를 입혔습니다.")
            if target.hp <= 0:
                target.hp = 0
                target.alive = False
                print(f"{target.name}을(를) 물리쳤습니다!")
        else:
            print("해당 스킬을 사용할 수 없습니다.")
    
    def heal(self):
        heal_point = self.skills["치유"]
        self.hp += heal_point
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        print(f"{self.name}의 체력이 {heal_point}만큼 회복되었습니다. 현재 체력: {self.hp}")
    

# 몬스터 클래스
class Monster:
    def __init__(self, name, hp, atk):
        self.name = name
        self.max_hp = hp
        self.hp = self.max_hp
        self.atk = atk
        self.alive = True
    
    def attack(self, target):
        damage = self.atk
        target.hp -= damage
        print(f"{self.name}이(가) {target.name}에게 {damage}의 데미지를 입혔습니다.")
        if target.hp <= 0:
            target.hp = 0
            target.alive = False
            print(f"{target.name}이(가) 쓰러졌습니다.")


# 스테이지 클리어 후 보상 지급 함수
def clear_stage(player, stage):
    print(f"스테이지 {stage}를 클리어하였습니다!")
    reward = stage_clear_reward(stage)
    print(f"보상으로 {reward}의 골드를 획득하였습니다.")
    player.gold += reward


def stage_clear_reward(stage):
    if stage == 1:
        return 100
    elif stage == 2:
        return 150
    elif stage == 3:
        return 200
    elif stage == 4:
        return 250
    elif stage == 5:
        return 300
    elif stage == 6:
        return 350
    elif stage == 7:
        return 400
    elif stage == 8:
        return 450
    elif stage == 9:
        return 500
    elif stage == 10:
        return 1000

