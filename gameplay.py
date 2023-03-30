from pynput import keyboard
import re
import os
import time
from player import *


global key_zero
global key_n
global key_range
global key_m
global key_range_v

global enter_on
global isActive
key_n = 1
key_range = 4
key_m = 1
key_range_v = 2

# 키보드 in


def on_press(key):
    global key_n
    global key_range
    global key_m
    global key_range_v
    global enter_on
    global tab_on
    try:
        key_n_in = re.sub(r'[^0-9]', '', '{0}'.format(
            key.char))
        if key_n_in == "":
            pass
        else:
            key_n = int(key_n_in)
            if key_range < key_n:
                key_n = key_range
            elif 0 == key_n:
                key_n = 1
            # print(key_n)
    except AttributeError:
        if (key == keyboard.Key.up):
            key_m += 1
        elif (key == keyboard.Key.down):
            key_m -= 1
        elif (key == keyboard.Key.right):
            key_n = key_n % key_range
            key_n += 1
        elif (key == keyboard.Key.left):
            key_n -= 2
            key_n = key_n % key_range
            key_n += 1
        elif (key == keyboard.Key.enter):
            enter_on = True
        elif (key == keyboard.Key.tab):
            if tab_on:
                tab_on = False
            else:
                tab_on = True
# 키보드 out
        if key_m < 1:
            key_m = 1
        elif key_m > key_range:
            key_m = key_range


def on_release(key):
    if key == keyboard.Key.esc:  # esc 키가 입력되면 종료
        global isActive
        isActive = False
        return False


# 리스너 등록방법1
# with keyboard.Listener(
#        on_press=on_press, on_release=on_release) as listener:
#    listener.join()

#


def reset_global(key_range_n, key_range_m):
    global key_zero
    global key_n
    global key_range
    global key_m
    global key_range_v

    if key_zero:
        key_n = 1
        key_range = key_range_n
        key_m = 1
        key_range_v = key_range_m
        key_zero = False


###########################
# 캐릭터 선택
global charaters
charaters = []

global char_num
global change_m
char_num = 1
change_m = False


def display_1():
    global key_n
    global key_m
    global enter_on
    global key_zero
    global char_num
    global change_m

    charater_range = 4  # 명
    select_charaters = 4  # 선택창 4명

    reset_global(4, 3)

    print("직업선택선택")

    job_dic[jobs[key_n-1]](player_name).show_detail()
    # print(char_list)
    # 캐릭터 번호별 선택
    # print([key_n, key_m])
    # print(key_n)
    if (enter_on):
        enter_on = False
        key_zero = True
        charater = job_dic[jobs[key_n-1]](player_name)
        return 2
    else:
        return 1
#


char_list = [1, 1, 1]


def display_2():
    global key_n
    global key_m
    global enter_on
    global key_zero
    global char_num
    global change_m

    player_list = [1, 2, 3]
    skill_list = [1, 2]

    reset_global(3, 2)
    if key_m == 1:
        change_m = True
    if key_m == 2:
        if change_m:
            key_n = 1
            change_m = False
    return 2


# tab눌르면 정보 뛰우기
global tab_on
tab_on = False


def display_infos():
    global tab_on
    if (tab_on):
        print("info")


    # display
displayer_dic = {1: display_1,
                 2: display_2
                 }

#### display1######################


# 3

############## 게임시작#########################
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()

print("실행중입니다.")
player_name = input("사용자 이름 : ")
isActive = True
key_zero = True
display_n = 1
enter_on = False
while isActive:
    os.system('cls')
    display_infos()
    display_n = displayer_dic[display_n]()
    time.sleep(0.05)
    pass

print("종료했습니다.")
