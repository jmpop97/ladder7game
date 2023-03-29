from pynput import keyboard
import re
import os
import time

global key_zero
global key_n
global key_range

global enter_on
global isActive
key_n = 0
key_range = 5

# 키보드


def on_press(key):
    global key_n
    global key_range
    global enter_on
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
            key_n = key_n % key_range
            key_n += 1

        elif (key == keyboard.Key.down):
            key_n -= 2
            key_n = key_n % key_range
            key_n += 1
        elif (key == keyboard.Key.right):
            key_n = key_n % key_range
            key_n += 1
        elif (key == keyboard.Key.left):
            key_n -= 2
            key_n = key_n % key_range
            key_n += 1
        if (key == keyboard.Key.enter):
            enter_on = True
        # print(key_n)

# 종료


def on_release(key):
    if key == keyboard.Key.esc:  # esc 키가 입력되면 종료
        isActive = False
        return False

# 리스너 등록방법1
# with keyboard.Listener(
#        on_press=on_press, on_release=on_release) as listener:
#    listener.join()

#


def reset_global(key_range_n):
    global key_zero
    global key_n
    global key_range
    if key_zero:
        key_n = 1
        key_range = key_range_n
        key_zero = False


###########################
# 캐릭터 선택
def display_1():
    global key_n
    global enter_on

    charater_range = 4  # 명

    print("캐릭터를 생성하세요")
    # 캐릭터 번호별 선택택
    reset_global(charater_range)
    charater_n = key_n
    select_charater(charater_n)
    if (enter_on):
        return 2
    else:
        return 1
#


def display_2():
    print("몬스터")
    return 2


# display
displayer_dic = {1: display_1,
                 2: display_2
                 }

#### display1######################


def select_charater(charater_n):
    print("charater_info"+str(charater_n))


# 3
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()

print("실행중입니다.")
isActive = True
key_zero = True
display_n = 1
enter_on = False
while isActive:
    os.system('cls')
    display_n = displayer_dic[display_n]()
    time.sleep(0.1)
    pass

print("종료했습니다.")
