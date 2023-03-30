from player import *

# 전투를 수행하는 함수
def battle(player, enemy):
    # 전투 시작
    print("전투 시작!")
    # 턴 수 초기화
    turn = 1
    # player와 enemy의 HP가 0보다 큰 동안 반복
    while player.hp > 0 and enemy.hp > 0:
        # 턴 정보 출력
        print(f"=== {turn}번째 턴 ===")
        # player와 enemy의 현재 체력 정보 출력
        print(f"{player.name}: {player.hp}/{player.max_hp} HP")
        print(f"{enemy.name}: {enemy.hp}/{enemy.max_hp} HP")
        # player의 행동 선택
        print(f"{player.name}의 행동을 선택하세요.")
        print("1. 기본 공격")
        print("2. 특수 공격")
        print("3. 물약 사용")
        print("4. 도망가기")
        action = input("선택: ")
        # 선택에 따른 동작 수행
        if action == "1":
            player.attack(enemy)
        elif action == "2":
            player.power_attack(enemy)
        elif action == "3":
            # 물약 목록 출력
            print("=== 물약 목록 ===")
            print(f"{red_portion.name}: {red_portion.amount}개")
            print(f"{white_portion.name}: {white_portion.amount}개")
            print(f"{blue_portion.name}: {blue_portion.amount}개")
            # 사용할 물약 선택
            potion_name = input("어떤 물약을 사용하시겠습니까? ")
            if potion_name == red_portion.name:
                red_portion.use(player)
            elif potion_name == white_portion.name:
                white_portion.use(player)
            elif potion_name == blue_portion.name:
                blue_portion.use(player)
            else:
                print("잘못된 입력입니다.")
                continue
        elif action == "4":
            print(f"{player.name}은 전투에서 도망쳤습니다.")
            return False
        else:
            print("잘못된 입력입니다.")
            continue

        # enemy의 HP가 0보다 큰 경우 enemy가 공격
        if enemy.hp > 0:
            enemy.attack(player)

        # 턴 수 증가
        turn += 1

    # player의 체력이 0 이하인 경우
    if player.hp <= 0:
        print(f"{player.name}이(가) 죽었습니다. 게임 오버!")
        return False
    # enemy의 체력이 0 이하인 경우
    elif enemy.hp <= 0:
        print(f"{enemy.name}을(를) 물리쳤습니다. 전투에서 승리했습니다!")
        return True
