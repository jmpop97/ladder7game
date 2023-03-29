from pynput import keyboard
import re
import os
import time

global key_n
global key_range
global isActive
key_n = 0
key_range = 5

# 선택지


def on_press(key):
    global key_n
    global key_range
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
            print(key_n)
    except AttributeError:
        if ('{0}'.format(key) == "Key.up"):
            key_n = key_n % key_range
            key_n += 1

        elif ('{0}'.format(key) == "Key.down"):
            key_n -= 2
            key_n = key_n % key_range
            key_n += 1
        elif ('{0}'.format(key) == "Key.right"):
            key_n = key_n % key_range
            key_n += 1
        elif ('{0}'.format(key) == "Key.left"):
            key_n -= 2
            key_n = key_n % key_range
            key_n += 1
        print(key_n)

# 종료


def on_release(key):
    if key == keyboard.Key.esc:  # esc 키가 입력되면 종료
        isActive = False
        return False

 # 리스너 등록방법1
# with keyboard.Listener(
#        on_press=on_press, on_release=on_release) as listener:
#    listener.join()


listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()

print("실행중입니다.")
isActive = True
while isActive:

    time.sleep(0.1)
    pass

print("종료했습니다.")
