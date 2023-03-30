# from monster import *
from item import *
# from player import *
# from gameplay import *
import random
import os


# 몬스터 그룹 생성
# generator = MonsterGenerator()
# print(f"{monster.type}")

# def action_select(players, skills, monsters):
#     select_action = 0

#     while select_action == 0:
#         # 플레이어 선택
#         select_erro = 0
#         actions_name = ["", "", ""]
#         while select_erro == 0:
#             try:
#                 temp_select(actions_name)
#                 temp = create_temp(players)
#                 print("player선택")
#                 get_action = input(temp)
#                 if 0 < int(get_action) and int(get_action) <= int(len(players)):
#                     actions_name[0] = players[int(get_action)-1]
#                     select_erro = 1
#             except:
#                 pass
#         # 행동선택
#         select_erro = 0
#         while select_erro == 0:
#             try:
#                 temp_select(actions_name)
#                 temp = create_temp(skills)
#                 print("action선택")
#                 get_action = input(temp)
#                 if 0 < int(get_action) and int(get_action) <= int(len(skills)):
#                     actions_name[1] = skills[int(get_action)-1]
#                     select_erro = 1
#             except:
#                 pass
#         # 대상 선택
#         select_erro = 0
#         while select_erro == 0:
#             try:
#                 temp_select(actions_name)
#                 temp = create_temp(monsters)
#                 print("공격대상 선택")
#                 get_action = input(temp)
#                 if 0 < int(get_action) and int(get_action) <= int(len(monsters)):
#                     actions_name[2] = monsters[int(get_action)-1]
#                     select_erro = 1
#             except:
#                 pass

#         # 확인
#         select_erro = 0
#         while select_erro == 0:
#             try:
#                 temp_select(actions_name)
#                 get_action = input("행동 선택 1-Yes , 2-No : ")
#                 if get_action == "1":
#                     select_erro = 1
#                     select_action = 1
#                     # key_action = {actions_name[0]: actions_name[1:3]}
#                 elif get_action == "2":
#                     select_erro = 1
#             except:
#                 pass

#     return actions_name

# def batlle():
#     player1 = Player("Player1")
#     player2 = Player("Player2")
#     players = [player1, player2]

#     monster1 = Monster("")
#     monster2 = Monster("")
#        //
#     monsters = [monster1, monster2, ~monster_n]



# turn = 1
# while players and monsters:
#     print(f"=={turn} 턴==")
#     for character in players:
#         target = monster[0]
#         character.attack(attack_type)
#         if not target.hp:
#             monsters.remove(target)
#     for monster in monsters:
#         target = random.randint(players)
#         monster.attack(target)
#         if not target.hp

# while True:
#     print(f"\n-- {turn} 턴 --\n")
#     for player in players:
#         print(f"{player.name}님의 차례입니다.")
#     unit = player.select_unit()
#     print(f"{player.name}님이 {unit.name}을(를) 선택하셨습니다.")

#     enemies = []
#     for enemy in players:
#         if enemy != player:
#             enemies.extend(enemy.units)
#     enemy = enemies[random.randint(0, len(enemies)-1)]
#     print(f"적으로 {enemy.name}을(를) 선택했습니다.")



#행동 텍스트
# print(f"{player1.jop}의 {attack_type} {attack_power} 피해 ")
# print(f"{monster1.name}의 {attack_type} {attack_power} 피해 ")
#  

#플레이어 , 행동 , 타겟 순서대로 출력
#지정순서 ex) player1(전사) 취할 행동을 입력 1.공격 2.파워어택 3.가드 1,2를 선택시 공격대상을 입력 goblin [0], orga [1], drake [2]



#몬스터 공격방식 



# 몬스터 공격방식 1. 기본값 일반 공격 
# 2.특정 몬스터에 한해 특수 공격 방식 ex) 방어력이 낮은 대상에게 우선공격, 공격력이 높은 대상에게 우선공격
# 속도가 낮은 대상에게 우선공격 스테이터스에 따른 공격 우선도 조정
# 일반 공격과 특수 공격 랜덤 사용 가중치를 주어 패턴 발현율 조정

# players_battle_list
# []
# monsters_battle_list 
# []

reward = Items.get(HpPortion)
print(reward)


# if len(self) == 0:     / 몬스터의 수 0 이 되면 승리 출력
# print("전투 승리")
# 
# player1 .get(reward) 보상 -- 아이템 획득 아이템은 장비 아이템(스테이터스 증가(영구적)) or 회복물약(HP or MP)
# stage() += 1 스테이지 클리어시 스테이지 단계 1증가 다음 스테이지로 속행


